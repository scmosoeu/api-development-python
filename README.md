# api-development-python

Develop a REST API using python programming language

Below are the example outputs for the following endpoints when requesting information about almonds.

```bash
/almonds
```

```json
{
    "information_date": "2024-04-02",
    "daily_prices": {
        "commodity": "almonds",
        "total_value_sold": {
            "value_sold": 1200.0,
            "month_to_date": 1200.0
        },
        "total_quantity_sold": {
            "quantity_sold": 20,
            "month_to_date": 20
        },
        "total_kg_sold": {
            "kg_sold": 10.0,
            "month_to_date": 10.0
        },
        "quantity_available": 164
    }
}
```

```bash
/containers/almonds
```

```json
{
    "information_date": "2024-04-02",
    "commodity": "almonds",
    "daily_prices": [
        {
            "container": "1KG PACKET",
            "quantity_available": 64,
            "total_value_sold": {
                "value_sold": 0.0,
                "month_to_date": 0.0
            },
            "total_quantity_sold": {
                "quantity_sold": 0,
                "month_to_date": 0
            },
            "total_kg_sold": {
                "kg_sold": 0.0,
                "month_to_date": 0.0
            },
            "average_price_per_kg": 0.0
        },
        {
            "container": "500G PACKET",
            "quantity_available": 100,
            "total_value_sold": {
                "value_sold": 1200.0,
                "month_to_date": 1200.0
            },
            "total_quantity_sold": {
                "quantity_sold": 20,
                "month_to_date": 20
            },
            "total_kg_sold": {
                "kg_sold": 10.0,
                "month_to_date": 10.0
            },
            "average_price_per_kg": 120.0
        }
    ]
}
```