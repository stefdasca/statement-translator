
# Task

In a distant realm called Numeronia, lived two magical beings: $X$ and $Y$. Each was composed of a unique string of symbols and resided in its own domain: $X$ in the _Base $X$_ realm and $Y$ in the _Base $Y$_ realm. It was said that the beings of Numeronia had a special connection called _Basic Attraction_.

For two beings to attract each other, they needed to meet in a common place – a realm represented by the smaller value of their domains, named $BazaXY$. There, they would reveal their essences (their symbols converted into the same base). If at least one symbol was common, their attraction would become reality.

One day, a wise sage from Numeronia was tasked to find out whether $X$ and $Y$ attract each other or not. With patience, he brought both of them to the $BazaXY$ realm, analyzed their symbols, and discovered the secret of their relationship. Will $X$ and $Y$ become allies in Numeronia, or will they go their separate ways? The answer lay hidden in their digits...

# Input data

The first line of the file `bazaxy.in` contains two natural numbers $bx$ and $by$, where $bx$ represents the numeral base in which the number $X$ is represented, and $by$ the numeral base in which the number $Y$ is represented. The second line of the file contains the numbers $X$ and $Y$, separated by a space.

# Output data

In the file `bazaxy.out`, on the first line, print the common digit, if the two numbers attract each other, or the value $-1$, otherwise. On the second line, print, in this order, separated by a space, the values $X$ and $Y$ converted to $BazaXY$, regardless of whether they attract each other or not.

# Constraints and clarifications

* $2 \leq bx, by \leq 10$;
* the numbers $X$ and $Y$ do not exceed 18 digits, regardless of the base in which they are represented
* if $X$ and $Y$ have multiple common digits when converted into $BazaXY$, the smallest of these digits will be printed
* for 31 points, $bx = by$
* for 20 points, $bx=by=10$

# Example 1

`bazaxy.in`

```
10 8 
23 57
```

`bazaxy.out`

```
7
27 57
```

## Explanation

The smallest base from the two given is $8$, the numbers represented in base $8$ are $27$ and $57$.

# Example 2

`bazaxy.in`

```
7 9 
34 56
```

`bazaxy.out`

```
-1 
34 102
```

## Explanation

The smallest base from the two given is $7$, the numbers represented in base $7$ are $34$ and $102$.
