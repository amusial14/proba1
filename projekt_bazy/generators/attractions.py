import random
import pandas as pd
from .generate_dates import generate_date




def generate_attractions(num, min_year, max_year, adjectives, nouns) -> pd.DataFrame:

    dates = []
    for i in range(num):
        year = random.randint(min_year, max_year)
        date = generate_date(year=year)
        dates.append(date)
        dates.append(date)

    names = []
    for i in range(num):
        random_name = f"{random.choice(adjectives)} {random.choice(nouns)}"
        names.append(random_name)
        names.append(random_name)  

    if_vr = []
    for i in range(num):
        if_vr.append(True)
        if_vr.append(False)

    dataframe_attractions = pd.DataFrame({
        "attraction_name": names,
        "vr": if_vr,
        "built_date": dates
        
        })

    return dataframe_attractions

