The Oasis Lacotrop in Etpas desert is surrounded by $n$ orange trees, all bearing fruits, arranged in a circle and numbered from $1$ to $n$, in a clockwise direction. The monkey Gino starts from an orange tree $m$ and always counts, in a clockwise direction, $k$ orange trees that bear fruits. He picks all the fruits from the orange tree at position $k$. He continues counting starting from the next orange tree that still has fruits. In the end, there remains only one unpicked orange tree $p$, where Gino makes his shelter.

# Task

Which orange tree $m$ should Gino start counting from so that he ends up making his shelter in exactly the orange tree $p$?

# Input data

The file `portocal.in` contains a single line, the numbers $n$, $k$ and $p$, separated by a space, in the format: $n \\ k \\ p$.

# Output data

The file `portocal.out` contains on the first line the natural number $m$, representing the orange tree from which Gino starts counting.

# Constraints and clarifications

* $2 \\leq n \\leq 1 \\ 000$;
* $1 \\leq k \\leq 10 \\ 000$;
* $1 \\leq p \\leq 1 \\ 000$; 

# Example 1

`portocal.in`
```
6 8 5
```

`portocal.out`
```
3
```