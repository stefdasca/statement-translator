Pacala has just been elected mayor in the village of Pacalici. Since only families with kinship ties to the new mayor live in his village, Pacala decided to number the houses so that he knows the kinship relationship he has with a family member living in that house, and how many men, women, and children live in each house.

Thus, all houses have a number consisting of $4$ digits, where the first digit (from left to right) represents the degree of kinship with Pacala (they can be relatives of degree 1, 2, or 3), the second digit represents the number of men living in that house (there can be a maximum of $6$ men), the third digit represents the number of women (there can be a maximum of $6$ women), and finally, the last digit of the number represents the number of children (maximum $9$) belonging to the family in that house.

# Task

Knowing the number of houses in Pacala's village, as well as the numbers of the houses, display how many families have kinship ties of degree 1, 2, and 3 with Pacala, as well as the number of men, women, and children living in Pacala's village.

# Input data

The input file `case.in` contains on the first line a natural number $n$ representing the number of houses. The next $n$ lines contain the house numbers, one house per line.

# Output data

The output file `case.out` will contain on the first line the number of relatives of degree 1, on the second line the number of relatives of degree 2, and on the third line the number of relatives of degree 3. On the fourth line, it will contain the number of men, on the fifth line the number of women, and on the last line the number of children.

# Constraints and clarifications

* $1 \leq n \leq 50$

# Example

`case.in`
```
6
1232
3215
2345
1325
3459
1123
```

`case.out`
```
3
1
2
15
17
29
