# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, COALESCE(NULLIF(Address.city,''), null) as city, COALESCE(NULLIF(Address.state,''), null) as state
FROM Person
LEFT JOIN Address ON Address.personId = Person.personId