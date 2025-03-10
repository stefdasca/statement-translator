
# Task
To keep track of how much money he has collected, Marius recorded in a table of size $n \times m$ the amounts of money he collected each day. He wants to buy the AcadBox console, and to do so, he needs to know the total amount of money he has collected. He wrote a small program to calculate the total amount, but it seems that it does not work. Therefore, he asked for your help to fix it and to be able to buy the console. You can find the program [here](bad_source.cpp) or in the sidebar under the â€œAttachmentsâ€ section.

# Input data
Two integers $n$ and $m$ are read from the keyboard, representing the number of rows and the number of columns of the matrix, respectively. The following $n$ lines will contain $m$ integers separated by a space, representing the amounts of money Marius collected each day.

# Output data
Print the total amount of money that Marius has collected.

# Constraints and clarifications
* $1 \leq n \leq 100$
* $1 \leq m \leq 100$
* The amounts of money are integers between $0$ and $1 \ 000$.

# Example
`stdin`
```
2 3
1 2 3
4 5 6
```
`stdout`
```
21
```
## Explanation
$1 + 2 + 3 + 4 + 5 + 6 = 21$
