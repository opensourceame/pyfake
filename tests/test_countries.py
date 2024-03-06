from pyfake.country import Country

def test_country():
    c = Country()

    assert isinstance(c.name, str)
    assert isinstance(c.currency, str)
    assert isinstance(c.capital_city, str)
    assert isinstance(c.population, int)
    assert isinstance(c.area, int)
    assert isinstance(c.languages, list)
