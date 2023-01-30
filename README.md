# Visma Solutions - programming task 2023
This is a repo for returning programming task for Visma Solutions Summer Trainee 2023 recruitment process.

## Running the code
Run `python client.py`

## Description
Problem was easy to understand. The task was to write basic URI parser that does not implement the whole URI standard. And a basic client for using it.
Solution was easy to implement but there were some parts where I had to make compromises.

### Compromises and further improvements
Biggest compromise I made was with validating parameters for every *path*. Currently the parser doesn't allow any other parameters for any given path other than the ones which were described in requirements. Also currently parser converts parameters to integers only based on the name of the parameter. This is to avoid the possibility of *documentid* being accidentally converted to an integer.

Further improvements include better handling for the compromises that I had to make and better implementation for parsing RFC 3986 compliant URIs.
