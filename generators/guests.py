from datetime import date
import random
import pandas as pd
from faker import Faker
from .generate_dates import generate_date

def generate_distribution() -> list:
    weights = []
    for age in range(3,17):
        weights.append(0.5/(17 - 3))
    for age in range(17, 28):
        weights.append(0.1/(28 - 17))
    for age in range(28, 40):
        weights.append(0.3/(40 - 28))
    for age in range(40, 70):
        weights.append(0.1/(70 - 40))
    return weights
def generate_age():
    weights = generate_distribution()
    ages = list(range(3, 70))
    age = random.choices(ages, weights=weights)[0]
    return age


def age_to_date(age) -> date:
    today = date.today()
    birth_year = today.year - age
    birth = generate_date(year=birth_year)
    return birth

def generate_guests(num):
    birth_dates = []
    fake = Faker("pl_PL")
    for _ in range(num):
        age = generate_age()
        birth_date = age_to_date(age)
        birth_dates.append(birth_date)

    guest_dataframe = pd.DataFrame({
        "first_name":   [fake.first_name() for _ in range(num)],
        "last_name":    [fake.last_name() for _ in range(num)],
        "birth_date":   birth_dates
    }
    )
    return guest_dataframe




# print(generate_guests(1000))


