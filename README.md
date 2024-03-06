# PyFake

Pyfake is a synthetic data generator for use in Unit testing.

## Usage

```python
from pyfake import Person
person = Person()

print(person.name)  # Joe Bloggs
print(person.email) # joe.bloggs@example.com
```

## Object generator list

* Adjective
* Book
* Company
* Country
* Person
* TCP/IP (ip addresses, port ranges etc)

_more generators are being added, check back for more details or request a generator via GH issues_
