def parse_record(line: str) -> dict:

    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("должно быть три поля")

    city, temperature, date = parts

    city = city.strip()
    temperature = temperature.strip()
    date = date.strip()

    if not city:
        raise ValueError("Город не может быть пустым")

    if not date:
        raise ValueError("Дата не может быть пустой")

    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }

def read_valid(lines: list[str]) -> list[dict]:

    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records

def average_by_city(records: list[dict]) -> dict:

    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0) + temperature
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


