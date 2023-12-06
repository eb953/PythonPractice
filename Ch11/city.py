from city_functions import get_city_name

print("Enter 'q' to quit")
while True:
    city = input("What is the city name?")
    if city == 'q':
        break
    country = input("What is the location of the city?")
    if country == 'q':
        break 
    population = input("What is the population?")

    formatted_city = get_city_name(city, country, population)
    print(f"{formatted_city}")