Raul and Deniz play True or False. Being computer scientists, they changed the game settings, and now the questions are different. The game now unfolds as follows:

1. Raul and Deniz receive the numbers $ N $, $ Q $, and a sequence $ a_1 \ a_2 \ \dots \ a_N $ of natural numbers.
2. There follow $ Q $ questions in the form: "The numbers $ l $, $ r $ and $ p $ ($ 1 \leq l \leq p \leq r \leq N $) are given. Say if $ a_p $ is equal to $ \max(a_l, a_{l+1} \dots a_r) $". Raul and Deniz must find out as quickly as possible if they should say True or False.

# Task

To respond very quickly to questions, they asked you to help write a program that answers these questions as quickly as possible.

# Input data

The first line contains two natural numbers, $ N $ and $ Q $.

The second line contains $ N $ natural numbers, representing the sequence $ a_1 \ a_2 \ \dots \ a_N $.

The next $ Q $ lines each contain a triplet of numbers, representing $ l $, $ r $ and $ p $, in this order.

# Output data

Print a sequence of $ Q $ characters, the $ i $-th character being $ 1 $ if the answer to the $ i $-th query is true, and $ 0 $ otherwise.

# Constraints and clarifications

* $ 1 \leq N, Q \leq 10^6 $
* $ a_i \leq 10^9 $
* It is recommended to print the entire sequence of characters (0 or 1) only once, at the end of the queries

|#|Score|Constraints|
|-|-|--------|
|1|12|$1 \leq N, Q \leq 3 \ 000$|
|2|15|$1 \leq N \leq 3 \ 000$|
|3|11|$1 \leq N, Q \leq 100 \ 000$|
|4|62|No other constraints|

# Example 1

`stdin`
```
8 12
1 5 5 2 4 9 3 2
1 2 2
1 2 1
2 3 2
2 3 2
2 4 3
2 4 4
2 4 2
1 6 6
7 8 8
4 5 4
3 6 3
3 6 6
```

`stdout`
```
101110110001
```

## Explanation

$ N = 8 $, $ Q = 12 $

$ a = [1, 5, 5, 2, 4, 9, 3, 2] $

The answer to the first question is true because $ l = 1 $, $ r = 2 $, $ p = 2 $, $ a_p = 2 $, and $ \max(a_1, a_2) = \max(1, 5) = 5 $. Hence, $ a_2 = \max(a_1, a_2) $. Thus, the character to be displayed is $ 1 $.

The answer to the second question is false because $ l = 1 $, $ r = 2 $, $ p = 2 $, $ a_p = 1 $, but $ \max(a_1, a_2) = 5 \neq a_1 $. Thus, the character to be displayed is $ 0 $.

The answer to the fifth question is true because $ l = 2 $, $ r = 4 $, $ p = 3 $, and $ a_p = a_3 $ equals $ \max(a_2, a_3, a_4) = \max(5, 5, 2) = 5 $. Thus, the character displayed at the fifth position is $ 1 $.

