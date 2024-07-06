# Task

Balaurului Arhirel doesn't like unsorted strings very much. For this reason, he cannot tolerate permutations of $N$ elements, so he decides to sort them and invents his own sorting method for that.

Initially, he takes a string $S$ which represents a permutation of order $N$. He looks in the string $S$ for the smallest ($min$) and the largest element ($max$). Let's consider that $min$ is at position $p_{min}$ in the string $S$, and $max$ at position $p_{max}$. Let's denote by $x$ the minimum of $p_{min}$ and $p_{max}$, and by $y$ the maximum of $p_{min}$ and $p_{max}$. Thus, the string $S$ has been divided into three other strings, $S_1$, $S_2$, $S_3$, which can each have zero elements, one element, or more elements. String $S_1$ starts at the first position in the string and ends at position $x-1$. String $S_2$ starts at position $x+1$ and ends at position $y-1$. String $S_3$ starts at position $y+1$ and ends at the last position in the string.

Balaurului Arhirel moves the value $min$ to the left end of $S$, and the value $max$ to the right end of the string $S$ and resumes sorting for each of the strings $S_1$, $S_2$, $S_3$.

For example, let's consider $N = 6$ and the string $S = (3 \\ 4 \\ 2 \\ 1 \\ 6 \\ 5)$. In the first step, $min = 1$ and $max = 6$. Therefore, $S_1 = (3 \\ 4 \\ 2)$; $S_2 = ()$; $S_3 = (5)$. The $min$ and $max$ are moved to the ends of the string and we get $S = (1 \\ 3 \\ 4 \\ 2 \\ 5 \\ 6)$ and sort in the same way $S_1$, $S_2$, and $S_3$. $S_2$ and $S_3$ have $0$ and $1$ elements respectively, so they are already sorted. For $S_1$, we find $min = 2$ and $max = 4$ and we will have the strings $(3)$; (); (). $min$ and $max$ are moved to the ends and we get $S_1 = (2 \\ 3 \\ 4)$. Finally, we will have the string $S = (1 \\ 2 \\ 3 \\ 4 \\ 5 \\ 6)$. Obviously, this method will not always work for sorting a permutation.

For example, for the string $S = (3 \\ 4 \\ 1 \\ 6 \\ 5 \\ 2)$, we find $min = 1$ and $max = 6$, and $S_1 = (3 \\ 4)$, $S_2 = ()$, $S_3 = (5 \\ 2)$. The $min$ and $max$ are moved to the ends of $S$: $S = (1 \\ 3 \\ 4 \\ 5 \\ 2 \\ 6)$ and the sorting proceeds in turn for the strings $S_1$, $S_2$, $S_3$. $S_1$ is sorted, $S_2$ has no elements, and $S_3$ will become $S_3 = (2 \\ 5)$. Finally, $S = (1 \\ 3 \\ 4 \\ 2 \\ 5 \\ 6)$.

# Task

Help Balaurului Arhirel to find out how many of the permutations of $N$ elements can be sorted by his method.

# Input data

The file `sortari.in` contains a single line which contains the number $N$.

# Output data

The file `sortari.out` will contain a single line which contains the number of permutations of order $N$ that can be sorted using Balaurului's method, modulo $19\, 573$ (the remainder of the number of permutations when divided by $19\, 573$).

# Constraints and clarifications

* $0 < N < 201$;

# Example 1

`sortari.in`
```
4
```

`sortari.out`
```
18
```

## Explanation

In the case of permutations of $4$ elements, the strings $(1 \\ 3 \\ 4 \\ 2)$; $(3 \\ 1 \\ 2 \\ 4)$; $(3 \\ 1 \\ 4 \\ 2)$; $(3 \\ 4 \\ 1 \\ 2)$; $(3 \\ 4 \\ 2 \\ 1)$; $(4 \\ 3 \\ 1 \\ 2)$ cannot be sorted in ascending order. The other $24 - 6 = 18$ permutations can be sorted in ascending order. For example, for the string $(1 \\ 3 \\ 4 \\ 2)$, after finding $min = 1$, $max = 4$, you get the strings: $S_1 = ()$; $S_2 = (3)$; $S_3 = (2)$, which, having one element each, are sorted. Thus, after moving $min$ and $max$ to the ends, we will have: $(1 \\ 3 \\ 2 \\ 4)$.

