Here's the translated problem statement in English:

---

Vila Elena, the main food supplier for Radu Greceanu high school, is facing a significant increase in demand for _grill at 7 lei_ with the implementation of the bench delivery service. To efficiently manage this increased order volume, a delivery scheduling algorithm has been developed.

In each break, a sequence of $N$ letters is randomly generated. The letters are sequentially assigned to each of the $C$ orders. For example, for $4$ orders and a sequence of $12$ letters, the first order will be associated with the letters at positions $1$, $5$, and $9$, the second order with the letters at positions $2$, $6$, and $10$, etc.

Deliveries are organized in groups based on the letters associated with the orders. Thus, all orders associated with the same multiset of letters (a set in which elements can appear multiple times, without considering the order) will be delivered together in the same shift. Moreover, order $1$ and the other orders with the same letters as order $1$ receive priority and are delivered in the initial stage of the planning.

# Task

Implement the delivery scheduling algorithm to provide the following data to the employees of Vila Elena:
* How many orders are prioritized?
* How many delivery shifts are needed?

# Input data

The first line of the input file `sorti.in` contains two natural numbers $N$ and $C$, representing the length of the letter sequence and the number of orders.

The second line contains a sequence of $N$ letters.

# Output data

The first line of the output file `sorti.out` will contain a single integer, the number of prioritized orders. The second line will contain the number of delivery shifts.

# Constraints and clarifications

* $ 1 \leq N \leq 200\ 000 $;
* Each order is associated with a maximum of $12$ letters;
* $N$ is a multiple of $C$;
* The letters associated with the orders are uppercase from `A` to `Z`;
* Correct answers to the first question are worth 30% of the problem's score.
* If you answer only one question, display `-1` on the respective line of the other question.

# Example

`sorti.in`
```
9 3
ABCCEDDQA
```

`sorti.out`
```
2
2
```

## Explanation

The three orders have the following associated letters: `ACD`, `BEQ`, `CDA`. The first and last orders have the same multiset of letters, so they are delivered with priority. There are two delivery shifts: for orders `ACD` and for those `BEQ`.

---

I have translated and reviewed the problem statement to ensure clarity and correct grammar following the rules of the English language.