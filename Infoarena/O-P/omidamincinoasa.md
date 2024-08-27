# Lying Caterpillar

Benson discovered that the snake from the Bible was actually a translation error. It was actually a caterpillar. Now he feels sorry for Adam.

## Task

Given $n$ and $k$, compute the sum $C(n,0)·0^k + C(n,1)·1^k + C(n,2)·2^k + \dots + C(n,n)·n^k$. Here, $C(i,j)$ denotes the combination of $i$ taken $j$ at a time.

## Input data

The input file `omidamincinoasa.in` contains on the first line the number $t$ - the number of test cases. The following $t$ lines describe the test cases. Each test case is described on a single line with $n$ and $k$.

## Output data

The output file `omidamincinoasa.out` contains for each test case the required sum modulo $998244353$. The answers should be printed on separate lines.

## Constraints and clarifications

$1 \leq t \leq 10$

$1 \leq n \leq 10^9$

$0 \leq k \leq 5000$

It is considered that $0^0 = 1$

Subtasks # Points

## Constraints

1:

D: It might be in Bucharest, but here it’s with me; Tell them to stop for a check--- Good day, Dorel Mateescu, Doiaru, head of the station, what are you transporting in the freight car?

V: Well, um, it’s an American military transport, for the front in Kosovo; It’s a NATO car, and the content is, it is strictly secret

3 $k = 0$

2:

D: Aha, show me the paperwork for inspection.

V: You don’t understand, it’s a military transport and we have approval from the top, from the government.

3 $k = 1$

3:

D: You don’t understand. I have regulations. Without proper paperwork, I cannot let you pass.

4 $k = 2$

4:

M: Is there a problem here (Asking if there is a problem)

D: I need to see custom and transportation papers.

M: This is a NATO military transport, sir, this has been organized and authorized by your government. Any documentation should be in your possession, sir.

10 $n \leq 2 \cdot 10^5$

5:

D: You have international transport from America?

M: That is correct sir.

D: And where are you, now?

M: I'm in Romania, I guess.

D: So, according to Romanian transportation laws, you need to have custom papers.

22 $k \leq 50$

6:

D: This is legislation. I don't make legislation. I respect legislation. You come to Romania, you have to respect legislation too.

M: So, if you respect legislation, sir, you are hereby advised to comply; have I made myself clear? Have I made myself understood?

23 $k \leq 500$

7:

D: USA. NATO. Bill Clinton, and those from Bucharest. This is my station. C H E C K P O I N T. You need to have custom papers. No papers, no passing. Move them to the second line because I’m irritated.

35 $k \leq 5 \cdot 10^3$

## Example

`omidamincinoasa.in`
```
2
5 0
100 3
```

`omidamincinoasa.out`
```
32
668189687
```

## Explanation

For the first sum, we have $C(5,0) + C(5,1) + C(5,2) + C(5,3) + C(5,4) + C(5,5) = 1 + 5 + 10 + 10 + 5 + 1 = 32$