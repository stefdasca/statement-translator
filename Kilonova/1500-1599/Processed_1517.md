```markdown
~[img1.JPG|align=right|width=auto]
The 100 meters flat race is one of the most popular and prestigious events in any athletics competition. The current world record for this event is held by Jamaican athlete Usain Bolt with a time of $9.58$ seconds.

Sometimes the competition between athletes is so close that the differentiation between them can only be made with the help of cameras that capture the finish line. There have been cases when two or more athletes were declared tied.

# Task

Considering $N$ athletes, participating in a 100-meter flat race, identified by numbers $1, 2, \ldots, N$, write a program to determine the number $P$ of distinct rankings that can be obtained after the race is finished. For example, for $N = 2$, there can be $3$ distinct rankings: $(1, 2), (2, 1), (1=2)$; where $(1=2)$ represents the situation when both athletes finish at the same time.

# Input data

The input file `100m.in` contains on the first line the natural number $N$, with the above meaning.

# Output data

The output file `100m.out` will contain on the first line the remainder of the division of the number $P$ by $666\ 013$.

# Constraints and clarifications

- $2 \leq N \leq 5\ 000;$
- Two rankings are considered distinct if they differ by at least one position;
- For tests worth $32$ points $N \leq 500$.

# Example 1

`100m.in`
```
3
```

`100m.out`
```
13
```

## Explanation

$N = 3$ athletes.

Numbering the athletes as $1$, $2$ and $3$ there are $13$ distinct rankings: $(1, 2, 3)$; $(1, 3, 2)$; $(2, 1, 3)$; $(2, 3, 1)$; $(3, 1, 2)$; $(3, 2, 1)$; $(1, (2=3))$; $(2, (1=3))$; $(3, (1=2))$; $((2=3), 1)$; $((1=3), 2)$; $((1=2), 3)$; $(1=2=3)$.

By $(i=j)$ we noted the possibility that athletes $i$ and $j$ finish the race at the same time. By $(i=j=k)$ we noted the possibility that athletes $i, j$ and $k$ finish the race at the same time.

# Example 2

`100m.in`
```
1771
```

`100m.out`
```
74140
```

## Explanation

$N = 1\ 771$ athletes.

The number of distinct rankings in which the athletes can finish the race, modulo $666\ 013$, is $74\ 140$
```

I have translated the problem statement from Romanian to English, adhering to your given instructions. If you find any issues, please let me know!