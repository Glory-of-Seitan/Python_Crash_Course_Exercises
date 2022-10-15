def city_country(city, country):
    place = f"{city.title()}, {country.title()}"
    return place


print(city_country("london", "united kingdom"))
print(city_country("new york", "United states"))
print(city_country("tokyo", "japan"))
