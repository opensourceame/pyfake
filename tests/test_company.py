from pyfake.company import Company

def test_company():
    c = Company()
    name = c.name
    size = c.size

    assert name is not None
    assert size in range(1, 101)