from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the paygal 2-digit country code for a given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Bolivia':
        return 'bo'
    # if the country wasnt found, retun None.
    return None

print(get_country_code('Bolivia')) #, Plurinational State of'))
#print(get_country_code('Venezuela, RB'))
#print(get_country_code('Afghanistan'))