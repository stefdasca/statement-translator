Ghiță received an exotic plant for his birthday, which behaves very strangely. He measured it when he received it and found that it had $D$ cm. Then, he noticed that it grows in a special rhythm:
* On the first day, the plant grows by $A$ cm;
* On the second day, it decreases by $B$ cm;
* On the third day, it grows again by $A$ cm;
* On the fourth day, it decreases again by $B$ cm;
* ...
* and so on.

In short, on odd-numbered days it grows by $A$ cm, and on even-numbered days, it decreases by $B$ cm.

# Task
Knowing $D$, the initial height of the plant, and the values $A$ and $B$ by which it grows and decreases, respectively, find out what height Ghiță's plant will have at the end of the $N$-th day.

# Input data
The first line of the file `planta.in` will contain four natural numbers $D$, $A$, $B$, $N$, in this order, separated by spaces, with the meanings mentioned in the statement.

# Output data
The first line of the file `planta.out` will contain a number $H$, signifying the final height of the plant in centimeters at the end of the $N$-th day.

# Constraints and clarifications
* $0 \\leq D \\leq 100$;
* $1 \\leq B \\leq A \\leq 1 \\ 000 \\ 000$;
* $1 \\leq N \\leq 1 \\ 000 \\ 000 \\ 000$;
* For 50% of the tests, $1 \\leq N \\leq 1 \\ 000 \\ 000$;
* It is guaranteed that for all tests the values fit within the `int` type.

# Example 1

`planta.in`
```
4 5 2 3
```

`planta.out`
```
12
```

## Explanation
- After the first day: $H = 4 + 5 = 9$;
- After the second day: $H = 9 - 2 = 7$;
- After the third day: $H = 7 + 5 = 12$;
So at the end of the 3rd day, the height of the plant will be $12$ cm.

# Example 2

`planta.in`
```
57 1000 1000 120
```

`planta.out`
```
57
```