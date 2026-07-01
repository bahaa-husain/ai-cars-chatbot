from mock_data import get_market_analysis
from typing import Optional


def get_recommendations(
    user_id: int,
    viewed_car_ids: list = [],
    favorite_car_ids: list = [],
    budget_max: Optional[int] = None,
    preferred_brand: Optional[str] = None,
    limit: int = 3,
    all_cars: list = [],
) -> dict:
    return {
        "suggested_for_you": _suggested_for_you(budget_max, preferred_brand, viewed_car_ids, limit, all_cars),
        "best_deals": _best_deals(limit, all_cars),
        "similar_to_viewed": _similar_to_viewed(viewed_car_ids, limit, all_cars),
        "from_favorites": _from_favorites(favorite_car_ids, limit, all_cars),
    }


def _suggested_for_you(budget_max, preferred_brand, exclude_ids, limit, all_cars):
    results = []
    for car in all_cars:
        if car["id"] in exclude_ids:
            continue
        score = 0
        if budget_max and car["price_syp"] <= budget_max:
            score += 3
        if preferred_brand and preferred_brand.lower() in car["brand"].lower():
            score += 2
        score += car["favorite_count"] / 100
        if car["days_listed"] <= 7:
            score += 1
        results.append({**car, "_score": score})
    results.sort(key=lambda x: -x["_score"])
    return _format(results[:limit], "suggested_for_you")


def _best_deals(limit, all_cars):
    deals = []
    for car in all_cars:
        avg = car["average_model_price"]
        if avg <= 0:
            continue
        diff_pct = ((car["price_syp"] - avg) / avg) * 100
        if diff_pct <= -5:
            deals.append({**car, "_discount": abs(diff_pct)})
    deals.sort(key=lambda x: -x["_discount"])
    return _format(deals[:limit], "best_deal")


def _similar_to_viewed(viewed_ids, limit, all_cars):
    if not viewed_ids:
        sorted_cars = sorted(all_cars, key=lambda x: -x["clicks"])
        return _format(sorted_cars[:limit], "most_viewed")

    viewed = [c for c in all_cars if c["id"] in viewed_ids]
    if not viewed:
        return []

    brands = set(c["brand"] for c in viewed)
    body_types = set(c["body_type"] for c in viewed)

    similar = [
        car for car in all_cars
        if car["id"] not in viewed_ids
        and (car["brand"] in brands or car["body_type"] in body_types)
    ]
    similar.sort(key=lambda x: -x["favorite_count"])
    return _format(similar[:limit], "similar_to_viewed")


def _from_favorites(favorite_ids, limit, all_cars):
    if not favorite_ids:
        sorted_cars = sorted(all_cars, key=lambda x: -x["favorite_count"])
        return _format(sorted_cars[:limit], "top_favorited")

    favs = [c for c in all_cars if c["id"] in favorite_ids]
    if not favs:
        return []

    brands = set(c["brand"] for c in favs)
    body_types = set(c["body_type"] for c in favs)
    avg_price = sum(c["price_syp"] for c in favs) / len(favs)

    results = [
        car for car in all_cars
        if car["id"] not in favorite_ids
        and (car["brand"] in brands or car["body_type"] in body_types)
        and car["price_syp"] <= avg_price * 1.2
    ]
    results.sort(key=lambda x: -x["favorite_count"])
    return _format(results[:limit], "from_favorites")


def _format(cars: list, rec_type: str) -> list:
    reasons = {
        "suggested_for_you": "يناسب ميزانيتك وتفضيلاتك السابقة",
        "best_deal": "أقل من متوسط السوق",
        "similar_to_viewed": "مشابه لسيارات شفتها مؤخراً",
        "from_favorites": "بناءً على سيارات حفظتها",
        "most_viewed": "الأكثر مشاهدة على المنصة",
        "top_favorited": "الأكثر حفظاً من المستخدمين",
    }
    output = []
    for car in cars:
        analysis = get_market_analysis(car)
        output.append({
            "id": car["id"],
            "title": car["title"],
            "year": car["year"],
            "price_syp": car["price_syp"],
            "price_usd": car["price_usd"],
            "mileage": car["mileage"],
            "recommendation_type": rec_type,
            "reason": reasons.get(rec_type, "موصى به"),
            "price_verdict": analysis["verdict"],
            "negotiation_tip": analysis["negotiation_tip"],
        })
    return output
