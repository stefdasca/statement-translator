Bob is going on vacation to the Volcano Island where there are $N$ volcanoes, positioned from $1$ to $N$. Each volcano has a known height, $H$, which is a positive number for volcanoes of type $1$, which are on the ground, and a negative number for volcanoes of type $2$, which are underground. A volcano is called special if there is no volcano of the same type, located at a higher position than its own, for which the absolute value of its height is greater than or equal to the absolute value of its height.
On the island, there is a button that can move a volcano from above ground to underground or a volcano from underground to above ground. Bob wants to find out what is the maximum number of special volcanoes that can be obtained by using that button only once.

# Input data
The input file `vulcani.in` contains on the first line a non-zero natural number $N$ which represents the number of volcanoes. The next line will contain $N$ integers which represent the heights of the volcanoes.

# Output data
The output file `vulcani.out` will contain on the first line the maximum number of special volcanoes that can be obtained.

# Constraints and clarifications
* $1 \leq N \leq 10^5$
* $\- 10^9 \leq H \leq 10^9$
* For tests worth $10$ points $N \leq 100$.
* For other tests worth $25$ points $N \leq 1 \ 000$.
* For other tests worth $25$ points $\- 10^6 \leq H \leq 10^6$.
* For other tests worth $40$ points, there are no additional constraints.

# Example 1

`vulcani.in`
```
6
7 9 -5 2 3 -4
```

`vulcani.out`
```
5
```

## Explanation
For the first example, the answer is obtained by using the button on the first or the second volcano. After this change, the volcanoes at positions $1, 2, 3, 5$ and $6$ are special.

# Example 2

`vulcani.in`
```
5
6 8 8 4 -9
```

`vulcani.out`
```
3
```

## Explanation
In the second example, initially the volcanoes at positions $3, 4$ and $5$ are special. Changing the type of the volcano at positions $1, 2$ or $3$ yields the maximum number which equals the initial number of special volcanoes.