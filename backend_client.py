import httpx
import os
from datetime import datetime, timedelta
from typing import Optional

_token: Optional[str] = None
_token_expires_at: Optional[datetime] = None

BACKEND_URL = os.getenv("CSHARP_API_URL", "http://localhost:5130")
AIBOT_EMAIL = os.getenv("AIBOT_EMAIL", "aibot@system.com")
AIBOT_PASSWORD = os.getenv("AIBOT_PASSWORD", "AiBot123!")


async def _get_token() -> Optional[str]:
    global _token, _token_expires_at
    if _token and _token_expires_at and datetime.now() < _token_expires_at:
        return _token
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"{BACKEND_URL}/api/auth/login",
                json={"email": AIBOT_EMAIL, "password": AIBOT_PASSWORD},
            )
            if r.status_code == 200:
                data = r.json()
                _token = data.get("token")
                _token_expires_at = datetime.now() + timedelta(minutes=55)
                return _token
    except Exception:
        pass
    return None


def _map_car(c: dict) -> dict:
    return {
        "id": c.get("id"),
        "business_account_id": c.get("businessAccountId"),
        "title": c.get("title", ""),
        "description": c.get("description", ""),
        "brand": (c.get("brand") or "").lower(),
        "model": c.get("model", ""),
        "year": str(c.get("year", "")),
        "mileage": str(c.get("mileage", "0")),
        "color": c.get("color", ""),
        "price_usd": float(c.get("priceUsd", 0)),
        "price_syp": int(c.get("priceSyp", 0)),
        "status": c.get("status", ""),
        "condition": c.get("condition", ""),
        "fuel_type": c.get("fuelType", ""),
        "body_type": c.get("bodyType", ""),
        "gear_type": c.get("gearType", ""),
        "clicks": c.get("clicks", 0),
        "likes": c.get("likes", 0),
        "dislikes": c.get("dislikes", 0),
        "favorite_count": c.get("favoriteCount", 0),
        "days_listed": c.get("daysListed", 0),
        "average_model_price": int(c.get("averageModelPrice", 0)),
        "doors": c.get("doors", 4),
        "interior_color": c.get("interiorColor", ""),
        "main_photo_url": c.get("mainPhotoUrl") or "",
    }


async def search_real_cars(
    budget_min: int = 0,
    budget_max: int = 999_999_999,
    brand: Optional[str] = None,
    body_type: Optional[str] = None,
    fuel_type: Optional[str] = None,
    year_min: Optional[int] = None,
    limit: int = 3,
) -> list:
    token = await _get_token()
    if not token:
        return []

    params: dict = {"priceMinSyp": budget_min, "priceMaxSyp": budget_max}
    if brand:
        params["brand"] = brand
    if body_type:
        params["bodyType"] = body_type
    if fuel_type:
        params["fuelType"] = fuel_type
    if year_min:
        params["yearMin"] = str(year_min)

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                f"{BACKEND_URL}/api/ai/cars/filter",
                params=params,
                headers={"Authorization": f"Bearer {token}"},
            )
            if r.status_code == 200:
                cars = r.json().get("data") or []
                mapped = [_map_car(c) for c in cars]
                mapped.sort(
                    key=lambda x: (
                        -(int(x["year"]) if x["year"].isdigit() else 0),
                        int(x["mileage"]) if x["mileage"].isdigit() else 0,
                        -x["favorite_count"],
                    )
                )
                return mapped[:limit]
    except Exception:
        pass
    return []


async def get_all_cars() -> list:
    token = await _get_token()
    if not token:
        return []

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                f"{BACKEND_URL}/api/ai/cars/filter",
                headers={"Authorization": f"Bearer {token}"},
            )
            if r.status_code == 200:
                cars = r.json().get("data") or []
                return [_map_car(c) for c in cars]
    except Exception:
        pass
    return []
