import re

example_strings = [
    "Mortal Kombat™ 11 6_18_2023 1_20_21 PM",
    "Cyberpunk 2077 (C) 2020 by CD Projekt RED 12_2_2023 12_58_01 AM",
    "Overwatch 2023-04-17 00-33-48"
]

for example in example_strings:
    parts = re.split(pattern, example)
    if len(parts) > 1:
        file_name = parts[0].strip()
        print(f"File Name: {file_name}")
        date_time = parts[1].strip()
        print(f"Date/Time: {date_time}")
    else:
        print(f"No match found for: {example}")
