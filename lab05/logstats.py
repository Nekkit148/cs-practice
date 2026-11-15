EVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line: str) -> dict:
   
    parts = line.rstrip("\n").split(" ", 2)
    if len(parts) < 3:
        raise ValueError(f"негодная строка: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}

