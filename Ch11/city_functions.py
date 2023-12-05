def get_city_name(City, Country, population = ''):
    """generate city name"""
    if population:
        city_name = (f"{City} {Country} {population}")
    else:
        city_name = (f"{City} {Country}")
    return city_name.title() 


