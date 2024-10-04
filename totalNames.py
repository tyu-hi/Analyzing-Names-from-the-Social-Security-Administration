import json
import os

def sum_both_numbers(json_file):
    if not os.path.exists(json_file):
        print(f"Error: The file '{json_file}' does not exist.")
        return

    with open(json_file, 'r') as file:
        data = json.load(file)
    
    total_both = sum(year_data["both"] for year_data in data.values())
    
    print(f'Total sum of "both" numbers from 1880 to 2022: {total_both}')

# Replace 'totals.json' with the path to your JSON file if needed
sum_both_numbers('totals.json')