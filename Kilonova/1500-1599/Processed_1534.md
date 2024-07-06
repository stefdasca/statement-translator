Sure, here is the translated text:

---

The Xoni Resort on Ixos Island has $N$ ice cream shops, arranged next to each other on the same side of the pedestrian street. They are numbered with natural numbers from $1$ to $N$, in the order of their arrangement on the street.

The shops are owned by $K$ shareholders (numbered from $1$ to $K$), each owning some consecutively numbered shops. A shop can have multiple shareholders.

With the arrival of summer, the holiday season begins, and all shareholders take their vacation together for $M$ days. Before leaving for vacation, they discussed with Transportel to take care of the supply of ice cream to their shops. He decided, on his own, to supply some shops with ice cream on each of the $M$ days, which are also numbered consecutively.

# Task
Determine for each shareholder the number of shops owned by them that were not supplied with ice cream on any day during the vacation.

# Input data

The first line of the `viitor.in` file contains three natural numbers $N$, $M$, and $K$ separated by a space, with the above meaning. Each of the next $M$ lines contains two natural numbers $x$ and $y$, separated by a space. The numbers $x y$ on the $i$-th line among the $M$ mean that on day $i$ all shops numbered $x, x+1, \\dots, y$ are supplied with ice cream. Each of the next $K$ lines contains two natural numbers $a$ and $b$, separated by a space. The numbers $a b$ on the $i$-th line among the $K$ mean that shareholder $i$ owns the shops numbered $a, a+1, a+2, \\dots, b$.

# Output data

The `viitor.out` file will contain $K$ lines. The $i$-th line contains the number of shops owned by shareholder $i$ that were not supplied with ice cream on any day during the vacation.

# Constraints and clarifications

* $1 \\leq N \\leq 2 \\ 000 \\ 000 \\ 000$
* $1 \\leq M \\leq 100 \\ 000$
* $1 \\leq K \\leq 100 \\ 000$
* For tests worth 30 points, $1 \\leq N, M, K \\leq 1 \\ 000.$
* $1 \\leq x \\leq y \\leq N, 1 \\leq a \\leq b \\leq N$
* It is guaranteed that each of the $N$ shops has at least one shareholder.
* Being very far in the future, we observe that people live longer, move faster, but also have longer vacations.

# Example 

`viitor.in`
```
10 3 2
1 4
9 10
3 6
1 7
4 10
```

`viitor.out`
```
1
2
```

## Explanation

Shop $7$ was not supplied on any day, being the only one among those owned by the first shareholder that did not receive ice cream on any day. Among the shops owned by the second shareholder, those numbered $7$ and $8$ do not receive ice cream on any day.

---

Please double-check for any potential grammar or syntax errors according to the rules of the English language.