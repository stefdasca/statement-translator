## Task

From young lady to young lady, Mr. Boss is a great charmer. On Saturday night, he charmed $N$ young ladies at the club and promised each one a visit. On Sunday, he woke up late and realized he had already visited a lucky lady but couldn't recall which one. Mr. Boss decided he would leave home again at 12 o'clock and has exactly $T$ minutes for visits. He knows exactly how much time he will spend with each young lady, including the travel time to and from her home. After visiting one girl, Mr. Boss returns home before going to the next, to avoid any suspicion. Mr. Boss assigned each girl a beauty coefficient. After visiting someone with coefficient $X$, it is beneath his dignity to visit anyone with a coefficient less than or equal to $X$ (in other words, Mr. Boss will only visit girls in strictly increasing order of their beauty coefficients). Given these conditions, Mr. Boss is curious to find out for each girl, if she was the one already visited, what is the maximum number of other girls he can visit. Mr. Boss goes to get ready for his meetings. In the meantime, knowing $t[i]$ - the time in minutes spent with girl $i$ and $c[i]$ - the beauty coefficient of girl $i$, you need to help Mr. Boss find out how many girls he can visit maximum for any given girl he might have already visited.

## Input data

The first line of the file `dlboss.in` contains an integer $N$, representing the number of young ladies. The second line contains $T$, the time in minutes allocated for visits. The next $N$ lines contain two integers separated by a space which describe the time spent with each girl and her beauty coefficient. 

## Output data

The output file `dlboss.out` will contain $N$ lines, line $i$ representing the maximum number of girls Mr. Boss can visit if he starts his visits from the young lady with index $i$. 

## Constraints and clarifications

$1 \leq N \leq 100000$ 

The beauty coefficients are integers between $1$ and $10^9$ 

$1 \leq T \leq 10^9$ 

$1 \leq t[i] \leq 10000$ 

Both Mr. Boss and his beautiful ladies have discovered the secret of eternal life, so there is no reason to worry about anything. 

## Example

`dlboss.in`

```
10
720
120 10
180 50
45 7
240 25
90 40
200 13
56 8
450 70
15 5
60 29
```

`dlboss.out`

```
6
3
2
4
5
0
6
3
2
4
```