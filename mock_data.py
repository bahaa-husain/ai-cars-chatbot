from typing import Optional

MOCK_CARS = [
    {
        "id": "1",
        "name": "تويوتا كامري",
        "brand": "toyota",
        "year": 2023,
        "price": 42000000,
        "mileage": 15000,
        "location": "دمشق",
        "fuel_type": "بنزين",
        "body_type": "sedan",
        "seats": 5,
        "color": "أبيض",
        "views": 320,
        "favorites": 45,
        "days_listed": 12,
        "market_avg_price": 44000000,
        "image": "camry_2023.jpg",
        "description": "سيارة بحالة ممتازة، صيانة دورية، مالك واحد"
    },
    {
        "id": "2",
        "name": "هوندا أكورد",
        "brand": "honda",
        "year": 2022,
        "price": 38000000,
        "mileage": 28000,
        "location": "حلب",
        "fuel_type": "بنزين",
        "body_type": "sedan",
        "seats": 5,
        "color": "رمادي",
        "views": 210,
        "favorites": 30,
        "days_listed": 35,
        "market_avg_price": 41000000,
        "image": "accord_2022.jpg",
        "description": "سيارة نظيفة جداً، كاملة المواصفات"
    },
    {
        "id": "3",
        "name": "كيا سبورتاج",
        "brand": "kia",
        "year": 2023,
        "price": 58000000,
        "mileage": 8000,
        "location": "دمشق",
        "fuel_type": "بنزين",
        "body_type": "suv",
        "seats": 5,
        "color": "أسود",
        "views": 540,
        "favorites": 89,
        "days_listed": 5,
        "market_avg_price": 60000000,
        "image": "sportage_2023.jpg",
        "description": "شبه جديدة، ضمان سنة، فل أوبشن"
    },
    {
        "id": "4",
        "name": "نيسان سنترا",
        "brand": "nissan",
        "year": 2022,
        "price": 32000000,
        "mileage": 35000,
        "location": "حمص",
        "fuel_type": "بنزين",
        "body_type": "sedan",
        "seats": 5,
        "color": "أزرق",
        "views": 180,
        "favorites": 22,
        "days_listed": 20,
        "market_avg_price": 33000000,
        "image": "sentra_2022.jpg",
        "description": "اقتصادية جداً بالوقود، مناسبة للمدينة"
    },
    {
        "id": "5",
        "name": "هيونداي توسان",
        "brand": "hyundai",
        "year": 2022,
        "price": 62000000,
        "mileage": 22000,
        "location": "اللاذقية",
        "fuel_type": "بنزين",
        "body_type": "suv",
        "seats": 5,
        "color": "أبيض",
        "views": 390,
        "favorites": 67,
        "days_listed": 18,
        "market_avg_price": 64000000,
        "image": "tucson_2022.jpg",
        "description": "SUV عائلي مريح، صيانة وكالة"
    },
    {
        "id": "6",
        "name": "تويوتا كورولا",
        "brand": "toyota",
        "year": 2021,
        "price": 28000000,
        "mileage": 45000,
        "location": "دمشق",
        "fuel_type": "بنزين",
        "body_type": "sedan",
        "seats": 5,
        "color": "فضي",
        "views": 450,
        "favorites": 78,
        "days_listed": 8,
        "market_avg_price": 29000000,
        "image": "corolla_2021.jpg",
        "description": "موثوقة جداً، استهلاك وقود ممتاز"
    },
    {
        "id": "7",
        "name": "كيا سيراتو",
        "brand": "kia",
        "year": 2023,
        "price": 35000000,
        "mileage": 12000,
        "location": "حلب",
        "fuel_type": "بنزين",
        "body_type": "sedan",
        "seats": 5,
        "color": "أحمر",
        "views": 290,
        "favorites": 41,
        "days_listed": 14,
        "market_avg_price": 36000000,
        "image": "cerato_2023.jpg",
        "description": "شبه جديدة، مواصفات عالية، سعر منافس"
    },
    {
        "id": "8",
        "name": "مازدا 6",
        "brand": "mazda",
        "year": 2022,
        "price": 47000000,
        "mileage": 19000,
        "location": "دمشق",
        "fuel_type": "بنزين",
        "body_type": "sedan",
        "seats": 5,
        "color": "أبيض",
        "views": 260,
        "favorites": 38,
        "days_listed": 25,
        "market_avg_price": 50000000,
        "image": "mazda6_2022.jpg",
        "description": "تصميم راقي، أداء ممتاز، سعر أقل من السوق"
    },
]


def search_mock_cars(
    budget_min: int = 0,
    budget_max: int = 999999999,
    brand: Optional[str] = None,
    body_type: Optional[str] = None,
    location: Optional[str] = None,
    year_min: Optional[int] = None,
    limit: int = 3
) -> list:
    results = []
    for car in MOCK_CARS:
        if not (budget_min <= car["price"] <= budget_max):
            continue
        if brand and brand.lower() not in car["brand"].lower():
            continue
        if body_type and body_type.lower() not in car["body_type"].lower():
            continue
        if location and location not in car["location"]:
            continue
        if year_min and car["year"] < year_min:
            continue
        results.append(car)

    results.sort(key=lambda x: (-x["year"], x["mileage"], -x["favorites"]))
    return results[:limit]


def get_market_analysis(car: dict) -> dict:
    diff = car["price"] - car["market_avg_price"]
    pct = round((diff / car["market_avg_price"]) * 100, 1)

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
