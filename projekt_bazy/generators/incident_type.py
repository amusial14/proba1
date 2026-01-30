import pandas as pd

def generate_incident_types(types_list, risk_list) -> pd.DataFrame:
    data = {
        "name": types_list,
        "risk_level": risk_list
    }

    df_incident_type = pd.DataFrame(data)
    return df_incident_type