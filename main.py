import csv

with open("world-data-2023.csv", "r") as f:
    reader = csv.reader(f)
    headers = next(reader)

    country_idx = headers.index("Country")
    birth_rate_idx = headers.index("Birth Rate")
    co2_idx = headers.index("Co2-Emissions")
    population_idx = headers.index("Population")

    countries = []
    birth_rates = []
    co2_emissions = []
    populations = []

    for row in reader:
        countries.append(row[country_idx])
        birth_rates.append(row[birth_rate_idx])
        co2_emissions.append(row[co2_idx])
        populations.append(row[population_idx])

with open("countries.txt", "w") as f:
    f.write("\n".join(countries))

with open("birth_rates.txt", "w") as f:
    f.write("\n".join(birth_rates))

with open("co2_emissions.txt", "w") as f:
    f.write("\n".join(co2_emissions))

with open("populations.txt", "w") as f:
    f.write("\n".join(populations))
