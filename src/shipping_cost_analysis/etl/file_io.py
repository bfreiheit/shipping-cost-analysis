import os
from typing import Optional

import pandas as pd


def read_or_write_csv(
    file_name: str, df: Optional[pd.DataFrame] = None, 
    file_dir="data",
    to_read: bool = False, 
    file_encoding="utf-8",
    file_sep=","
) -> Optional[pd.DataFrame]:
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, os.path.pardir, file_dir)
    data_path = os.path.join(data_dir, file_name)

    if to_read:
        return pd.read_csv(data_path, encoding=file_encoding, sep=file_sep)        
    else:
        if df is not None:
            df.to_csv(data_path, index=False, encoding=file_encoding, sep=file_sep)
        else:
            raise ValueError("DataFrame must be provided when writing.")