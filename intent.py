import re
from typing import Optional


def detect_intent(message: str) -> str:
    patterns = {
        "search_cars": [
            "بدي", "دوّرلي", "دورلي", "بحث", "لاقيلي", "ابحث",
            "عندكم", "متوفر", "فيه", "أريد", "اريد", "بحتاج"
        ],
        "compare_cars": [
            "قارن", "مقارنة", "الفرق", "أفضل بين", "أحسن", "يفضل", "الأحسن"
        ],
        "price_opinion": [
            "سعره", "غالي", "رخيص", "يستاهل", "منطقي", "السعر", "مناسب", "كتير"
        ],
        "negotiate_advice": [
            "تفاوض", "أقلو", "أول عرض", "كم أحط", "يقبل", "ساوم", "نزلو"
        ],
        "car_details": [
            "مواصفات", "مشاكل", "موثوق", "استهلاك", "محرك", "معلومات", "تفاصيل", "شو بتعرف عن"
        ],
        "not_available": [
            "مو موجود", "ما عندكم", "مش متوفر", "ما في"
        ],
        "out_of_scope": [
            "مطعم", "طقس", "رياضة", "أخبار", "سياسة", "طبخ", "سفر", "فندق"
        ],
    }
    for intent, words in patterns.items():
        if any(word in message for word in words):
            return intent
    return "general"


def extract_entities(message: str) -> dict:
    return {
        "budget": _extract_budget(message),
        "brand": _extract_brand(message),
        "body_type": _extract_body_type(message),
        "location": _extract_location(message),
        "year": _extract_year(message),
        "fuel_type": _extract_fuel_type(message),
        "seats": _extract_seats(message),
    }


def _extract_budget(message: str) -> dict:
    between = re.search(r'بين\s*(\d+)\s*و\s*(\d+)\s*مليون', message)
    if between:
        return {"min": int(between.group(1)) * 1_000_000, "max": int(between.group(2)) * 1_000_000}

    less = re.search(r'(أقل من|تحت)\s*(\d+)\s*مليون', message)
    if less:
        return {"min": 0, "max": int(less.group(2)) * 1_000_000}

    more = re.search(r'(أكتر من|فوق)\s*(\d+)\s*مليون', message)
    if more:
        return {"min": int(more.group(2)) * 1_000_000, "max": 999_999_999}

    around = re.search(r'(\d+)\s*مليون', message)
    if around:
        amount = int(around.group(1)) * 1_000_000
        return {"min": int(amount * 0.85), "max": int(amount * 1.15)}

    return {"min": 0, "max": 999_999_999}


def _extract_brand(message: str) -> Optional[str]:
    brands = {
        "toyota": ["تويوتا", "toyota"],
        "kia": ["كيا", "kia"],
        "honda": ["هوندا", "honda"],
        "hyundai": ["هيونداي", "hyundai"],
        "nissan": ["نيسان", "nissan"],
        "mazda": ["مازدا", "mazda"],
        "mitsubishi": ["ميتسوبيشي", "mitsubishi"],
        "chevrolet": ["شيفروليه", "chevrolet"],
    }
    msg = message.lower()
    for brand, keywords in brands.items():
        if any(k in msg for k in keywords):
            return brand
    return None


def _extract_body_type(message: str) -> Optional[str]:
    if any(w in message for w in ["SUV", "سيارة دفع", "رباعي", "جيب", "دفع رباعي", "عالية"]):
        return "SUV"
    if any(w in message for w in ["سيدان", "sedan", "عادية"]):
        return "Sedan"
    if any(w in message for w in ["هاتشباك", "hatchback"]):
        return "Hatchback"
    if any(w in message for w in ["كوبيه", "coupe"]):
        return "Coupe"
    return None


def _extract_location(message: str) -> Optional[str]:
    locations = ["دمشق", "حلب", "حمص", "اللاذقية", "حماة", "طرطوس", "دير الزور", "درعا", "ادلب"]
    for loc in locations:
        if loc in message:
            return loc
    return None


def _extract_year(message: str) -> Optional[int]:
    match = re.search(r'(20\d{2})', message)
    if match:
        return int(match.group(1))
    if "أحدث" in message or "جديد" in message:
        return 2022
    return None


def _extract_fuel_type(message: str) -> Optional[str]:
    if any(w in message for w in ["هايبرد", "hybrid"]):
        return "Hybrid"
    if any(w in message for w in ["ديزل", "مازوت"]):
        return "Diesel"
    if any(w in message for w in ["كهربائي", "electric"]):
        return "Electric"
    if any(w in message for w in ["بنزين"]):
        return "Gas"
    return None


def _extract_seats(message: str) -> Optional[int]:
    match = re.search(r'(\d)\s*مقاعد', message)
    if match:
        return int(match.group(1))
    if "عائلية" in message or "عيلة" in message:
        return 7
    return None
