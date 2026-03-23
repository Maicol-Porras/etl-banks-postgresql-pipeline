# ETL Banks PostgreSQL Pipeline

## Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL.

The pipeline extracts banking data from a CSV file, transforms and cleans it using pandas, and loads it into a PostgreSQL database for structured storage and SQL-based analysis.

---

## Architecture

The project follows a modular ETL design:

* **Extract**: Reads raw data from a CSV file
* **Transform**: Cleans, formats, and validates the data
* **Load**: Inserts processed data into PostgreSQL

---

## Technologies Used

* Python
* pandas
* PostgreSQL
* psycopg2
* SQL
* Logging

---

## Project Structure

```
etl-banks-postgresql-pipeline/
│
├── data/        # Raw data (CSV)
├── logs/        # ETL logs
├── sql/         # SQL scripts
├── src/         # Python source code
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── db.py
│   └── logger.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to Run

### 1. Create the PostgreSQL database

```sql
CREATE DATABASE etl_project;
```

---

### 2. Create the table

Run the following SQL script:

```
sql/create_table.sql
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure database credentials

Update your PostgreSQL credentials in:

```
src/db.py
```

---

### 5. Run the ETL pipeline

```bash
python src/main.py
```

---

## Example Queries

```sql
SELECT * FROM banks;

SELECT bank, market_cap_usd
FROM banks
ORDER BY market_cap_usd DESC
LIMIT 5;

SELECT country, COUNT(*) AS total_banks
FROM banks
GROUP BY country
ORDER BY total_banks DESC;
```

---

## Key Features

* Modular ETL architecture
* PostgreSQL integration
* Batch data insertion
* Logging for pipeline traceability
* SQL-based data validation

---

## Author

Maicol Porras
