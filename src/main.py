from extract import extract_data
from transform import transform_data
from load import load_data
from logger import log_progress


def main():
    log_progress("ETL pipeline started")

    df = extract_data("data/banks.csv")
    df = transform_data(df)
    load_data(df)

    log_progress("ETL pipeline finished successfully")
    print("ETL ejecutado correctamente.")


if __name__ == "__main__":
    main()