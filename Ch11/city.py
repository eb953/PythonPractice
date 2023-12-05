from city_functions import get_city_name

print("Enter 'q' to quit")
while True:
    city = input("What is the city name?")
    if city == 'q':
        break
    country = input("What is the location of the cityu?")
    if country == 'q':
        break 

    formatted_city = get_city_name(city, country)
    print(f"{formatted_city}")