import pandas as pd
import random

def generate_accident_date(build_date):    
    build_date = pd.to_datetime(build_date)
    end_date = pd.Timestamp.today()

    between_days = (end_date-build_date).days

    random_days = random.randint(0, between_days)
    return build_date + pd.Timedelta(days=random_days)

def generate_fix_date(accident_date, max_days_for_fix):
    accident_date = pd.to_datetime(accident_date)
    end_date = accident_date + pd.Timedelta(days=max_days_for_fix)

    end_date = min(pd.Timestamp.today(), end_date)

    between_days = (end_date-accident_date).days

    random_days = random.randint(0, between_days)
    return accident_date + pd.Timedelta(days=random_days)

def generate_malfunctions(baza, possible_malfunctions_per_attraction, minimal_cost, maximal_cost, max_days_for_fix) -> pd.DataFrame:
    attractions_df = pd.read_sql("select attraction_id, built_date from attractions", con=baza.con)
    pairs = attractions_df[["attraction_id", "built_date"]].to_records(index=False).tolist()

    attraction_ids = []
    accident_dates = []
    fix_dates = []
    comments = []
    fix_costs = []

    for pair in pairs:
        for i in range(random.randint(0, possible_malfunctions_per_attraction+1)):
            attraction_ids.append(pair[0])
            accident_date = generate_accident_date(pair[1])
            fix_date = generate_fix_date(accident_date, max_days_for_fix)
            accident_dates.append(accident_date)
            fix_dates.append(fix_date)
            comments.append("")
            fix_costs.append(random.randint(minimal_cost, maximal_cost))

    df = pd.DataFrame({
        "attraction_id": attraction_ids,
        "accident_date": accident_dates,
        "fix_date": fix_dates,
        "comment": comments,
        "fix_cost": fix_costs
    })

    return df

            