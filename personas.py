from typing import TypedDict
import random


class Persona(TypedDict):
    age: int
    nationality: str
    gender: str


# TODO: we should get this from a nationality database of some kind
NATIONALITIES = (
    "Indian",
    "Brazilian",
    "American",
    "British",
    "German",
    "Japanese",
    "Korean",
    "Chinese",
    "Italian",
)


def get_persona() -> Persona:
    age = random.randint(16, 60)
    nationality = random.choice(NATIONALITIES)
    gender = random.choice(("male", "female"))

    return {"age": age, "nationality": nationality, "gender": gender}
