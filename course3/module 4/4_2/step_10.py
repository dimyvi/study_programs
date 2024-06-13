import csv
from datetime import datetime
def get_latest_entries(data):
    latest_entries = {}
    for entry in data:
        email = entry['email']
        dtime = datetime.strptime(entry['dtime'], '%d/%m/%Y %H:%M')
        if email not in latest_entries or dtime > latest_entries[email]['dtime']:
            latest_entries[email] = {'username': entry['username'], 'dtime': dtime}
    return latest_entries

with open('name_log.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file))

latest_entries = get_latest_entries(data)

final_data = [{'username': value['username'], 'email': email, 'dtime': value['dtime'].strftime('%d/%m/%Y %H:%M')} for
              email, value in latest_entries.items()]

final_data_sorted = sorted(final_data, key=lambda x: x['email'])

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['username', 'email', 'dtime'])
    writer.writeheader()
    writer.writerows(final_data_sorted)
