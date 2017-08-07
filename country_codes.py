from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the paygal 2-digit country code for a given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the country wasnt found, retun None.
    return None

#print(get_country_code('Andorra'))
#print(get_country_code('Hungary'))
#print(get_country_code('Afghanistan'))