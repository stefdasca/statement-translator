Sure, here's the translation according to the specified instructions:

```markdown
We define a percentual price modification as a pair $(c, p)$ consisting of a character $c \in \{\text{‘+’, ‘-’}\}$ and a natural number $p$. If $c = \text{‘+’}$ then there is a price increase and if $c = \text{‘-’}$ then there is a price decrease, with the number $p$ representing the percent change in price. 
Examples of percentual price modifications:
* $(+ 35)$ – represents a price increase by $35\%$
* $(- 50)$ – represents a price decrease by $50\%$ 

An initial price can go through a sequence of $n$ percentual price modifications resulting in a final price. We define a **price cycle of length $n$** as a sequence of $n$ percentual price modifications where the **final price** is equal to the **initial price**. 

Examples of price cycles:
* of length $n=2$:  $(- 20)$, $(+ 25)$ 
* of length $n=3$: $(- 50)$, $(+ 25)$, $(+ 60)$ 

# Task
Write a program that reads a natural number $n$ and determines the **number of distinct price cycles of length n** that contain at least one known percentual price modification $(C, P)$.

# Input data

The input file `procente.in` contains on the first line the natural number $n$ and on the second line a character $C \in \{\text{‘+’, ‘-’}\}, followed by a natural number $P$, separated by a space, as described above. 

# Output data

The output file `procente.out` will contain the sought number on the first line.

# Constraints and clarifications

* $2 \leq n \leq 80$;
* $C \in \{\text{‘+’, ‘-’}\}$
* The value of the percentage $p$ in case of a price increase is between $0$ and $100$ inclusive.
* The value of the percentage $p$ in case of a price decrease is between $1$ and $99$ inclusive.
* Two percentual price modifications $(c_{1}, p_{1})$, $(c_{2}, p_{2})$ are different if $c_{1} \neq c_{2}$ or $p_{1} \neq p_{2}$.
* Two price cycles of length $n$ are distinct if they differ by at least one percentual price modification.
* Two price cycles of length $n$ that contain the same percentual modifications in a different order are identical.
* For $28\%$ of the score $n \leq 20$, for $60\%$ of the score $n \leq 40$, for $100\%$ of the score $n \leq 80$ 

# Example 1

`procente.in`
```
2
- 20
```

`procente.out`
```
1
```

## Explanation

There is only one sequence of $2$ percentual price modifications that includes a price decrease by $20\%$ resulting in the final price being equal to the initial price. This sequence is $(- 20)$, $(+ 25)$.

# Example 2

`procente.in`
```
3
+ 25
```

`procente.out`
```
4
```

## Explanation

There are four distinct sequences of $3$ percentual price modifications that include at least one price increase by $25\%$ resulting in the final price being equal to the initial price. These sequences are:  
* $(- 50)$, $(+ 25)$, $(+ 60)$  
* $(- 36)$, $(+ 25)$, $(+ 25)$  
* $(- 60)$, $(+ 25)$, $(+ 100)$
* $(- 20)$, $(+ 25)$, $(+ 0)$ 
```
