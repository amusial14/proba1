import pandas as pd
import random


def generate_insurance(insurance_list, amount_list) -> pd.DataFrame:

    df = pd.DataFrame({
        "name": insurance_list,
        "coverage_amount": amount_list
    })
    return df

def generate_guest_insurance(baza, id_child_insurances, id_adult_insurances, id_senior_insurances) -> pd.DataFrame:
    guests = pd.read_sql("SELECT guest_id, birth_date FROM guests", con=baza.con)
    insurances = []
    today_year = pd.Timestamp.today().normalize().year
    for row in guests["birth_date"]:
        birth_year = pd.to_datetime(row).year
        age = today_year - birth_year
        if age <= 18:
            insurances.append(random.choice(id_child_insurances))
        elif age <= 65:
            insurances.append(random.choice(id_adult_insurances))
        else:
            insurances.append(random.choice(id_senior_insurances))
        
    guests["insurance"] = insurances

    df = pd.DataFrame({
        "guest_id": guests["guest_id"],
        "insurance_id": guests["insurance"]
    })

    return df


