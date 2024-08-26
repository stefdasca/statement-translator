# Carpet Bomber

Ato Marm remembered the times when he used to play C&C Generals. Carpet Bombing was a technique used by Chinese generals in the war against GLA. A salvo of bombs was released by a powerful aircraft, usually a B-52, on a zone chosen by the general, causing significant damage. The bombers maintained a linear trajectory and thus were very efficient at stopping transport convoys on the roads. Chinese General Tsing Shi Tao has orders to bomb the entire surface of a linear highway. This highway is divided into $1\,000\,000$ segments of length $1$, numbered from $1$ to $1\,000\,000$. The general has at his disposal $N$ aircraft, each of them having explosive type $T_i$ and a continuous interval on the highway $[L_i, R_i]$ that it bombs if used. He also has orders to use aircraft with at most $2$ different types of explosives. The task is to find the minimum number of aircraft necessary to bomb the entire highway, if it is possible. If it is not possible to bomb the entire highway, print $-1$.

## Input data

The input file `carpetbomber.in` contains on the first line the number $N$ of bombs. Each of the following $N$ lines will contain $3$ natural numbers representing, respectively, the type of the bomb $T_i$, the left endpoint $L_i$ of the interval affected by bomb $i$, and the right endpoint $R_i$ of the interval affected by bomb $i$.

## Output data

The output file `carpetbomber.out` will contain the minimum number of aircraft necessary to bomb the entire highway, respecting the mentioned restriction, or $-1$ if covering the entire highway is not possible.

## Constraints

$ 1 \leq N \leq 8\,191 $

$ 1 \leq T_i \leq 1\,023 $

$ 1 \leq L_i \leq R_i \leq 1\,000\,000 $

## Example

`carpetbomber.in` 
```
5
1 1 250000
2 250001 500000
1 750001 1000000
3 500001 1000000
2 500001 750000
```

`carpetbomber.out`
```
4
```

## Explanation

Bombs with order numbers $1$, $2$, $3$, and $5$ will be used. If we could use bombs with more than $2$ types of explosives, we would use bombs with order numbers $1$, $2$, and $4$ to bomb the entire highway.