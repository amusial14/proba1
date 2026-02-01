import pandas as pd
import random

def generate_inspection_date(build_date):
    build_date = pd.to_datetime(build_date)
    end_date = pd.Timestamp.today()

    between_days = (end_date-build_date).days

    random_days = random.randint(0, between_days)
    return build_date + pd.Timedelta(days=random_days)

def generate_inspections(baza, num, possible_results):
    attractions_df = pd.read_sql("select attraction_id, built_date from attractions", con=baza.con)

    pairs = attractions_df[["attraction_id", "built_date"]].to_records(index=False).tolist()

    attraction_ids = []
    inspection_dates = []
    results = []


    for i in range(num):
        inspected_pair = random.choice(pairs)
        attraction_ids.append(inspected_pair[0])

        inspection_date = generate_inspection_date(inspected_pair[1])

        inspection_dates.append(inspection_date)

        results.append(random.choice(possible_results))

    df = pd.DataFrame({
        "attraction_id": attraction_ids,
        "inspection_date": inspection_dates,
        "result": results
    })

    return df