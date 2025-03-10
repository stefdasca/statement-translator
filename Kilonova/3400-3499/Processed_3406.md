The given text has been translated into English while preserving the specified structures and formats.

---

We are given $n$ natural numbers, representing the IDs of $n$ players. Each ID is a natural number composed of $4$ digits, each digit having a meaning:

* The first digit represents the "Power" of the player. It can be between $1$ and $9$.
* The second digit represents the "Ammunition" of the player, which can be between $1$ and $9$.
* The third digit represents the "Superpower" of the player. It can be between $0$ and $2$, and a value of $2$ means the "Superpower" is activated.
* The fourth digit represents the "Hyperpower" of the player. It can be between $0$ and $3$, and a value of $3$ means the "Hyperpower" is activated.

Based on this ID, the players' final power is calculated as follows:
- Multiply the power by the ammunition.
- Add the superpower multiplied by $4$ (if the superpower is activated).
- Square the last obtained value (if the hyperpower is activated).

For example:
- For ID $6200$, the final power is $6 \cdot 2$, which is $12$ (neither the superpower nor the hyperpower is activated);
- For ID $4521$, the final power is $4 \cdot 5 + 2 \cdot 4$, which is $28$ (only the superpower is activated);
- For ID $5123$, the final power is $(5 \cdot 1 + 2 \cdot 4)^2$, which is $169$ (both the superpower and the hyperpower are activated).

The highest final power ensures winning the battle; there may be multiple winners.

# Task

Determine the ID of the first winner.

# Input data

Read from the input file `puteri.in` the number $n$ on the first line, then on the next line, the $n$ IDs of the players.

# Output data

Print in the output file `puteri.out` the ID of the first player who will win the battle, after calculating the final power of each of them.

# Constraints and clarifications

* $1 \le N \le 3 \cdot 10^5$;
* The ID is composed of $4$ digits, according to the rules in the statement.

# Example 1

`puteri.in`
```
3
9122 8922 9212
```

`puteri.out`
```
8922
```

## Explanation

ID $9122$ -> final power $17$, which is $(9 \cdot 1 + 2 \cdot 4)$  
ID $8921$ -> final power $80$, which is $(8 \cdot 9 + 2 \cdot 4)$  
ID $9212$ -> final power $18$, which is $(9 \cdot 2)$

# Example 2

`puteri.in`
```
6
3100 1223 1200 2123 2900 1123 
```

`puteri.out`
```
1223
```

## Explanation

ID $3100$ -> final power $3$, which is $1 \cdot 3$  
ID $1223$ -> final power $100$, which is $(1 \cdot 2 + 2 \cdot 4)^2$  
ID $1200$ -> final power $2$, which is $1 \cdot 2$  
ID $2133$ -> final power $100$, which is $(2 \cdot 1 + 2 \cdot 4)^2$  
ID $2900$ -> final power $18$, which is $2 \cdot 9$  
ID $1123$ -> final power $81$, which is $(1 \cdot 1 + 2 \cdot 4)^2$

# Example 3

`puteri.in`
```
4
4400 2810 8202 4411
```

`puteri.out`
```
4400
```

## Explanation

None of them have the Superpower or Hyperpower activated, so the final power is obtained by multiplying only the first $2$ digits, and the maximum value is $16$; all have this final power.