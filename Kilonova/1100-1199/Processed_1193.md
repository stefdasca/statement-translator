In Gigel's class there are $n$ students and they have just taken a math test. The teacher has brought the grades to all the students, and now Gigel wants to know two things:

- What are the grades that have appeared the most? If there are multiple such grades, they should be displayed in ascending order.
- What are the grades that were not given? If there are multiple such grades, they should be displayed in ascending order.

# Input data

The first line of the input file `nota.in` contains $n$, the number of students. The next $n$ lines contain the grades received by the students in Gigel's class.

# Output data

The first line of the output file `nota.out` should contain the grades that were given the most. The second line should contain the grades that were not given. If all grades were given, print `-1`.

# Constraints and clarifications

* $1 \leq n \leq 20$;
* The students' grades are between $1$ and $10$.
* The statement has been reconstructed based on information deduced from the problem, the original statement was not found. If you have the original statement, please contact us so we can restore the problem completely.

# Example

`nota.in`
```
5
4
8
9
8
10
```

`nota.out`
```
8
1 2 3 5 6 7
