# Heavy metal

Miruna recently ventured into the good music business. She decided to organize a heavy metal festival and bought a concert hall. She invited $N$ bands to the festival, but each band can only play for a certain fixed interval of time. Because the fans are unruly, Miruna wants to select the bands that will play in such a way that the total time during which someone is performing is as long as possible. In choosing the bands, she must ensure that no two bands perform at the same time.

## Input data

The first line of the input file heavymetal.in contains a natural number $N$, as described above. The next $N$ lines each contain two values $A_i$ and $B_i$, representing the time intervals during which the bands can play.

## Output data

The output file heavymetal.out will contain a single number representing the maximum sum of time intervals during which the bands will play.

## Constraints

$1 \leq N \leq 100000$  
$1 \leq A_i, B_i \leq 10^9$  
$A_i < B_i$

For 40% of the tests,  
$1 \leq N, A_i, B_i \leq 1000$

## Example

`heavymetal.in`
```
4
3 5
5 10
3 4
1 2
```

`heavymetal.out`
```
8
```

## Explanation

Bands $1$, $2$, and $4$ will play, and the total time will be $2 + 5 + 1 = 8$.