# Prompt

*Problem*:

Please design and develop a service that I can query that will yield the
difference between 1.) the sum of the squares of the first n natural
numbers and 2.) the square of the sum of the same first n natural numbers,
where n is guaranteed to be no greater than 100.

Example:

The sum of the squares of the first ten natural numbers is:

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

*Requirements*:

You should use Python3.6 and preferably Django (but if it will
add a lot of time to learn one of those & you know another Python framework
already, go ahead & use that).

I should be able to install your service by doing: pip install -r
requirements.txt from a virtual environment. Please include a README
with instructions for launching it.

I should be able to query your service at the following (or similar) endpoint:

localhost:8000/difference?number=n where n is any integer greater than 0
and less than or equal to 100.

Your service should emit a JSON object of the following structure:

{
"datetime":current_datetime,
"value":solution,
"number":n,
"occurrences":occurrences // the number of times n has been requested
"last_datetime": datetime_of_last_request
}

For persistence you can use postgres, mysql, memcached,
sqlite3 or redis.

*Optional 1*

Front end:

Create a react application (or any other front end framework or just
jquery) based on the above backend service that should display a list of
the above values in the four columns described above.

Your UI should have a form to enter the number that you wish to query.

*Optional 2*

Assume this is only the first of many such similar requests. For example, as a team we have decided that users really want to know the answer you may need to develop a service that also asks the following:

Please design and develop a service that I can query that will yield 1.) if a sequence of three natural numbers (a,b and c) are a Pythagorean triplet and 2.) the product of the sequence of these three numbers where abc = n, where c is guaranteed to be no greater than 1000.

Construct your application in such a way that you can easily scale to meet these additional product needs.

*Optional 3*

Use Python3.6 style typehinting


*Optional 4*

Unit tests are appreciated.

*Delivery*:

Please commit your code using either git or mercurial and use either
bitbucket or github, or a similar service.

# Discussion

I've created a simple service that creates database records whose primary key is the number passed in as input (n above).
Each time the service receives a request for a record, it first attempts to fetch an existing record with the same primary key.
- If it finds an existing record it updates its timestamps and increments it's `occurrences` count, then returns the values as JSON.
- If it doesn't find an existing record it creates one and returns its values as JSON.

# Documentation

From a virtual environment run `pip install -r requirements.txt`

To start the API server run `python3 manage.py runserver`

This will start an HTTP server on port 8000.

You can query the service by sending a GET request to localhost:8000/difference?number=10
Where 10 here is n.

There is a simplistic React front end if you navigate to the root in a browser (localhost:8000/). It will fetch records on mount.
