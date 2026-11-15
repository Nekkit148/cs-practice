EVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line: str) -> dict:
   
    parts = line.rstrip("\n").split(" ", 2)
    if len(parts) < 3:
        raise ValueError(f"негодная строка: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        else:
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
    return counts

