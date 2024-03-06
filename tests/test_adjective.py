from pyfake.adjective import Adjective

def test_adjective():
    adj = Adjective().adjective

    assert adj in Adjective().CONFIG['adjectives']