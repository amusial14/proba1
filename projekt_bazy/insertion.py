from generators.guests import generate_guests
from generators.attractions import generate_attractions
from generators.prices import generate_prices
from generators.payments import generate_payments, generate_payment_ticket
from generators.incident_type import generate_incident_types
from generators.incidents import generate_incidents
from generators.insuranse import generate_guest_insurance, generate_insurance
from generators.employees import generate_employees
from generators.costs import generate_costs
from generators.malfunctions import generate_malfunctions
from generators.inspections import generate_inspections

from config import config


def table_row_count(cursor, table_name) -> int:
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

import numpy as np

def _py(x):
    if x is None:
        return None
    if isinstance(x, np.generic):        # sometimes np data_types are not understandable for sql
        return x.item()
    return x

def df_to_sql(baza, df, table: str, columns: list[str], batch_size: int = 100):
    df = df.where(df.notna(), None)  
    rows = [tuple(map(_py, row)) for row in df.to_numpy()]
    placeholders = ", ".join(["%s"] * len(columns))
    sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"

    for i in range(0, len(rows), batch_size):
        baza.cursor.executemany(sql, rows[i:i+batch_size])
    baza.con.commit()

def insert_guests(baza, num):
    if table_row_count(baza.cursor, "guests") > 0:
        print("Guests table already has data. Skipping insertion.")
        return
    
    guests = generate_guests(num)
    
    df_to_sql(
        baza,
        guests,
        table="guests",
        columns=["first_name", "last_name", "birth_date"]
    )

def insert_attractions(baza, num, min_year, max_year, adjectives, nouns):
    if table_row_count(baza.cursor, "attractions") > 0:
        print("Attractions table already has data. Skipping insertion.")
        return
    
    attractions = generate_attractions(num, min_year, max_year, adjectives, nouns)
    
    df_to_sql(
        baza,
        attractions,
        table="attractions",
        columns=["attraction_name", "vr", "built_date"],
        batch_size=50
    )

def insert_prices(baza):
    if table_row_count(baza.cursor, "prices") > 0:
        print("Prices table already has data. Skipping insertion.")
        return
    
    prices = generate_prices(25)

    df_to_sql(
        baza,
        prices,
        table="prices",
        columns=["amount", "attraction_id"],
        batch_size=100
    )

def insert_payments(baza, max_payments_per_guest, weights_for_payments, guest_num, open_hour, closure_hour):
    
    
    payments_tickets = generate_payment_ticket(baza, max_payments_per_guest, weights_for_payments, guest_num)
    payments = generate_payments(baza, payments_tickets, open_hour, closure_hour)

    if table_row_count(baza.cursor, "payments") > 0:
        print("Payments table already has data. Skipping insertion.")
    else:
        df_to_sql(
            baza,
            payments,
            table="payments",
            columns=["payment_date", "amount", "guest_id"],
            batch_size=len(payments)
        
        )

    if table_row_count(baza.cursor, "payment_ticket") > 0:
        print("Payments_tickets table already has data. Skipping insertion.")
    else:
        df_to_sql(
            baza,
            payments_tickets,
            table="payment_ticket",
            columns=["payment_id", "ticket_id"],
            batch_size=len(payments)
        )


def insert_incident_types(baza, types_list, risk_list):
    if table_row_count(baza.cursor, "incident_type") > 0:
        print("Incident_type table already has data. Skipping insertion.")
        return
    
    incident_types = generate_incident_types(types_list, risk_list)
    
    df_to_sql(
        baza,
        incident_types,
        table="incident_type",
        columns=["name", "risk_level"],
        batch_size=100
    )

def insert_incidents(baza, num):
    if table_row_count(baza.cursor, "incidents") > 0:
        print("Incidents table already has data. Skipping insertion.")
        return
    
    incidents = generate_incidents(baza, num)

    df_to_sql(
        baza, 
        incidents,
        table="incidents",
        columns=["incident_type_id", "guest_id", "attraction_id", "incident_date", "description"],
        batch_size=num
    )

def insert_insurance(baza, insurance_list, amount_list, id_child_insurances,  id_adult_insurances, id_senior_insurances):

    insurance = generate_insurance(insurance_list, amount_list)
    guest_insurance = generate_guest_insurance(baza, id_child_insurances, id_adult_insurances, id_senior_insurances)


    if table_row_count(baza.cursor, "insurance") > 0:
        print("Insurance table already has data. Skipping insertion.")
    else:
        df_to_sql(baza,
                  insurance,
                  "insurance",
                  columns= ["name", "coverage_amount"])
        
    if table_row_count(baza.cursor, "guest_insurance") > 0:
        print("Guest_insurance table already has data. Skipping insertion.")
    else:
        df_to_sql(baza,
                  guest_insurance,
                  "guest_insurance",
                  columns=["guest_id", "insurance_id"])
    

def insert_employees(baza, min_salary, max_salary, number_of_months, workers_num):
    if table_row_count(baza.cursor, "employees") > 0:
        print("Employees table already has data. Skipping insertion")
        return
    
    employees = generate_employees(baza, min_salary, max_salary, number_of_months, workers_per_attration=workers_num)

    df_to_sql(baza,
              employees,
              "employees",
              ["first_name", "last_name", "position", "salary", "hire_date", "attraction_id"])
    
def insert_costs(baza, min_amount, max_amount):
    if table_row_count(baza.cursor, "costs") > 0:
        print("Costs table already has data. Skipping insertion")
        return
    
    costs = generate_costs(baza, min_amount, max_amount)

    df_to_sql(baza,
              costs,
              "costs",
              ["cost_type", "amount", "how_often", "attraction_id"])

def insert_malfunctions(baza, possible_malfunctions_per_attraction, min_amount, max_amount, max_days_to_fix):
    if table_row_count(baza.cursor, "malfunctions") > 0:
        print("Malfunctions table already has data. Skipping insertion")
        return
    
    malfunctions = generate_malfunctions(baza, possible_malfunctions_per_attraction, min_amount, max_amount, max_days_to_fix)

    df_to_sql(baza,
              malfunctions,
              "malfunctions",
              ["attraction_id", "accident_date", "fix_date", "comment", "fix_cost"])
    
def insert_inspections(baza, num, possible_results):
    if table_row_count(baza.cursor, "inspections") > 0:
        print("Inspections table already has data. Skipping insertion")
        return
    
    inspections = generate_inspections(baza, num, possible_results)

    df_to_sql(baza,
              inspections,
              "inspections",
              ["attraction_id", "inspection_date", "result"])

def insert_data(baza, config=config):
    insert_guests(baza, config.guest_num)
    insert_attractions(baza, config.unique_attractions_num, config.min_attraction_built_year, config.max_attraction_built_year, config.adjectives_for_attractions_names, config.nouns_for_attractions_names)
    insert_prices(baza)
    insert_payments(baza, config.max_payments_per_guest, config.weights_for_payments, config.guest_num, config.open_hour, config.closure_hour)
    insert_incident_types(baza, config.names_for_incident_types, config.risks_of_incident_types)
    insert_incidents(baza, config.incidents_num)
    insert_insurance(baza, config.insurance_names, config.insurance_amounts, config.children_id_list, config.adult_id_list, config.senior_id_list)
    insert_employees(baza, config.min_salary, config.max_salary, config.number_of_months, config.workers_num_per_attraction)
    insert_costs(baza, config.min_month_costs, config.max_month_costs)
    insert_malfunctions(baza, config.possible_malfunctions_per_attraction, config.min_fix_cost, config.max_fix_cost, config.max_days_to_fix)
    insert_inspections(baza, config.inspections_num, config.possible_inspection_results)