from django.db import models


class BodyType(models.TextChoices):
    Sedan = "Sedan"
    Limousine = "Limousine"
    Pickup = "Pickup"
    Hatchback = "Hatchback"
    StationWagon = "Station wagon"
    Minivan = "Minivan"
    Coupe = "Coupe"
    Convertible = "Convertible"
    Roadster = "Roadster"
    _ = "Out of classification"


class EnginType(models.TextChoices):
    Petrol = "Petrol "
    Diesel = "Diesel"
    Electric = "Electric"
    Hybrid = "Hybrid"


class NumberOfDoor(models.TextChoices):
    TwoDoor = "two-door"
    FourDoor = "four-door"
    FiveDoor = "five-door"


class Color(models.TextChoices):
    Onyx = "Onyx"
    Viking = "Viking"
    Lagoon = "Lagoon"
    Phoenix = "Phoenix"
    Victoria = "Victoria"
    Pomegranate = "Pomegranate"
    Emerald = "Emerald"
    Galaxy = "Galaxy"
    Iris = "Iris"
    Carmen = "Carmen"
    Cedar = "Cedar"
    White = "White"
    Aquamarine = "Aquamarine"
