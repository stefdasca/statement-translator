Sure, here is the translated text:

---

An **FFT** graph *of order* $F$ is a directed **graph** with $F$ *levels*, numbered from $0$ to $F - 1$. Each level is composed of $2^{F - 1}$ nodes, numbered from $0$ to $2^{F - 1} - 1$. We will use the notation $(h, x)$ to refer to the node with index $x$ on level $h$.

The edges of the **FFT** graph are as follows:
1. All **directed** edges from $(h, x)$ to $(h + 1, x)$;
2. All **directed** edges from $(h, x)$ to $(h + 1, x \oplus 2^{F - h - 2})$.

Initially, all nodes of the graph were colored white by *Stiuboss*. Out of anger, *Nustiuboss* selected $T$ nodes which he colored black. (See figure)

~[fft2d.png]

Intrigued by the changes made, *Nusdeaici* decided to calculate the number of pairs $(a, b)$ with the property that there exists at least one *directed* path from node $(0, a)$ to node $(F - 1, b)$ that does not pass through any black node.

# Task
The input file `fft2d.in` will contain on the first line two natural numbers $F$ and $T$. The next $T$ lines will contain one pair $(h, x)$ each, representing that the node on level $h$ with index $x$ is colored black.

# Input data
The input file `fft2d.in` will contain on the first line two natural numbers $F$ and $T$. The next $T$ lines contain one pair $(h, x)$ each, indicating that the node on level $h$ with index $x$ is colored black.

# Output data
The output file `fft2d.out` will contain a single natural number representing the number of pairs $(a, b)$ with the property that there exists at least one **directed** path from node $(0, a)$ to node $(F - 1, b)$ that does not pass through any black node.

# Constraints and clarifications
* $1 \leq F \leq 30$
* $1 \leq T \leq 100\, 000$
* $A \oplus B$ represents the exclusive OR operation on bits (xor).
* **ATTENTION! The edges are directed (although they are not represented as such in the figure).**
* "Apam, what shall we name the main character?" Answer: "Nustiuboss".
* For tests worth $10$ points, $F \leq 10$
* For other tests worth $10$ points, $F \leq 16$
* For other tests worth $30$ points, $T \leq 2\, 000$

# Example 1
`fft2d.in`
```
3 3
0 2
1 1
2 3
```

`fft2d.out`
```
5
```

## Explanation

There are $5$ pairs $(a, b)$ with the above-mentioned property. More precisely, these are: $(0, 0)$, $(0, 1)$, $(0, 2)$, $(1, 2)$, $(3, 2)$.

# Example 2

`fft2d.in`
```
4 3
0 1
1 1
2 4
```

`fft2d.out`
```
44 
```

## Explanation

There are $44$ pairs $(a, b)$ with the above-mentioned property. The figure above corresponds to this example.

# Example 3

`fft2d.in`
```
15 10
3 12914
8 10479
12 1039
8 13597
11 2633
12 10668
12 6769
11 4443
7 15697
12 13418
```

`fft2d.out`
```
268271648
```

## Explanation

You'll have to take our word for it.

---

Please let me know if you need anything else!