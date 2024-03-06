# PyFake

Pyfake is a synthetic data generator for use in Unit testing or
other places where you need to use fake data for some purpose.

## Usage

```python
from pyfake import Person

person = Person()

print(person.name)        # Joe Bloggs
print(person.email)       # joe.bloggs@example.com

from pyfake import TcpIp

print(TcpIp().ipv6)       # ca39:a408:5736:769:a0b5:c5a5:393e:d2b
```

## Object generator list

* Adjective
* Book
* Company
* Country
* Person
* Sports
* TCP/IP (ip addresses, port ranges etc)

_more generators are being added, check back for more details or request a generator via GH issues_
