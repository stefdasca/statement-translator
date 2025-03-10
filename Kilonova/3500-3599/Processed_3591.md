Certainly! Here is the translated competitive programming problem statement:

---

How old is your cat in human years? Your cat might be older than you think! A cat's first year of life is equivalent to $15$ human years, according to the Purina study. In the second year, cats age another nine human years, reaching the age of $24$ human years at their second birthday. Every year after that adds four years.

# Task

At the CatShow, $n$ cats are registered, and each must walk on one of the corridors $1$, $2$, $3$, $\\dots$, depending on the number of complete decades in human years that correspond to its age (**decade** = group of $10$). The cats walk all at once at the announced time, with some corridors possibly having multiple cats and other corridors potentially remaining empty.

# Input data

The input file `catshow.in` contains a number $n$ on the first line, representing the number of cats, and on the next line, $n$ natural numbers representing the age of each registered cat.

# Output data

The output file `catshow.out` will contain the number of the first corridor from which the parade will begin.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000$;
* The ages of the cats are realistic, expressed as non-zero natural numbers with a maximum of $2$ digits.

# Example

`catshow.in`
```
3
7 2 4
```

`catshow.out`
```
2
```

## Explanation

There are $3$ cats registered with ages $7$ years, $2$ years, and $4$ years.
- $7$ years of the cat signify $44$ years in human age ($15+9+4+4+4+4+4$), meaning four complete decades, and it will parade on corridor $4$;
- $2$ years of the cat signify $24$ years in human age ($15+9$), meaning two complete decades, and it will parade on corridor $2$;
- $4$ years of the cat signify $32$ years in human age ($15+9+4+4$), meaning $3$ complete decades, and it will parade on corridor $3$.

Thus, the parade will take place on corridors $2$, $3$, $4$, with the first corridor from which the parade starts being $2$, while the rest of the corridors $1$, $5$, $6$, $\\dots$ remain unoccupied.

--- 

Please review and let me know if there are any further changes needed!