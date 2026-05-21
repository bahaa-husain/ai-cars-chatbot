# Car Marketplace AI Service

AI chatbot backend for a Syrian car marketplace. Built with FastAPI and Groq (LLaMA 3.3 70B). Handles Arabic conversations, car search, price analysis, and personalized recommendations.

## Stack
- **FastAPI** — REST API
- **Groq** — LLM inference (llama-3.3-70b-versatile)
- **Python-dotenv** — env config

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Add a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Run:
```bash
uvicorn main:app --reload
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Service status |
| POST | `/ai/chat` | Arabic car chatbot |
| POST | `/ai/recommendations` | Personalized car picks |
| POST | `/ai/recommendations/feedback` | User feedback |
