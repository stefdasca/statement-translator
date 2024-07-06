Sure, here is the translation of the given competitive programming problem statement from Romanian to English:

---

For obtaining the Philosopher's Stone, an alchemist prepared an elixir using a crucible with capacity $C$, into which he poured drops of molten metal in a well-established order, in $N$ stages. The number of drops poured in a stage is between 0 and $C-1$, and the process starts when the first drop is poured into the crucible (in the first stage the number of drops poured is non-zero). Drops accumulate in the crucible one by one, and every time it fills up completely, the alchemist utters a magic formula, causing the entire content to transform into a single drop, then continues the process. A recipe for obtaining the elixir is expressed as a sequence of $N$ numbers, representing the number of drops poured in the $N$ stages.

For example, applying the recipe $5 \ 6 \ 1 \ 0$, with a crucible of capacity $C = 7$, in the $N = 4$ stages the process is:
- stage 1: pour $5$ drops;
- stage 2: pour $6$ drops, as follows: after the first $2$ drops, the crucible is filled ($5 + 2 = 7$) and thus the magic formula is uttered, leaving one drop in the crucible; continue with the remaining $4$ drops; at the end of the stage, there are $5$ drops in the crucible ($1 + 4 = 5$);
- stage 3: pour one drop; at the end of the stage, there are $6$ drops in the crucible ($5 + 1 = 6$);
- stage 4: pour $0$ drops; after the last stage, the crucible contains $6$ drops ($6 + 0 = 6$).

$$ $$

A recipe that corresponds to the Philosopher's Stone must lead, at the end of its application, to obtaining **a single drop**, the quintessence of the mixed metals. Of course, there are multiple such recipes.

Being a responsible person, the alchemist left behind a set of treatises that include all these recipes. He wrote one recipe on each page, so that none of them is repeated throughout the entire work. Back then, there were skilled craftsmen who made appropriately sized treatises, so that each page could contain one recipe like ours, no matter how long it is. Each treatise has $P$ pages, and only after completing all $P$ pages of a treatise does the alchemist start a new treatise.

# Task
Determine the number of recipes published in the last treatise.

# Input data
The file `magic.in` contains on the first line, in this order, the natural numbers $C$, $N$, $P$, separated by a space and having the meaning from the statement.

# Output data
The file `magic.out` contains a natural number representing the number of recipes published in the last treatise.

# Constraints and clarifications
- $1 \le C, P \le 10^7$, $2 \le N \le 10^7$ natural numbers;
- for $30\%$ of the tests, $C \le 10$ and $N < 10$, and for $70\%$ of the tests, $N \le 10^4$.

# Example
`magic.in`
```
4 2 3
```
`magic.out`
```
1
```

## Explanation
The crucible has a capacity of $C = 4$, there are $N = 2$ stages of applying each recipe, the treatises have $P = 3$ pages. The recipes applied in two stages, after each such process leaving a single drop in the crucible, are: $1 \ 0$; $1 \ 3$; $3 \ 1$; $2 \ 2$. For these, two treatises are needed, with the first containing three recipes, and the second (the last) **one** recipe.

