An institute of history collects objects discovered at multiple archaeological sites. For each discovery at a site, the category of the object (e.g., pottery, coin, etc.), the material from which it is crafted, and the number of specimens that belong to the same category and material are determined. The category and material of an object are represented by non-zero natural numbers.

For each site, the total number of values sent to the institute is known, grouped into sequences formed of $2$ or $3$ non-zero natural numbers followed by a negative number (which marks the end of a sequence). Each such sequence encodes the data of a discovery. The first number in a sequence represents the category of the discovered object, the second number represents the material from which the object is crafted, and the third number indicates the number of specimens discovered in that operation. If the sequence only has $2$ positive numbers, then a single specimen of that object was discovered. For example, the sequence of numbers $3$, $7$, $4$, $-2$ will represent a discovery of $4$ specimens in category $3$, crafted from material $7$ (category $3$ could be coins, material $7$ could be bronze, and there are $4$ specimens discovered: thus $4$ bronze coins were discovered).

# Task

Write a program that determines and displays, for the data sent by $n$ sites to the institute:
1. The list of objects in increasing order by category: the category and the total number of specimens discovered at all sites in that category will be displayed.
2. The list of objects discovered in increasing order by category: for each object, the category, material, and number of specimens discovered, having these characteristics, will be displayed.

# Input data

The input file `institut.in` contains on the first line two natural numbers $c$ and $n$: $c$ represents the task and has one of the values $1$ or $2$, and $n$ represents the number of archaeological sites.

Each of the following $n$ lines in the file contains a sequence of integers, separated by space, which represents the data sent by a site, in the following order: total number of values, sequences formed of $2$ or $3$ non-zero natural numbers followed by a negative number, which encodes the discovery made: the category, material, and the number of specimens with these characteristics for the discovered objects.

# Output data

The output file `institut.out` will contain:
1. If $c = 1$, the output file `institut.out` will contain on each line two natural numbers, separated by a space, which represent the category and the total number of specimens discovered in that category on all sites, in increasing order of the categories.
2. If $c = 2$, the output file `institut.out` will contain on the first line a natural number $d$, representing the total number of discoveries from all sites, and on each of the following $d$ lines three natural numbers, separated by space, which represent in this order: the category of the discovered object, the material of the object, and the number of specimens discovered. The $d$ lines will be displayed in increasing order of the object categories and for objects of the same category, in increasing order of the material.

# Constraints and clarifications

* $4 \leq n \leq 400$;
* The category, material, and number of specimens of an object are non-zero natural numbers with at most $2$ digits.
* The total number of values transmitted by a site to the institute is at most $600$;
* The number of discoveries from all sites is at most $10 \ 000$.
* For the test data, it is assumed that the objects of any two different discoveries do not have the same category and the same material.
* For solving task $1$, a maximum of $40$ points can be obtained, for task $2$, a maximum of $50$ points can be obtained.

# Example 1

`institut.in`
```
1 4  
10 1 6 -5 7 2 -8 2 10 3 -4 
10 2 5 -7 2 6 2 -4 1 5 -7 
6 3 8 -6 7 5 -1  
4 2 1 5 -6
```

`institut.out`
```
1 2 
2 11 
3 1 
7 2
```

## Explanation

There are $4$ archaeological sites, for each the number of values sent is known: for the first site, there are $10$ values, with the following sequences representing discoveries made:
- Sequence $(1,6,-5)$ represents category $1$, material $6$, $1$ specimen;
- Sequence $(7,2, -8)$ represents category $7$, material $2$, $1$ specimen;
- Sequence $(2,10,3,-4)$ represents category $2$, material $10$, $3$ specimens, etc.

Objects discovered from all sites are displayed by category, in increasing order of categories:
- There are $2$ specimens in category $1$,
- $11$ specimens in category $2$: $(2,10,3, -4)$, $(2,5,-7)$, $(2,6,2,-4)$, $(2,1,5,-6)$,
- $1$ specimen in category $3$
- $2$ specimens in category $7$.

# Example 2

`institut.in`
```
2 4  
10 1 6 -5 7 2 -8 2 10 3 -4 
10 2 5 -7 2 6 2 -4 1 5 -7 
6 3 8 -6 7 5 -1  
4 2 1 7 -6
```

`institut.out`
```
9 
1 5 1 
1 6 1 
2 1 7 
2 5 1 
2 6 2 
2 10 3 
3 8 1 
7 2 1 
7 5 1
```

## Explanation

There are $9$ object discoveries, which are displayed by categories in increasing order: at the same category, they are displayed by material in increasing order.