from pathlib import Path
import pandas as pd

def get_data_jsonl(fn: str):
    """
    Reads in the data from the jsonl file and returns a dataframe.
    """
    df = pd.read_json(fn, lines=True)
    df.to_excel(Path(fn).with_suffix('.xlsx'), index=False)
    return df

get_data_jsonl('output.jsonl')