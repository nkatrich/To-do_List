import json
import os

file_name = "data.json"

my_stats = {
    "Channel": "DevLog Nikita",
    "Programmer": 'Nikita Katrich'
}

with open(file_name, "w") as file:
    json.dump(my_stats, file, indent=4)
    print("Data saved to data.json!")

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        loaded_data = json.load(file)
        print(f"Biography: Name is {loaded_data["Programmer"]}, organisation is {loaded_data["Channel"]}.")
