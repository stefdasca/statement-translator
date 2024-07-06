# Task

The Alfaract and Betaract organizations are in a civil war, aiming to gain control over the Interact organization. Each organization has $n$ members, and for each member, the skill level is known: $a_i$ for those in the first organization and $b_i$ for those in the second organization.

# Task

As the two organizations prepare for war, they want to know for each $i$ from $1$ to $n$ which organization would win.

An organization wins scenario $i$ if it can choose $i$ people such that the sum of the values of those $i$ people is greater than the sum of the values of the $i$ people chosen by the other organization, regardless of how they are chosen.

# Input data

The first line will contain a number $n$, representing the number of members in each organization.

The second line will contain $n$ numbers, representing the skills of the members of Alfaract.

The third line will contain $n$ numbers, representing the skills of the members of Betaract.

# Output data

Print $n$ lines, each containing a string, as follows:

If Alfaract can win, print the string `Alfaract`.

If Betaract can win, print the string `Betaract`.

Otherwise, print `Equal`.

# Constraints and clarifications

* $1 \leq n \leq 10^5$
* $1 \leq a_i, b_i \leq 10^7$

# Example

`stdin`
```
5
5 9 2 4 5
8 8 3 1 4
```

`stdout`
```
Alfaract
Betaract
Betaract
Equal
Alfaract
```

~[name.png|optional_attribute]