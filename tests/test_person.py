from pyfake.person import Person

def test_person():
    c = Person()

    assert isinstance(c.first_name, str)
    assert isinstance(c.last_name, str)
    assert isinstance(c.email, str)
    assert isinstance(c.age, int)
    assert isinstance(c.gender, str)

    assert c.gender     in ['Male', 'Female']
    assert c.age        in range(1, 101)
    assert c.email.find ('@') > 0