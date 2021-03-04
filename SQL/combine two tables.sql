select FirstName, LastName, City, state
from Person left join Address
on Person.PersonId = Address.PersonId
