from enum import IntEnum


class BodyType(IntEnum):
    Sedan = 0
    Hatchback = 1
    Coupe = 2
    SUV = 3
    Bus = 4
    MiniTruck = 5


class CarCondition(IntEnum):
    Used = 0
    New = 1


class CarReactionType(IntEnum):
    Like = 0
    Dislike = 1


class CarStatus(IntEnum):
    Draft = 0
    PendingReview = 1
    Available = 2
    NotAvailable = 3
    Rejected = 4
    Sold = 5
    Archived = 6


class FuelType(IntEnum):
    Gas = 0
    Diesel = 1
    Electric = 2
    Hybrid = 3


class GearType(IntEnum):
    Auto = 0
    Manual = 1
