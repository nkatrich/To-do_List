import json

fl_nm = "data.json"

def in_data():
    with open(fl_nm, "w") as f:
        json.dump(data, f, indent=4)
        print("Data have been saved!\n")

def get_data():
    with open(fl_nm, "r") as f:
        return json.load(f)

def show_notes(data):
    print('Current notes:\n')
    [print(f'\033[1m{i}\033[0m') for i in data["Notes"]] if len(data["Notes"]) != 0 else print("\033[1mYou dont have any note yet.\033[0m")

def remove_notes(note, type):
    if type == 'REM':
        pass

print(f'\033[1m{25 * '*'} TO-DO List ready for notes! {25 * '*'}\033[0m\n')
data = get_data()

while True:
    show_notes(data)
    note = input("\n\u001b[32mType note, type note for delete(key word for delete specific: REM)(or delete all type: DEL) or key word for exit: EXIT\033[0m\n")
    note = note.split()
    if note[0] == 'EXIT':
        print('\nProgramm finished. All data saved.')
        break
    elif note[0] == 'REM':
        remove_notes(note, 'REM')
    elif note[0] == 'DEL':
        remove_notes(note, 'DEL')
    else:
        data["Notes"].append(note)
        in_data()
