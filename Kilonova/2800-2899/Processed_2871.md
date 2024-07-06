Following the monetary reform, the financial experts concluded that the number of monetary values necessary for any payment is 4 and named them, for simplicity, RAN, REN, RIN, RON. Thus, they established the base coin as RAN, with a value of $1$. The other three values were expressed either in terms of the base coin or in terms of another value. For instance, the REN coin has a value of $5$ RAN, the RIN coin has a value of $2$ REN, and the RON coin has a value of $2$ RIN. However, the financial experts are now questioning whether the four monetary values offer enough payment diversity to allow a sum of money to be paid in multiple ways.

# Task

Write a program that determines in how many ways a certain sum $S$, expressed in the base coin RAN, can be paid using the new coins introduced by the monetary reform.

# Input data

The input file `reforma.in` contains a single line which contains the value $S$.

# Output data

The output file `reforma.out` contains a single line with a natural number indicating in how many ways the sum $S$ can be paid using the new values.

# Constraints and clarifications

* $1 \leq S \leq 10 \ 000$

# Example 1

`reforma.in`
```
23
```

`reforma.out`
```
10
```

## Explanation

|#|RAN|REN|RIN|RON|
|-|-|-|-|-|
|1|23|0|0|0|
|2|18|1|0|0|
|3|13|2|0|0|
|4|8|3|0|0|
|5|3|4|0|0|
|6|13|0|1|0|
|7|8|1|1|0|
|8|3|2|1|0|
|9|3|0|2|0|
|10|3|0|0|1|

# Example 2

`reforma.in`
```
36
```

`reforma.out`
```
26
```

## Explanation

|#|RAN|REN|RIN|RON|
|-|-|-|-|-|
|1|36|0|0|0|
|2|31|1|0|0|
|3|26|2|0|0|
|4|21|3|0|0|
|5|16|4|0|0|
|6|11|5|0|0|
|7|6|6|0|0|
|8|1|7|0|0|
|9|26|0|1|0|
|10|21|1|1|0|
|11|16|2|1|0|
|12|11|3|1|0|
|13|6|4|1|0|
|14|1|5|1|0|
|15|16|0|2|0|
|16|11|1|2|0|
|17|6|2|2|0|
|18|1|3|2|0|
|19|6|0|3|0|
|20|1|1|3|0|
|21|16|0|0|1|
|22|11|1|0|1|
|23|6|2|0|1|
|24|1|3|0|1|
|25|6|0|1|1|
|26|1|1|1|1|