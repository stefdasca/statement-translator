## Task

There are $N+1$ people competing in some event for $N$ days. Each day, exactly one of them is declared the winner of the day. The score of some participant is equal to the number of days he was winner. After each day, the participants with the highest score receive a coin. After the competition is over, each participant has some happiness value, calculated the following way: for every discretely continuous maximal interval when he receives coin, add to his happiness the square of the length of the interval. For example, if some contestant won coins on days $3$, $4$, $10$, $11$, $12$, $18$ and $19$, the intervals are $[3-4]$, $[10-12]$ and $[18-19]$, while his happiness is equal to $2^2 + 3^2 + 2^2 = 4 + 9 + 4 = 17$. The outcome of the competition is the sum of happiness for all participants. Now Marcel comes in, and he is able to insert, somewhere in the array of days, one day that will surely be won by participant number $0$. You are given an array of $N$ integers between $0$ and $N$, representing the winner of each day. Let $f(p) = $ the outcome of the competition if we would insert number $0$ in this array after the $p$'th element in the array. You need to print numbers $f(0), f(1), \dots, f(N)$.

For example, if the array of $3$ elements is $0\ 1\ 1$, $f(0) = $ the outcome of the competition $0\ 0\ 1\ 1$. Participant number $0$ receives coins on days $1$, $2$, $3$, and $4$. So his happiness is $4^2 = 16$. Participant number $1$ receives a coin on day $4$. His happiness is $1^2 = 1$. Participants $2$ and $3$ receive no coins. So $f(0) = 17$. 
$f(N = 3) = $ the outcome of the competition $0\ 1\ 1\ 0$. Participant number $0$ receives coins on days $1$, $2$, $4$ so his happiness is $4 + 1 = 5$. Participant number $1$ receives coins on days $2$, $3$, $4$ so his happiness is $9$. So $f(3) = 14$. 

## Input data

The first line of input file `competition.in` contains a number $N$, and the following line contains $N$ numbers with values between $0$ and $N$, representing the winners of the competition on each day.

## Output data

Output file `competition.out` contains $N + 1$ lines. Line $i$ contains number $f(i - 1)$.

## Constraints and clarifications

$1 \leq N \leq 10^6$ 

For $8$ points, $N \leq 10$ 

For $20$ points, $N \leq 100$ 

For $40$ points, $N \leq 1.000$ 

For $68$ points, $N \leq 100.000$ 

Note that the scoring is not the same as the one in the official onsite contest 

## Example

`competition.in`
```
4
0 4 4 4
```
`competition.out`
```
20
20
21
21
20
```

`competition.in`
```
4
1 0 1 1
```
`competition.out`
```
21
17
17
27
26
```

`competition.in`
```
4
2 1 1 0
```
`competition.out`
```
23
23
27
21
21
```

## Explanation

You can see a solution description in the problem's editorial

Contact the author if you are willing to translate the statement into Romanian.