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
    [print(f'\033[1m{i}\033[0m') for i in data["Notes"]] if len(data["Notes"]) != 0 else print("\033[1mYou dont have any note yet.\033[0m")

data = get_data()
print(f'\033[1m{25 * '*'} TO-DO List ready for notes! {25 * '*'}\033[0m\n')
while True:
    show_notes(data)
    note = input("\n\u001b[32mType note or key word for exit: EXIT\033[0m\n")
    if note == 'EXIT':
        print('\nProgramm finished. All data saved.')
        break
    data["Notes"].append(note)
    in_data()
