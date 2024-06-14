import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    new_file = []
    for position in data:
        if isinstance(position, str):
            new_file.append(position + '!')
        elif isinstance(position, int) and not isinstance(position, bool):
            new_file.append(position + 1)
        elif isinstance(position, bool):
            new_file.append(not position)
        elif isinstance(position, list):
            position.extend(position)
            new_file.append(position)
        elif isinstance(position, dict):
            position['newkey'] = None
            new_file.append(position)
        else:
            continue

with open('updated_data.json', 'w', encoding='utf-8') as out_file:
    json.dump(new_file, out_file, indent=3)
