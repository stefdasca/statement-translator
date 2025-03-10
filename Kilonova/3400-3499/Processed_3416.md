The extraterrestrials from the planet Adarin have studied all $K$ stars in their galaxy. They have concluded that each star, after its death, will create a supernova. The extraterrestrials want to leave their planet before a supernova can destroy it.  
The galaxy where the extraterrestrials live is divided into sectors, represented as a matrix with $N$ rows and $M$ columns. Each sector in the galaxy corresponds to a position in this matrix. In the galaxy, planet Adarin is located in the sector with coordinates $N_a$ and $M_a$. Through their research, the extraterrestrials know the positions of all the stars in their galaxy, as well as the lifespan of each one. When a star dies, it creates a supernova. A supernova is defined as follows:
* In the year a star dies, the sector where it is located becomes dangerous.
* Each following year, the dangerous area extends to all sectors that share a side with a dangerous sector, and they become dangerous as well.

Example of a supernova evolution after a star's death:
~[supernova.png]

# Task

Write a program that solves the following two tasks:
1. The extraterrestrials have simulated the death of a star. Knowing that the star lives for $v$ years, they want to determine how many sectors become dangerous after $t$ years.
2. The coordinates of planet Adarin and the $K$ stars in the galaxy, as well as the lifespans of the stars, are given. Calculate the year in which planet Adarin will be destroyed.

# Input data

The input file `supernova.in` contains on the first line a value $cer$ which can be $1$ or $2$, depending on the task to be solved.  
For task $1$, on the second line of the input file there are two values $v$, representing the lifespan of the star, and $t$, representing a time interval.  
For task $2$, on the second line, there are values $K, N, M$ which represent the number of stars in the galaxy and the number of rows and columns of the galaxy respectively. On the third line of the input file, there are the values $N_a$ and $M_a$ which represent the coordinates of planet Adarin. On each of the lines from $4$ to $K + 3$ there are $3$ values $n, m$ and $T$ which represent the row, column of the sector where a star is located, and the lifespan of that star.

# Output data

For task $1$, the file `supernova.out` will contain the number of sectors in the galaxy that become dangerous after $t$ years.  
For task $2$, the file `supernova.out` will contain the year when planet Adarin will be destroyed by a supernova.

# Constraints and clarifications

* $1 \le t \le 10^9$;
* $1 \le v \le t$;
* $1 \le K \le 10^5$;
* $1 \le N, M \le 10^9$;
* $1 \le n, m, N_a, M_a \le N, M$;
* $1 \le T \le 10^9$.

| # |           Score          | Constraints |
|:-:|:-----------------------------:|:-------:|
| 1 |      15     |    $cer = 1; t \le 100$   |
| 2 |     15     |    $cer = 1; t \le 10^5$   |
| 3 |           20           |    $cer = 1$   |
| 4 | 20 |   $cer = 2; 1 \le K, N, M, T \le 100$    |
| 5 |           20           |   $cer = 2$    |

# Example 1

`supernova.in`
```
1
1 3
```

`supernova.out`
```
13
```

## Explanation

For the first example, the star dies in year $1$ creating $1$ dangerous sector, in year $2$ there will be $5$ dangerous sectors, and in year $3$ there will be $13$ dangerous sectors in total.

# Example 2

`supernova.in`
```
1
1337 31414
```

`supernova.out`
```
1809312013
```

# Example 3

`supernova.in`
```
2
1 10 10
5 5
5 5 1
```

`supernova.out`
```
1
```

## Explanation

The galaxy has $1$ star, $10$ rows and $10$ columns.  
Planet Adarin is located in the sector with coordinates $(5,5)$.  
The star is in the sector with coordinates $(5,5)$ and will die in Year $1$, destroying the planet in the same year.

# Example 4

`supernova.in`
```
2
4 100000 100000
69450 7266
45925 758 39310
3205 28284 57866
11199 45407 48522
38985 44310 14702
```

`supernova.out`
```
69343
