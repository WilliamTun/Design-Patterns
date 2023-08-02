# USING PANDERA SCHEMA CLASS BASED ON PYDANTIC FOR VALIDATING NEW DATA

from pathlib import Path
from typing import Union 

import pandas as pd 
import pandera as pa 
from pandera.typing import DataFrame, Series

from altered_schema import schema 

# CLASS
class OutputSchema(pa.SchemaModel):
    """ Schema for data """
    col1: Series[str]
    col2: Series[int]
    col3: Series[int] = pa.Field(ge=1) # specify values greater or equal to 1
    col4: Series[float] = pa.Field(nullable=True)
    col5: Seires[datetime]


# USE "check_types" DECORATOR TO VALIDATE IF NEW DATA FITS SCHEMA MODEL
@pa.check_types(schema, lazy=True)
def read_csv(path: Union[Path, str]) -> DataFrame[OutputSchema]: # NOTE! Dataframe wraps Output Schema object
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
