In one of the days at the Informatics Olympiad, $P$ attractive excursions are organized. A total of $N$ people participate in these excursions. For simplicity, the people have been numbered from $1$ to $N$, with the first $K$ people being the guides. A person can sign up for exactly one of the $P$ organized excursions.
To avoid unpleasant surprises (insufficient means of transport, insufficient seats at a restaurant, etc.), the organizers intend to study all configurations that might appear from the registration of participants, while considering that there will be at least one participant in each excursion.

# Task 

Write a program that determines the number of distinct configurations that can be obtained after the registration of the $N$ people in the $P$ organized excursions, such that the $K$ guides are registered in different excursions.

# Input data

The input file is named `ex.in` and contains a single line that contains $3$ natural numbers separated by a space: $N \\ K \\ P$ (representing the number of people, the number of guides, and the number of excursions, respectively).

# Output data

The output file `ex.out` contains a single line that contains the number of distinct configurations.

# Constraints and clarifications

* $1 \leq K \leq P \leq N \leq 100$
* In a configuration, the order of the excursions or the order in which people sign up for an excursion does not matter.

# Example

`ex.in`
```
5 3 4
```

`ex.out`
```
7
```

## Explanation

The $7$ distinct configurations are:

* $(1,4), (2), (3), (5)$
* $(1), (2,4), (3), (5)$
* $(1), (2), (3,4), (5)$
* $(1), (2), (3), (4,5)$
* $(1,5), (2), (3), (4)$
* $(1), (2,5), (3), (4)$
* $(1), (2), (3,5), (4)$