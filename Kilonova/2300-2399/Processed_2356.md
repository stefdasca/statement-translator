Gaby is an enthusiast and bird lover, especially of canaries. She has decided to become a promoter for those who prefer a symphony that elevates the soul. Having experience in organizing exhibitions, she plans to organize in 2024 the first exhibition of roller song canary breeders in Suceava, under the aegis of the central association SV EXOTICOS. Gaby rented a space in which she can exhibit $N$ stands with canary cages. The stands will be located along a straight line at positions $x_1$, $x_2$, ..., $x_N$.

The canaries, in number $C$, are picky and can become agitated. To prevent unnecessary agitation of the small birds and to avoid injuries, the entrepreneur Gaby wants to allocate the canary cages on the stands so that the minimum distance between any two of them is as large as possible.

# Task

Determine the largest minimum distance.

# Input data

The first line of the file `canari.in` contains $N$ - which represents the number of stands and $C$ the number of canaries, and the second line contains $x_1$, $x_2$, ... $x_N$ the $N$ numbers representing the positions where the cages will be placed.

# Output data

The first line of the file `canari.out` will contain the maximum of the minimum distance.

# Constraints and clarifications

- $2 \leq N \leq 10^5$;
- $2 \leq C \leq N$;
- $0 \leq x_i \leq 10^9$.

# Example 1

`canari.in`
```
4 3
2
8
16
4
```

`canari.out`
```
6
```

## Explanation

Initially, the possible minimum would be $2$ placing the cages at positions $2$, $4$, and $8$. However, Gaby can improve this minimum if she places the 3 canaries in the cages at positions $2$, $8$, and $16$, resulting in a maximum minimum distance of $6$.

# Example 2

`canari.in`
```
4 3
1
5
2
4
```

`canari.out`
```
1
```

## Explanation

Initially, Gaby could place the 3 canaries in cages at positions $1$, $2$, and $4$ resulting in a minimum distance of $1$. Even if she changes the positions to $1$, $4$, and $5$, the minimum distance cannot be improved.