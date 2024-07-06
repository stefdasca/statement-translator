Here's the translated competitive programming problem statement:

---

Poli has $N$ colleagues at the university. Some of Poli's colleagues can be friends with each other, under the following conditions:

* if person $x$ is friends with person $y$, then person $y$ is also friends with person $x$;
* if person $x$ is friends with person $y$ and person $y$ is friends with person $z$ then person $x$ is friends with person $z$;
* a person is always friends with themselves.

We define a friendship relationship as the set of friendships formed among the $N$ colleagues.

Poli went around the university and managed to obtain from each person **at most** one piece of information about someone with whom that person is **not** friends. Knowing the number of Poli's colleagues and the information he obtained, determine how many distinct friendship relationships can be formed that respect the obtained information. A friendship relationship is considered different from another if there is a pair $(x, y)$ such that in the first relationship $x$ is friends with $y$, and in the second relationship $x$ is not friends with $y$.

# Task

Write a program that calculates the total number of possible friendship relationships.

# Input data

The file `prietenie.in` contains on the first line $N$ and $M$, the number of colleagues and the number of pieces of information Poli obtained, respectively. The next $M$ lines contain two numbers $(x, y)$ representing that $x$ is not friends with $y$.

# Output data

The file `prietenie.out` contains on its single line the total number of possible friendship relationships modulo $31 \ 333$.

# Constraints and clarifications

* $1 \leq N \leq 5 \ 000$
* $0 \leq M \leq \frac{N}{2}$
* $1 \leq x, y \leq N$
* Let there be two pairs $(x, y)$ and $(a, b)$ among the $M$. Then $x$, $y$, $a$, $b$ are distinct two by two.

# Example

`prietenie.in`
```
3 1
1 3
```

`prietenie.out`
```
3
```

## Explanation

The $3$ variations are:

* no one is friends with anyone;
* $1$ is friends with $2$;
* $2$ is friends with $3$.

---

Please double check for potential grammar and/or syntax errors.