
~[Tarzan.jpg|align=right|width=15%]

Tarzan, our favorite hero from the African jungle, felt the need for a new challenge: Australia. Arriving on the continent of kangaroos, he was filled with anxiety at the sight of the natural disaster caused by fires. The jungle no longer has vines! Desperate, he was put in contact, through Jane, with the *Association of Mystic Trees of Wise Australia*, which offers him the possibility to rebuild his precious jungle, but obviously, in exchange for a price.

In the *Association's* records, there are $N$ trees for Tarzan's jungle, numbered from $1$ to $N$, each labeled with 2 values, $A$ and $B$. When creating a vine between 2 trees $i$ and $j$, Tarzan must pay a cost equal to $A_i \cdot A_j + B_i + B_j$. 
Tarzan, being less skilled in calculations, needs your help to carry out his plans! Knowing somewhat that money has value in today's society (Jane tried to explain while he and a gorilla were washing each other), he asks you to present him the minimum cost scheme for hanging the vines that would allow him to swing from any tree to any other tree (possibly using intermediary trees)!

# Task

Given $N$ and the two arrays $A$ and $B$, find the minimum cost to complete the jungle.

# Input data

The first line contains the natural number $N$ with the significance from the statement. The next 2 lines contain the elements of array $A$, and respectively the elements of array $B$.

# Output data

The first line contains the minimum cost of reassembling Tarzan's jungle.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* $1 \leq A_i \leq 10^6$, for any $1 \leq i \leq N$;
* $1 \leq B_i \leq 10^{12}$, for any $1 \leq i \leq N$;

|# | Points | Constraints|
| - | - | ------------|
|1|7|$N \leq 1 \ 000$|
|2|14|$N \leq 10 \ 000$|
|3|18|In the array $A$ there are a maximum of $100$ different numbers.|
|4|14|The tests are generated randomly.|
|5|47|Without additional constraints.|

# Example

`stdin`
```
5
7 9 6 7 5
14 13 15 9 100
```

`stdout`
```
363
```

## Explanation

We can construct the vines: $(1, 3)$, $(2, 3)$, $(3, 4)$, $(4, 5)$
```

