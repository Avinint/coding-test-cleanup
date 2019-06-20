import json

def get_countries():
    with open('data_countries.json') as json_file:
        return json.load(json_file)

def get_areas():
    with open('data_areas.json') as json_file:
        return json.load(json_file)

def get_country_by_code(code):
    match = [country for country in countries if country[0] == code]
    return match and match[0] or None

def get_country_by_name(full_name):
    name = " ".join([name.strip().lower().capitalize() for name in full_name.split()])
    match = [country for country in country_list if country[3] == name]
    return match and match[0] or None

def get_country():
    user_input = input("Country?\n")
    if user_input.isdigit():
        return get_country_by_code(int(user_input))
    return get_country_by_name(user_input)

def get_area_by_code(code):
    match = [area for area in area_list if area[0] == code]
    return match and match[0] or None

input_country = None
country_list = get_countries()
area_list = get_areas()

while input_country is None:
    input_country = get_country()
    if input_country:
        country_code, country_area, iso, country_name = input_country
    else:
        print("Country not in database")

area_code, parent_area, area_name = get_area_by_code(country_area)
areas = [country_name, area_name]

while parent_area:
    area_code, parent_area, area_name = get_area_by_code(parent_area)
    areas.append(area_name)

print (" < ".join(areas[::-1]) )