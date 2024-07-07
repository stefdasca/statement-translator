> *“Frații Buzești� National College* ~[logos.png|align=right|width=20rem]
> *Training Center for Excellence in Informatics*
> **InfoCNFB** - Second Edition, Juniors
> December 9, 2023

The astronauts from a cosmic research center have discovered a new galaxy, containing an infinite number of stars, which they have associated with the ordinal numbers $1, 2, 3, 4, \dots$. They wish to name each star and, to manage them more quickly, they thought to group adjacent stars into constellations so that each constellation $k$ consists of exactly $k$ stars (thus, constellation $1$ will have one star, constellation $2$ will have two stars, constellation $3$ will have three stars, and so on). This way, it will be easier to name the stars, because the name of a star will consist of the last digit of the position it occupies within its constellation, expressed in letters, immediately followed by a natural number representing the constellation number from which it belongs.

# Task

Given a nonzero natural number $n$, representing the $n$th star, display its name.

# Input data

The input file `constelatii.in` will contain the natural number $n$.

# Output data

The output file `constelatii.out` will contain the required result.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000 \ 000$;
* The name of a star will contain only lowercase English letters and digits from $0$ to $9$;
* The names of the digits are: `zero`, `unu`, `doi`, `trei`, `patru`, `cinci`, `sase`, `sapte`, `opt`, `noua`.

# Example 1

`constelatii.in`
```
12
```

`constelatii.out`
```
doi5
```

## Explanation

The stars will be grouped into constellations as follows:
* Constellation $1$: $1$
* Constellation $2$: $2 \ 3$
* Constellation $3$: $4 \ 5 \ 6$
* Constellation $4$: $7 \ 8 \ 9 \ 10$
* Constellation $5$: $11 \ 12 \ 13 \ 14 \ 15$
* Constellation $6$: $16 \ 17 \ 18 \ 19 \ 20 \ 21$

The 12th star is number $2$ within Constellation $5$.

# Example 2

`constelatii.in`
```
18
```

`constelatii.out`
```
trei6
```

## Explanation

The 18th star is number $3$ within Constellation $6$.