countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

d = list(zip(capitals, countries, population))
for ind, (cap, country, popular) in enumerate(d):
    print(f"{cap} is the capital of {country}, population equal {popular} people.")