from pyfake.tcp_ip import TcpIp

def test_tcp_ip():
    i = TcpIp()
    assert i.ipv6 is not None
    assert i.port in range(0, 65536)
    assert len(i.ipv4.split('.')) == 4
    assert len(i.ipv6.split(':')) == 8