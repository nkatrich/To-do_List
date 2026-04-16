import json
import os

file_name = "data.json"
stats = []

def in_data():
    with open(file_name, "w") as file:
        json.dump(stats, file, indent=4)
        print("Data saved to data.json!")

def get_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)

def show_notes():
    data = get_data()
    print(f'''Current notes:
{data}''')

print('TO-DO List ready for notes!\n')
while True:
    note = input("Type note or key word for exit: EXIT\n")
    if note == 'EXIT':
        print('\nProgramm finished. All data saved.')
        break
    stats.append(note)
