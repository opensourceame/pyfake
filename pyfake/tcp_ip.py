from .generator import Generator
import random
import ipaddress

def generate_ipv4():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generate_ipv6():
    return str(ipaddress.IPv6Address(random.randint(0, 2**128-1)))

class TcpIp(Generator):
    def generate(self):
        self.ipv4 = generate_ipv4()
        self.ipv6 = generate_ipv6()
        self.port = random.randint(0, 65535)
