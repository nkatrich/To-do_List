import json
import os

file_name = "data.json"

def in_data():
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        print("Data have been saved!\n")

def get_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)

def show_notes(data):
    print('Current notes:\n')
    [print(i) for i in data["Notes"]] if len(data["Notes"]) != 0 else print("You dont have any note yet.\n")

data = get_data()
print('TO-DO List ready for notes!\n')
while True:
    show_notes(data)
    note = input("\nType note or key word for exit: EXIT\n")
    if note == 'EXIT':
        print('\nProgramm finished. All data saved.')
        break
    data["Notes"].append(note)
    in_data()
