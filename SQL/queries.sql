SELECT * FROM banks;

SELECT bank, country, market_cap_usd
FROM banks
WHERE market_cap_usd > 150;

SELECT country, COUNT(*) AS total_banks
FROM banks
GROUP BY country
ORDER BY total_banks DESC;

SELECT AVG(market_cap_usd) AS average_market_cap
FROM banks;

SELECT bank, market_cap_usd
FROM banks
ORDER BY market_cap_usd DESC
LIMIT 5;