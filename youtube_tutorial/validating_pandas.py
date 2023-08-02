# CREATING A FRESH NEW PANDAS SCHEMA FILE

from pathlib import Path 
import pandas as pd 
import pandera as pa 

from altered_schema import schema 

def read_csv(path: Path) -> pd.DataFrame:
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
