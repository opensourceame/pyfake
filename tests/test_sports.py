from pyfake.sport import Sport

def test_person():
    s = Sport()

    assert isinstance(s.name, str)
    assert isinstance(s.players, int) or isinstance(s.players, str)
    assert isinstance(s.field_size, str)
    assert isinstance(s.equipment, list)
    assert isinstance(s.outdoor, bool)