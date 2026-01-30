import pandas as pd
import random

def generate_costs(baza, min_amount, max_amount) -> pd.DataFrame:
    attractions = pd.read_sql("select attraction_id from attractions", con = baza.con)["attraction_id"].tolist()

    cost_types = []
    amounts = []
    how_often_list = []

    for attraction_id in attractions:
        cost_types.append('monthly cost')
        amounts.append(random.randint(min_amount, max_amount))
        how_often_list.append("once_per_month")

    df = pd.DataFrame({
        "cost_type": cost_types,
        "amount": amounts,
        "how_often": how_often_list,
        "attraction_id": attractions
    })

    return df