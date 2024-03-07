from pyfake.adjective import Adjective

def test_adjective():
    adj = Adjective().adjective

    assert isinstance(adj, str)