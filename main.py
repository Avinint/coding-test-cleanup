import json

def get_countries():
    with open('data_countries.json') as json_file:
        data = json.load(json_file)
    return [country for country in data]

def get_areas():
    with open('data_areas.json') as json_file:
        data = json.load(json_file)
    return [area for area in data]

def get_country_by_code(code):
    match = [country for country in countries if country[0] == code]
    return match and match[0] or None

def get_country_by_name(name):
    match = [country for country in countries if country[3] == name]
    return match and match[0] or None

def get_country():
    user_input = input("Country?\n")
    if user_input.isdigit():
        return get_country_by_code(int(user_input))
    return get_country_by_name(user_input)

def get_area_by_code(code):
    match = [area for area in areas if area[0] == code]
    return match and match[0] or None

res_country = None
countries = get_countries()
areas = get_areas()

while res_country is None:
    res_country = get_country()
    if res_country:
        country_code, country_area, iso, country_name = res_country
    else:
        print("Country not in database")

area_code, parent_area, area_name = get_area_by_code(country_area)
areas = [country_name, area_name]

while parent_area:
    area_code, parent_area, area_name = get_area_by_code(parent_area)
    areas.append(area_name)

print (" < ".join(areas[::-1]) )


