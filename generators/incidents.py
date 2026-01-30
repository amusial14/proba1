import pandas as pd
import random

def generate_incidents(baza, num) -> pd.DataFrame:
    type_ids = []
    dates = []
    guests = []
    attractions = []
    types_df = pd.read_sql("SELECT incident_type_id FROM incident_type", con=baza.con)["incident_type_id"].tolist()
    guest_attraction_df = pd.read_sql("""
                                        SELECT DISTINCT
                                            g.guest_id,
                                            a.attraction_id,
                                            p.payment_date
                                        FROM guests g
                                        JOIN payments p        ON p.guest_id = g.guest_id
                                        JOIN payment_ticket pt ON pt.payment_id = p.payment_id
                                        JOIN prices pr         ON pr.ticket_id = pt.ticket_id
                                        JOIN attractions a     ON a.attraction_id = pr.attraction_id
                                        """, con=baza.con)
    for i in range(num):
        type_ids.append(random.choice(types_df))
        gu_at_da = guest_attraction_df.sample(n=1).iloc[0]
        guests.append(gu_at_da["guest_id"])
        dates.append(gu_at_da["payment_date"].date())
        attractions.append(gu_at_da["attraction_id"])

    df = pd.DataFrame({
        "incident_type_id": type_ids,
        "guest_id": guests,
        "attraction_id": attractions,
        "incident_date": dates,
        "description": [' ' for i in range(num)]
    })

    return df