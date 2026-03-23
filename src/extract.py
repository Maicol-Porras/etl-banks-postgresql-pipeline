import pandas as pd
from logger import log_progress


def extract_data(file_path="data/banks.csv"):
    log_progress("Extract phase started")
    df = pd.read_csv(file_path)
    log_progress("Extract phase completed")
    return df