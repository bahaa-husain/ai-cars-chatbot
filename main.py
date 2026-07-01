from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
from prompts import build_system_prompt
from mock_data import get_market_analysis
from backend_client import search_real_cars, get_all_cars
from intent import detect_intent, extract_entities
from recommendations import get_recommendations
from typing import List, Optional
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI(title="Car Marketplace AI Service", version="1.0.0")


class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    user_id: str
    history: Optional[List[Message]] = []
    inventory_context: Optional[str] = ""

class RecommendationRequest(BaseModel):
    user_id: str
    viewed_car_ids: Optional[List[int]] = []
    favorite_car_ids: Optional[List[int]] = []
    budget_max: Optional[int] = None
    preferred_brand: Optional[str] = None

class FeedbackRequest(BaseModel):
    user_id: str
    car_id: int
    action: str


def format_cars_for_prompt(cars: list) -> str:
    if not cars:
        return "لا توجد سيارات مطابقة."
    result = ""
    for i, car in enumerate(cars, 1):
        analysis = get_market_analysis(car)
        result += f"""
سيارة {i}: {car['title']} {car['year']}
- السعر: {car['price_syp']:,} ل.س | الممشى: {car['mileage']} كم
- تقييم السعر: {analysis['verdict']} | {analysis['negotiation_tip']}
- {car['description']}
"""
    return result


@app.get("/")
def root():
    return {"status": "AI Service is running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "llama-3.3-70b-versatile",
        "data_source": "real"
    }

@app.post("/ai/chat")
async def chat(request: ChatRequest):
    try:
        intent = detect_intent(request.message)
        entities = extract_entities(request.message)
        cars = []
        cars_context = ""

        if intent == "search_cars":
            budget = entities["budget"]
            cars = await search_real_cars(
                budget_min=budget["min"],
                budget_max=budget["max"],
                brand=entities["brand"],
                body_type=entities["body_type"],
                fuel_type=entities["fuel_type"],
                year_min=entities["year"],
            )
            cars_context = f"\n\nنتائج البحث:\n{format_cars_for_prompt(cars)}"
            if not cars:
                cars_context = "\n\nما لقينا سيارات بهالمواصفات — اقترح بدائل مناسبة للمستخدم."

        system = build_system_prompt(request.inventory_context) + cars_context
        messages = [{"role": "system", "content": system}]
        for msg in request.history[-8:]:
            messages.append({"role": msg.role, "content": msg.content})
        messages.append({"role": "user", "content": request.message})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )

        return {
            "reply": response.choices[0].message.content,
            "user_id": request.user_id,
            "intent": intent,
            "entities": entities,
            "cars": cars,
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/ai/recommendations")
async def recommendations(request: RecommendationRequest):
    try:
        all_cars = await get_all_cars()
        recs = get_recommendations(
            user_id=request.user_id,
            viewed_car_ids=request.viewed_car_ids,
            favorite_car_ids=request.favorite_car_ids,
            budget_max=request.budget_max,
            preferred_brand=request.preferred_brand,
            all_cars=all_cars,
        )
        return {
            "user_id": request.user_id,
            "recommendations": recs,
            "total": sum(len(v) for v in recs.values())
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/ai/recommendations/feedback")
def feedback(request: FeedbackRequest):
    return {"status": "ok", "message": "تم تسجيل التفاعل"}
