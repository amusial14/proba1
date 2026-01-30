import pandas as pd
import random



def random_work_datetime(dates, open_hour, closure_hour):
    d = random.choice(dates)

    seconds = random.randint(9*3600, 18*3600 - 1)

    return d + pd.Timedelta(seconds=seconds)

def generate_payment_ticket(baza, max_payments_per_guest, weights_for_payments, guest_num) -> pd.DataFrame:
    payments = []
    tickets = []
    df_prices = pd.read_sql("SELECT * FROM prices", con=baza.con)
    all_tickets = df_prices["ticket_id"].tolist()
    for i in range(1,guest_num+1):
        k = random.choices(range(1, max_payments_per_guest), weights=weights_for_payments, k=1)[0]


        chosen = random.sample(all_tickets, k)

        for ticket_id in chosen:
            payments.append(i)
            tickets.append(ticket_id)

    dataframe_payment_ticket = pd.DataFrame({
        "payment_id": payments,
        "ticket_id": tickets
    })

    return dataframe_payment_ticket

def generate_payments(baza, payments_tickets, open_hour, closure_hour) -> pd.DataFrame:
    payment_ids = payments_tickets["payment_id"].dropna().unique().tolist()
    dates = []
    amounts = []
    guests_df = pd.read_sql("SELECT * FROM guests", con=baza.con)
    guests = guests_df.loc[guests_df["birth_date"] <= pd.Timestamp('2010-01-01').date(), "guest_id"].to_list()      #bierzemy starszych od 15
    while len(guests) < len(payment_ids):
        shuffled = random.sample(guests, len(guests))
        guests= guests + shuffled
    guests = guests[:len(payment_ids)]
    lst = payments_tickets.groupby("payment_id")["ticket_id"].apply(list)
    prices_df = pd.read_sql("SELECT * FROM prices", con=baza.con)
    price_dict = prices_df.set_index("ticket_id")["amount"].to_dict()
    dates_to_gen = pd.date_range("2026-01-01", "2026-01-31")        #mamy info za ostatni miesiac
    for ls in lst:
        total = 0
        for ticket in ls:
            total += price_dict[ticket]
        amounts.append(total)
        date = random_work_datetime(dates_to_gen, open_hour, closure_hour)
        dates.append(date)
    dataframe_payments = pd.DataFrame({
        "payment_date": dates,
        "amount": amounts,
        "guest_id": guests
    })

    return dataframe_payments