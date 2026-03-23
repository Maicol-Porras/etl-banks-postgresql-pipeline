CREATE TABLE IF NOT EXISTS banks (
    id SERIAL PRIMARY KEY,
    bank VARCHAR(255),
    country VARCHAR(255),
    market_cap_usd NUMERIC(12,2)
);