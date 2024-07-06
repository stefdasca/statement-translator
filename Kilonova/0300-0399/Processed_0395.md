### Task
Vasilică has become a passionate philatelist. For this reason, all his friends brought him stamps for his birthday, a lot of stamps. Now he is trying to organize the received stamps.
Each stamp is part of a series and has a value. Distinct stamps from the same series have distinct values. It's possible that Vasilică received duplicates (i.e. he received the same stamp multiple times).  
The value of a series is equal to the sum of the values of the distinct stamps from that series. Duplicates do not contribute to the value of the series, but Vasilică can use them to trade stamps with other philatelists.

### Task
Given the list of received stamps, write a program to solve the following requirements:
1. Determine the number of distinct series to which the received stamps belong;
2. Determine the number of unique stamps (that have no duplicates);
3. Determine the series with the highest value.

### Input data
The input file `timbre.in` contains on the first line the requirement that needs to be solved ($1$, $2$, or $3$). The second line contains a natural number $N$, representing the number of stamps received by Vasilică. On each of the following $N$ lines, a stamp is described. A stamp consists of a series (the name of the series to which the stamp belongs) and a value (a number representing the value of the stamp); the series and the value are separated by a single space.

### Output data
If the requirement is $1$ or $2$, the output file `timbre.out` will contain on the first line a number, representing the answer to the respective requirement. If the requirement is $3$, the output file `timbre.out` will contain the names of the series with the highest value, one name per line, in lexicographical order.

### Constraints and clarifications
* $1 \leq N \leq 100$;
* The values of the stamps are non-zero natural numbers less than or equal to $1 \ 000$;
* The names of the series consist of at most $50$ characters (letters, digits, space, hyphen);
* For each requirement, $33\\%$ of the points are awarded based on the tests passed.

### Example 1

`timbre.in`
```
1
9
Cap-de-bour 4
Romania 100 10
Cap-de-bour 7
Cap-de-bour 4
Romania 100 5
Romania 100 5
Romania 100 5
CRACIUN 2018 15
Romania 100 10
```

`timbre.out`
```
3
```

### Example 2

`timbre.in`
```
2
9
Cap-de-bour 4
Romania 100 10
Cap-de-bour 7
Cap-de-bour 4
Romania 100 5
Romania 100 5
Romania 100 5
CRACIUN 2018 15
Romania 100 10
```

`timbre.out`
```
2
```

### Example 3

`timbre.in`
```
3
9
Cap-de-bour 4
Romania 100 10
Cap-de-bour 7
Cap-de-bour 4
Romania 100 5
Romania 100 5
Romania 100 5
CRACIUN 2018 15
Romania 100 10
```

`timbre.out`
```
CRACIUN 2018
Romania 100
```

### Explanations
There are $3$ distinct series (`Cap-de-bour`, `Romania 100`, and `CRACIUN 2018`). In these series, there are only two unique stamps (the stamp with the value $7$ from the series `Cap-de-bour` and the one from the series `CRACIUN 2018`). The series with the highest value ($15$) are (in lexicographical order) `CRACIUN 2018` and `Romania 100`.