
from faker import Faker
fake = Faker()
print(fake.name())

print(fake.address())

print(fake.email())

from mimesis import Person
person = Person()
print(person.full_name(), person.name(), person.last_name(), person.username(), person.email(domains=["kuti.co.il"]))