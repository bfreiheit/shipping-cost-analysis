import pandas as pd
from shipping_cost_analysis.models import state_mapping

def missing_data(df: pd.DataFrame) -> pd.DataFrame:
    total = df.isnull().sum().sort_values(ascending=False)
    total = total[total.apply(lambda x: x > 0)]

    Percentage = round((df.isnull().sum() / df.isnull().count() * 100), 2).sort_values(
        ascending=False
    )
    Percentage = Percentage[Percentage.apply(lambda x: x > 0.00)]
    return pd.concat([total, Percentage], axis=1, keys=["Total", "Percentage Missing"])

def normalize_state(val):
    valid_state_codes = set(state_mapping.us_states.values())
    if not isinstance(val, str):
        return None
    val = val.strip().upper()
    if val in valid_state_codes:
        return val  # already a valid code
    return state_mapping.us_states.get(val, None)  # map from name


def impute_missing_sales_and_quantity(df, price_map):
    mask = df["quantity"].isna() & df["sales"].isna() & df["stock_code"].notna()
    df.loc[mask, "quantity"] = 1
    df.loc[mask, "sales"] = df.loc[mask, "stock_code"].map(price_map)
    return df
