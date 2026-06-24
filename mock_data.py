from typing import Optional
from enums import BodyType, CarCondition, CarStatus, FuelType, GearType

MOCK_CARS = [
    {
        "id": 1,
        "business_account_id": 1,
        "title": "تويوتا كامري",
        "description": "سيارة بحالة ممتازة، صيانة دورية، مالك واحد",
        "brand": "toyota",
        "model": "Camry",
        "year": "2023",
        "mileage": "15000",
        "color": "أبيض",
        "price_usd": 2800,
        "price_syp": 42_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.Sedan,
        "gear_type": GearType.Auto,
        "clicks": 320,
        "likes": 31,
        "dislikes": 4,
        "favorite_count": 45,
        "days_listed": 12,
        "average_model_price": 44_000_000,
        "doors": 4,
        "interior_color": "بيج",
        "main_photo_url": "/photos/camry_2023.jpg",
    },
    {
        "id": 2,
        "business_account_id": 2,
        "title": "هوندا أكورد",
        "description": "سيارة نظيفة جداً، كاملة المواصفات",
        "brand": "honda",
        "model": "Accord",
        "year": "2022",
        "mileage": "28000",
        "color": "رمادي",
        "price_usd": 2533,
        "price_syp": 38_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.Sedan,
        "gear_type": GearType.Auto,
        "clicks": 210,
        "likes": 21,
        "dislikes": 3,
        "favorite_count": 30,
        "days_listed": 35,
        "average_model_price": 41_000_000,
        "doors": 4,
        "interior_color": "أسود",
        "main_photo_url": "/photos/accord_2022.jpg",
    },
    {
        "id": 3,
        "business_account_id": 3,
        "title": "كيا سبورتاج",
        "description": "شبه جديدة، ضمان سنة، فل أوبشن",
        "brand": "kia",
        "model": "Sportage",
        "year": "2023",
        "mileage": "8000",
        "color": "أسود",
        "price_usd": 3867,
        "price_syp": 58_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.SUV,
        "gear_type": GearType.Auto,
        "clicks": 540,
        "likes": 62,
        "dislikes": 5,
        "favorite_count": 89,
        "days_listed": 5,
        "average_model_price": 60_000_000,
        "doors": 4,
        "interior_color": "بيج",
        "main_photo_url": "/photos/sportage_2023.jpg",
    },
    {
        "id": 4,
        "business_account_id": 4,
        "title": "نيسان سنترا",
        "description": "اقتصادية جداً بالوقود، مناسبة للمدينة",
        "brand": "nissan",
        "model": "Sentra",
        "year": "2022",
        "mileage": "35000",
        "color": "أزرق",
        "price_usd": 2133,
        "price_syp": 32_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.Sedan,
        "gear_type": GearType.Auto,
        "clicks": 180,
        "likes": 15,
        "dislikes": 2,
        "favorite_count": 22,
        "days_listed": 20,
        "average_model_price": 33_000_000,
        "doors": 4,
        "interior_color": "رمادي",
        "main_photo_url": "/photos/sentra_2022.jpg",
    },
    {
        "id": 5,
        "business_account_id": 5,
        "title": "هيونداي توسان",
        "description": "SUV عائلي مريح، صيانة وكالة",
        "brand": "hyundai",
        "model": "Tucson",
        "year": "2022",
        "mileage": "22000",
        "color": "أبيض",
        "price_usd": 4133,
        "price_syp": 62_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.SUV,
        "gear_type": GearType.Auto,
        "clicks": 390,
        "likes": 47,
        "dislikes": 6,
        "favorite_count": 67,
        "days_listed": 18,
        "average_model_price": 64_000_000,
        "doors": 4,
        "interior_color": "أسود",
        "main_photo_url": "/photos/tucson_2022.jpg",
    },
    {
        "id": 6,
        "business_account_id": 6,
        "title": "تويوتا كورولا",
        "description": "موثوقة جداً، استهلاك وقود ممتاز",
        "brand": "toyota",
        "model": "Corolla",
        "year": "2021",
        "mileage": "45000",
        "color": "فضي",
        "price_usd": 1867,
        "price_syp": 28_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.Sedan,
        "gear_type": GearType.Auto,
        "clicks": 450,
        "likes": 55,
        "dislikes": 7,
        "favorite_count": 78,
        "days_listed": 8,
        "average_model_price": 29_000_000,
        "doors": 4,
        "interior_color": "بيج",
        "main_photo_url": "/photos/corolla_2021.jpg",
    },
    {
        "id": 7,
        "business_account_id": 7,
        "title": "كيا سيراتو",
        "description": "شبه جديدة، مواصفات عالية، سعر منافس",
        "brand": "kia",
        "model": "Cerato",
        "year": "2023",
        "mileage": "12000",
        "color": "أحمر",
        "price_usd": 2333,
        "price_syp": 35_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.Sedan,
        "gear_type": GearType.Auto,
        "clicks": 290,
        "likes": 29,
        "dislikes": 3,
        "favorite_count": 41,
        "days_listed": 14,
        "average_model_price": 36_000_000,
        "doors": 4,
        "interior_color": "أسود",
        "main_photo_url": "/photos/cerato_2023.jpg",
    },
    {
        "id": 8,
        "business_account_id": 8,
        "title": "مازدا 6",
        "description": "تصميم راقي، أداء ممتاز، سعر أقل من السوق",
        "brand": "mazda",
        "model": "Mazda6",
        "year": "2022",
        "mileage": "19000",
        "color": "أبيض",
        "price_usd": 3133,
        "price_syp": 47_000_000,
        "status": CarStatus.Available,
        "condition": CarCondition.Used,
        "fuel_type": FuelType.Gas,
        "body_type": BodyType.Sedan,
        "gear_type": GearType.Auto,
        "clicks": 260,
        "likes": 27,
        "dislikes": 3,
        "favorite_count": 38,
        "days_listed": 25,
        "average_model_price": 50_000_000,
        "doors": 4,
        "interior_color": "بيج",
        "main_photo_url": "/photos/mazda6_2022.jpg",
    },
]


def search_mock_cars(
    budget_min: int = 0,
    budget_max: int = 999_999_999,
    brand: Optional[str] = None,
    body_type: Optional[str] = None,
    year_min: Optional[int] = None,
    limit: int = 3
) -> list:
    results = []
    for car in MOCK_CARS:
        if not (budget_min <= car["price_syp"] <= budget_max):
            continue
        if brand and brand.lower() not in car["brand"].lower():
            continue
        if body_type:
            try:
                if car["body_type"] != BodyType[body_type]:
                    continue
            except KeyError:
                continue
        if year_min and int(car["year"]) < year_min:
            continue
        results.append(car)

    results.sort(key=lambda x: (-int(x["year"]), int(x["mileage"]), -x["favorite_count"]))
    return results[:limit]


def get_market_analysis(car: dict) -> dict:
    diff = car["price_syp"] - car["average_model_price"]
    pct = round((diff / car["average_model_price"]) * 100, 1)

    if pct <= -5:
        verdict = "صفقة ممتازة 🟢"
    elif pct <= 5:
        verdict = "سعر عادل 🟡"
    else:
        verdict = "غالي نسبياً 🔴"

    if car["days_listed"] > 30:
        tip = "ابدأ بعرض أقل بـ 15% — الإعلان قديم"
    elif car["days_listed"] > 7:
        tip = "ممكن تتفاوض بـ 5-8%"
    else:
        tip = "إعلان جديد — التفاوض محدود هلق"

    return {"verdict": verdict, "difference_pct": pct, "days_listed": car["days_listed"], "negotiation_tip": tip}
