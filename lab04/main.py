import sys

from stats import average_by_city, read_valid, warmest_city


lines = sys.stdin.read().splitlines()

records = read_valid(lines)

non_empty_lines = [
    line for line in lines
    if line.strip()
]

valid_count = len(records)
invalid_count = len(non_empty_lines) - valid_count

print(valid_count)
print(invalid_count)

if records:
    averages = average_by_city(records)
    city = warmest_city(records)
    print(f"{averages[city]:.1f}")
else:
    print("0.0")
