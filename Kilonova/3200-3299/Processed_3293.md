
# Task
Working at McDonald's has become a little more difficult recently. Donald Pump, the famous American, has recently started working at a McDonald's in Texas. He is given a pile of $N$ chicken nuggets, which he arranges with care next to each other. Each nugget is characterized by a weight $G$, and a beauty $F$, both expressed as two natural numbers. As usual, American citizens demand food and are very picky. D. Pump asks you to find a subset of nuggets as quickly as possible such that the sum of their beauties is maximized, and the sum of the weights does not exceed a given value $G$. (since Pump is a serious man and doesn't want to be too generous with the citizens).

~[img0.png|align=right|width=30%]

# Input data

The first line of the file `mcdonalds.in` will contain the values $N$ and $G$, with the meaning from the statement. On the next $N$ lines, there will be pairs of values $G_i$ and $F_i$, representing the weight and the beauty of the nugget with index $i$.

# Output data

The first line of the file `mcdonalds.out` will print a single value $F_{\text{max}}$, the maximum beauty that can be obtained according to the problem's task.

# Constraints and clarifications

* $2 \leq N \leq 5 \ 000$
* $1 \leq G \leq 10 \ 000$
* $1 \leq G_i, F_i \leq 10 \ 000$
* $F_{\text{max}} \leq G$

# Example 1

`mcdonalds.in`
```
5 8
2 6
3 5
4 7
1 3
5 9
```

`mcdonalds.out`
```
18
```

## Explanation

D. Pump takes the nuggets with indices $1$, $4$, and $5$, whose total weight is $8$. They have a total beauty sum of $6 + 3 + 9 = 18$.

# Example 2

`mcdonalds.in`
```
3 7
4 1
2 2
1 6
```

`mcdonalds.out`
```
9
```

## Explanation
In this case, D. Pump takes all the nuggets, as the sum of the weights is exactly $7$. They have a total beauty sum of $1 + 2 + 6 = 9$.
