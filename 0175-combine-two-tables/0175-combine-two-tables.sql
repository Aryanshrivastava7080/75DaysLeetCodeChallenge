# Write your MySQL query statement below
-- Create table Person(
--     id int,
--     lastname varchar(80),
--     firstname varchar(60)
-- );

-- Create table Address(
--     id int,
--     perid int,
--     city varchar(90),
--     state varchar(90)
-- );

SELECT 
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId;