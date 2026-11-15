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

def top_errors(lines, n: int) -> list:
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] != "ERROR":
            continue
        msg = event["message"]
        freq[msg] = freq.get(msg, 0) + 1

    ordered = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[msg, cnt] for msg, cnt in ordered[:n]]


def format_report(counts: dict, errors: list) -> str:
    out = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        out.append(f"{level}: {counts[level]}")

    out.append("")
    out.append("Частые ошибки:")
    for msg, cnt in errors:
        out.append(f"- {msg} — {cnt}")

    return "\n".join(out) + "\n"
