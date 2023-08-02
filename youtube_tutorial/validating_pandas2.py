# USING PANDAS SCHEMA FILE FOR VALIDATING NEW DATA

from pathlib import Path
from typing import Union 

import pandas as pd 
import pandera as pa 

from altered_schema import schema 

# USE "check_output" DECORATOR TO VALIDATE IF NEW DATA FITS SCHEMA MODEL
@pa.check_output(schema, lazy=True)
def read_csv(path: Union[Path, str]) -> pd.DataFrame:
    return pd.read_csv(path)

def main() -> None:
    dataset_path = Path().absolute() / "datasets"
    df = read_csv(dataset_path / "data.csv")

    df_inferred_schema = pa.infer_schema(df)

    # write out inferred schema to a python file
    with open("inferred_schema.py", "w") as file:
        file.write(df_inferred_schema.to_script())
    
    try: 
        schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as err:
        print(err)
