import json

with open('pools.json', 'r', encoding='utf-8') as file:
    pools = json.load(file)

def is_open_on_monday(pool):
    hours = pool['WorkingHoursSummer'].get('Понедельник', '')
    if not hours:
        return False
    start, end = hours.split('-')
    return start <= '10:00' and end >= '12:00'


suitable_pools = [pool for pool in pools if is_open_on_monday(pool)]

if not suitable_pools:
    print("Нет подходящих бассейнов")
else:
    best_pool = max(suitable_pools, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))

    dimensions = best_pool['DimensionsSummer']
    address = best_pool['Address']
    print(f"{dimensions['Length']}x{dimensions['Width']}")
    print(address)