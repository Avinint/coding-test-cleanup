import json

def get_countries():
    with open('data_countries.json') as json_file:
        data = json.load(json_file)
    return [country for country in data]

def get_areas():
    with open('data_areas.json') as json_file:
        data = json.load(json_file)
    return [area for area in data]

def get_area_by_code(code):
    match = [area for area in liste_areas if area[0] == code]
    return match and match[0] or None

def get_countries_by_area(code):
    return [country for country in liste_countries if country[1] == code]

def get_areas_by_parent(code=None, d=0):
    areas = [a for a in liste_areas if a[1] == code]
    indent = d * '\t'
    for area in areas:
        display = indent + area[2]
        countries = len(get_countries_by_area(area[0]))
        if countries:
            print(f"{display} {countries}")
        else:
            print(display)
        get_areas_by_parent(area[0], d+1)
    return len(areas)

def get_areas_by_parent_countries(code=None, d=0):
    areas = [a for a in liste_areas if a[1] == code]
    indent = d * '\t'
    for area in areas:
        display = indent + area[2]
        countries = get_countries_by_area(area[0])
        if countries:
            print(display, len(countries))
            for country in countries:
                print(f"{indent}\t{country[3]}")
        else:
            print(display)
        get_areas_by_parent_countries(area[0], d+1)
    return len(areas)

liste_countries = get_countries()
liste_areas = get_areas()
get_areas_by_parent_countries()

