
# Problem Statement
We define a natural number "tablou" $X$ if and only if:
- $X$ is composite;
- There exist natural numbers $A$ and $B$ such that $A \times B = X, 2 \leq A \leq B \leq \frac{X}{2}$ with the property that there exists a rectangular matrix with width $A$ and length $B$, such that the sum of any $A$ numbers is positive $(\geq 0)$ and there exist $B$ numbers, so that the sum of these $B$ numbers is divisible by $X$;
- Each number at coordinates $(row, col)$ will be in the form: $row \times col \times (A - col + 1) \times (B - row + 1)$;
- Rows will be numbered from $1$ to $A$, and columns will be numbered from $1$ to $B$;

For example, 25 is a "tablou" number, because we can form a rectangular matrix with a width of 5 and a length of 5, looking like this:

~[image_200x200.png]

No matter how we choose 5 numbers from that matrix, the sum of those 5 numbers will be positive and there exist the 5 numbers $40$, $40$, $40$, $40$ and $40$, whose sum is $40 + 40 + 40 + 40 + 40 = 200 = 25 \times 8$, therefore the sum of those 5 numbers is divisible by $25$.
Given the number $N$ and on the next $N$ lines one number $X$ each, print $YES$ if $X$ is a "tablou" number, otherwise print $NO$ if $X$ is not a "tablou" number.

# Task
Given the natural number $N$ and on the next $N$ lines one number $X$ each, print $YES$ if it satisfies the property from the statement, otherwise print $NO$ if it does not satisfy the property from the statement.

# Input Data
In the file `tablou.in` contains the number $N$ on the first line, and on the next $N$ lines contains one natural number $X$.

# Output Data
In the file `tablou.out` contains the message $YES$ if the number $X$ is a "tablou" number, otherwise $NO$ if the number $X$ is not a "tablou" number.

# Constraints and clarifications
* $1 \leq N \leq 200\ 000$
* $1 \leq X \leq 1\ 000\ 000$
* For 25 points, $1 \leq N \leq 1\ 000$ and $1 \leq X \leq 100$
* For 4 points, each $X$ in the input file is not composite
* 1 is not considered a composite number

# Example:
`tablou.in`
```
3
25
13
18
```
`tablou.out`
```
YES
NO
NO
```

# Explanations:
25 is a "tablou" number, because there exists a rectangular matrix with a width of 5 and a length of 5 which has the property specified from the statement.
13 is not a "tablou" number because it is not composite.
18 is not a "tablou" number because there is no rectangular matrix that has the property specified in the statement.
```

Please review the statement and let me know if you find any grammar or syntax errors so that I can fix them for you.