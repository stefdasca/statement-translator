~[pirati.jpg|align=right|width=auto]
The Pirates of the Caribbean crew has plotted a new adventure! Captain Jack finds himself caught in a scheme that will fully test his skills and intelligence. Because he owes a blood debt to the legendary Davey Jones, captain of the ghost ship The Flying Dutchman, he is forced to give him part of his latest diamond loot. The diamonds are stored in chests and must be very well guarded until Jack pays off his debt. He decides that each chest should be guarded by two pirates and organizes his crew as follows:
* pirates who will form **rows**;
* pirates arranged in **circular formations**.

In both cases, **a chest will be placed between any two adjacent pirates**. When Davey Jones' ship docks ashore, he asks Jack to pay off his debt as follows: 
"Choose $N$ of your pirates. They will load aboard all the chests guarded **only** by them. Make sure the number of chests is the largest possible!"

# Task

Knowing the number of pirates and their mode of organization in formations, write a program to determine the **maximum number** of chests that can be loaded onto the ship by those $N$ selected pirates.

# Input data

From the file `pirati.in` read:
* the first line contains three natural numbers $N$, $C$, and $R$ separated by spaces. $N$ represents the number of pirates that must be chosen to transport the chests to Jones' ship, $C$ represents the number of circular formations, and $R$ represents the number of rows;
* the second line contains $C$ natural numbers from the range $[2,250]$. The $K$-th number represents the number of pirates guarding the chests in the $K$-th circular formation;
* the third line contains $R$ natural numbers from the range $[2,250]$. The $K$-th number represents the number of pirates guarding the chests in the $K$-th row.

# Output data

The output file `pirati.out` will contain on the first line a single value that represents the maximum number of chests that can be loaded onto the ship by the $N$ pirates.

# Constraints and clarifications

* $2 \leq N \leq 50 \ 000$;
* $1 \leq C, R \leq 1 \ 000$;
* $N$ is less than or equal to the total number of pirates organized to guard the chests;
* It is not necessary to use complete formations for transporting the chests onto the ship.

# Example

`pirati.in`
```
6 1 2
4
2 3
```

`pirati.out`
```
5
```

## Explanation

We need to choose $6$ pirates to transport the chests onto the ship. The pirates are arranged in a single circular formation with $4$ pirates and two rows. The first row consists of $2$ pirates, and the second row consists of $3$ pirates. All $4$ pirates in the circular formation will be chosen. They will load $4$ chests. Additionally, $2$ more adjacent pirates will be chosen from any row. They will load $1$ chest. The maximum number of chests loaded onto the ship is $5$.