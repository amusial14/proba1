import random
import pandas as pd


def generate_prices(attractions_num, min_price=25, max_price=120) -> pd.DataFrame:
    prices = []
    attractions = []

    for i in range(attractions_num):

        # FIX: max_price jest osiągalne
        price_real = random.randint(min_price, max_price)

        # FIX: VR zawsze droższe
        price_vr = random.randint(int(price_real * 1.3), int(price_real * 1.8))

        # FIX: zniżka = dokładnie 50%
        price_real_discounted = price_real * 0.5
        price_vr_discounted = price_vr * 0.5

        # FIX: realistyczne końcówki cen
        price_real += random.choice([0, 0.99])
        price_real_discounted += random.choice([0, 0.99])
        price_vr += random.choice([0, 0.99])
        price_vr_discounted += random.choice([0, 0.99])

        prices.extend([
            round(price_real, 2),
            round(price_real_discounted, 2),
            round(price_vr, 2),
            round(price_vr_discounted, 2)
        ])

        # real = 2*i+1, vr = 2*i+2
        attractions.extend([
            i * 2 + 1,
            i * 2 + 1,
            i * 2 + 2,
            i * 2 + 2
        ])

    dataframe_prices = pd.DataFrame({
        "amount": prices,
        "attraction_id": attractions
    })

    return dataframe_prices
