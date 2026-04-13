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

def get_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
        
data = get_data()

print('TO-DO List ready for notes!')
print(f'''Current notes:
{data}''')
