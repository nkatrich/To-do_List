import json
import os

file_name = "data.json"

def in_data():
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        print("Data saved to data.json!")

def get_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    else:
        return {}

def show_notes(data):
    print('Current notes:')
    [print(i) for i in data["Notes"]]

data = get_data()
print('TO-DO List ready for notes!\n')
while True:
    note = input("Type note or key word for exit: EXIT\n")
    if note == 'EXIT':
        print('\nProgramm finished. All data saved.')
        break
    data["Notes"].append(note)
    in_data()
    show_notes(data)
