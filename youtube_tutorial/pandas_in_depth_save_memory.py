# Concept 1: Conversion of pandas dataframe types
import pandas as pd 
pandas_df = pd.read_csv("x.csv")
mapping_type_conversion = {
    "col1": "string",
    "col2": "string",
    "col3": "int",
    "col4": "boolean",
    "col5": "datetime"
}
pandas_df = pandas_df.astype(mapping_type_conversion)


# Concept 2: LOG how much memory is being used by pandas df
def calculate_memory_usage(df_input: pd.DataFrame) -> pd.Series:
    ''' Returns real memory usage of a pandas df object '''
    memory_usage = df_input.memory_usage(deep=True)
    print("--- memory consumption ---")
    print(f"{memory_usage:4}")
    return memory_usage

calculate_memory_usage(pandas_df)


# Concept 3: If we have a LARGE dataset
#            where columns are STRINGS
#            it is inefficient! 
#            PROBLEM: strings require lots of memory
#                     many rows of strings requires lots and lots of memory
#            SOLUTION: convert columns to "categorical" datatype

def convert_to_categorical (
    df_to_convert: pd.DataFrame,
    columns: [list[str]]
) -> pd.DataFrame:
    ''' Converts specified columns off dataframe to categoricals '''
    df_out = df_to_convert.copy()
    for column in columns: 
        df_out[column] = df_out[column].astype("category")
    return df_out

pandas_df2 = convert_to_categorical(pandas_df, ["col1", "col2"])


# Concept 4: Calculate memory consumption before and after conversion from string type to categorical
def calculate_percentage_difference(initial: pd.Series, final: pd.Series) -> pd.Series:
    return (final - initial) / initial * 100

print("--- DataTypes before conversion ---")
print(pandas_df.dtypes)
initial_mem = calculate_memory_usage(pandas_df)
print(f"initial_memory_usage : {initial_mem} ")
print("--- DataTypes after conversion ---")
print(pandas_df2.dtypes)
final_mem = calculate_memory_usage(pandas_df2)
print(f"final_memory_usage : {final_mem}")
print("--- Memory reduction ---")
print(calculate_percentage_difference(initial_mem, final_mem))