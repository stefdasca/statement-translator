To travel in the country of Acadnia, each passenger must pass through a control that involves creating a control key by merging two passwords, one belonging to the traveler, of size $n$, and one belonging to the airport, of size $m$, both consisting of numbers in ascending order (the merge operation combines two ordered sequences so that the result remains ordered). Ultimately, after the merging operation, a control key will be obtained, with a size equal to the sum of the sizes of the two passwords, which will contain all elements from both passwords and will itself be ordered in ascending order. To facilitate this, the airport has created a program that performs this merging operation, but which sometimes goes wrong.

# Task

They ask you to help fix the problem so that the correct control key is obtained. You can find the program [here](bad_source.cpp) or in the â€œAttachmentsâ€ section on the side.

# Input data

The numbers $n$ and $m$ are read from the keyboard, followed by the two sequences of numbers in ascending order, separated by space, with sizes $n$ and $m$, representing the passwords.

# Output data

Print on the screen the control key, of size $n+m$, formed by merging the two passwords, ordered in ascending order.

# Constraints and clarifications
* $1 \leq n \leq 100$
* $1 \leq m \leq 100$
* The password elements are between $-1 \ 000$ and $1 \ 000$.

# Example 1
`stdin`
```
5 5
1 2 3 4 5
6 7 8 9 10
```
`stdout`
```
1 2 3 4 5 6 7 8 9 10
```

# Example 2
`stdin`
```
4 6
10 19 20 25
19 20 20 31 45 55
```
`stdout`
```
10 19 19 20 20 20 25 31 45 55
