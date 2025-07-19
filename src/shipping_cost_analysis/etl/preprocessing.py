import pandas as pd


def missing_data(df: pd.DataFrame) -> pd.DataFrame:
    total = df.isnull().sum().sort_values(ascending=False)
    total = total[total.apply(lambda x: x > 0)]

    Percentage = round((df.isnull().sum() / df.isnull().count() * 100), 2).sort_values(
        ascending=False
    )
    Percentage = Percentage[Percentage.apply(lambda x: x > 0.00)]
    return pd.concat([total, Percentage], axis=1, keys=["Total", "Percentage Missing"])
