import pandas as pd
import random
from faker import Faker


def generate_hire_date(build_date, number_of_month):    #number of months is made to generate hire dates truthfully, workers not to be hired for example yesterday.
    # so this number of months influences maximal generated hire date
    build_date = pd.to_datetime(build_date)
    end_date = pd.Timestamp.today() - pd.DateOffset(months=number_of_month)

    between_days = (end_date-build_date).days
    if between_days <= 0:
        return build_date
    else:
        random_days = random.randint(0, between_days)
        return build_date + pd.Timedelta(days=random_days)

def generate_employees(baza, min_salary, max_salary, number_of_months, workers_per_attration=1) -> pd.DataFrame:
    attractions_df = pd.read_sql("select * from attractions", con=baza.con)
    
    pairs = attractions_df[["attraction_id", "built_date"]].to_records(index=False).tolist()
    names = []
    last_names = []
    position = []
    salaries = []
    hire_dates = []
    fake = Faker("pl_PL")
    attraction_ids = []
    for pair in pairs:
        for i in range(workers_per_attration):
            names.append(fake.first_name())
            last_names.append(fake.last_name())
            position.append("Ride operator")
            salaries.append(random.randint(min_salary, max_salary))
            hire_dates.append(generate_hire_date(pair[1], number_of_months))
            attraction_ids.append(pair[0])
    
    df = pd.DataFrame({
        "first_name": names,
        "last_name": last_names,
        "position": position,
        "salary": salaries,
        "hire_date": hire_dates,
        "attraction_id": attraction_ids
    })

    return df