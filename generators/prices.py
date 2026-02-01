import random
import pandas as pd


def generate_prices(attractions_num, min_price=10, max_price=50) -> pd.DataFrame:
    prices = []
    attractions = []
    for i in range(attractions_num):
        price_real = random.choice(range(min_price, max_price))
        price_real_discounted = price_real/2
        price_vr = random.choice(range(min_price, price_real+1))
        price_vr_discounted = price_vr/2
        price_real = price_real +  random.choice([0, 0.49, 0.99])
        price_real_discounted = price_real_discounted +  random.choice([0, 0.49, 0.99])
        price_vr = price_vr +  random.choice([0, 0.49, 0.99])
        price_vr_discounted = price_vr_discounted +  random.choice([0, 0.49, 0.99])
        prices.append(price_real)
        prices.append(price_real_discounted)
        prices.append(price_vr)
        prices.append(price_vr_discounted)
        attractions.append(i*2 + 1)
        attractions.append(i*2 + 1)
        attractions.append(i*2 + 2)
        attractions.append(i*2 + 2)


    dataframe_prices = pd.DataFrame({
        "amount": prices,
        "attraction_id": attractions

    })

    return dataframe_prices
