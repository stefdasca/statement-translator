Certainly! Here is the translated problem statement:

---

> -- Can you write to my husband that the children have come to eat?
> -- Sure, but how many children are there?
> -- 4, why?
> -- Well, so I know how many "i"s to put.

We define the common noun "gigel" with a masculine gender (one gigel, two gigei), representing a child named Gigel who is 7 years, 4 months, and 16 days old.

In the park, there are exactly $N$ gigei, specifically $gigel_1, gigel_2, \dots, gigel_N$. They are with their mothers ($mama_1, mama_2, \dots, mama_N$). Each $mama_i$ intends for $gigel_i$ to stay in the park from moment $st_i$ to moment $dr_i$.

However, the mothers have a very peculiar habit, not understood by anyone. At each moment $t$, if $t$ is a prime number and $gigel_i$ is in the park, $mama_i$ will let him stay one more minute (in other words, $dr_i$ increases by $1$).

At each moment $t$, the *gigela effect* has a *gravity* $x$, where $x$ represents the number of gigei in the park at moment $t$.

The world is a simulation from moment $1$ to moment $T$, and you are an employee of those who control it (Gigelsoft). Your task is to monitor the gigela effects.

# Task

To verify if you have worked or not, the company Gigelsoft asks you, for certain moments in time, what was the maximum gravity of a gigela effect from the start of the simulation up to that moment in time.

# Input data

The first line of the input file `substantiv.in` contains three natural numbers, $N$, $T$, and $Q$. On the following $N$ lines, there are two natural numbers $st_i$ and $dr_i$, with the meaning explained in the statement. On the next line, there are $Q$ numbers, representing the moments in time for which you are asked.

# Output data

On the $Q$ lines of the output file `substantiv.out`, there will be a natural number on each line representing the answers to the questions.

# Constraints and clarifications

* $1 \leq N \leq 200 \ 000$
* $1 \leq Q \leq 1 \ 000 \ 000$
* We will consider that $st_i$ and $dr_i$ are the final ones.
* $1 \leq st_i \leq dr_i \leq T \leq 1 \ 000 \ 000$
* $1 \leq t \leq T$, where $t$ is the value given in a question.
* We denote by $\sum t$ the sum of $t$ values from the questions.

| # | Points | Restrictions |
| - | ------- | ------------ |
| 1 | 8 | $N \leq 100, dr_i - st_i \leq 100, \sum t \leq 10 \ 000 \ 000$ |
| 2 | 8 | $N \leq 100, dr_i - st_i \leq 100$ |
| 3 | 8 | $N \leq 3 \ 000, dr_i - st_i \leq 3 \ 000, \sum t \leq 10 \ 000 \ 000$ |
| 4 | 12 | $N \leq 3 \ 000, dr_i - st_i \leq 3 \ 000$ |
| 4 | 64 | Without other restrictions |

# Example

`substantiv.in`
```
5 30 3
2 6
5 10
3 8
12 14
3 12
4 18 12
```

`substantiv.out`
```
3
4
4
```

## Explanation

These are the time intervals when the gigei will stay in the park:

1. from $2$ to $10$
2. from $5$ to $14$
3. from $3$ to $12$
4. from $12$ to $15$
5. from $3$ to $18$