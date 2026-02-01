import pandas as pd
import random


def random_work_datetime(dates, open_hour, closure_hour):
    d = random.choice(dates)

    # FIX: używamy open_hour i closure_hour zamiast stałych godzin
    seconds = random.randint(open_hour * 3600, closure_hour * 3600 - 1)

    return d + pd.Timedelta(seconds=seconds)


def generate_payment_ticket(baza, max_payments_per_guest, weights_for_payments, guest_num) -> pd.DataFrame:
    payments = []
    tickets = []

    df_prices = pd.read_sql("SELECT * FROM prices", con=baza.con)
    all_tickets = df_prices["ticket_id"].tolist()

    for guest_id in range(1, guest_num + 1):

        # FIX: max_payments_per_guest MUSI być osiągalne
        k = random.choices(
            range(1, max_payments_per_guest + 1),
            weights=weights_for_payments,
            k=1
        )[0]

        # FIX: można kupić ten sam bilet więcej niż raz
        chosen_tickets = random.choices(all_tickets, k=k)

        for ticket_id in chosen_tickets:
            payments.append(guest_id)
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

    # FIX: każdy gość może płacić (nie tylko 15+)
    guests_df = pd.read_sql("SELECT * FROM guests", con=baza.con)
    guests = guests_df["guest_id"].to_list()

    # zabezpieczenie gdy płatności > liczba gości
    while len(guests) < len(payment_ids):
        guests += random.sample(guests, len(guests))

    guests = guests[:len(payment_ids)]

    grouped_tickets = payments_tickets.groupby("payment_id")["ticket_id"].apply(list)

    prices_df = pd.read_sql("SELECT * FROM prices", con=baza.con)
    price_dict = prices_df.set_index("ticket_id")["amount"].to_dict()

    dates_to_gen = pd.date_range("2025-01-01", "2026-01-01")

    for tickets in grouped_tickets:
        total_amount = sum(price_dict[ticket] for ticket in tickets)
        amounts.append(total_amount)

        payment_date = random_work_datetime(dates_to_gen, open_hour, closure_hour)
        dates.append(payment_date)

    dataframe_payments = pd.DataFrame({
        "payment_date": dates,
        "amount": amounts,
        "guest_id": guests
    })

    return dataframe_payments
