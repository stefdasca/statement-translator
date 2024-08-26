## Task

Why did we call it this way? We all want to live forever. Unfortunately, this is unlikely. However, our friend Faust, a philosopher and great sage, has the unique opportunity to apply for the company Ludai Romania where everything is possible. Of course, before that, he will have to go through numerous exhausting interviews (held, as you rightly guessed, by the well-known Mephisto). Faust was informed that he would have to participate in $T$ existential (interview) tests in the coming days. Fortunately for him, there was a breach in the email system (the culprit was not found), so Faust conveniently obtained the tests for all $T$ days beforehand. Curiously, all the days contained very similar tests. Faust noticed that the problem statement was identical each day: You are in an unknown realm that has $N$ cities. Some cities are poor, others are wealthy, but $K$ of them contain valuable relics. What you have to do is "retrieve" all the relics, in the name of Ludai Romania. You can start in any city you want and can stop in any city you want, but once you enter a city, be sure you will never be able to return (alive). Choose your path wisely! Alongside each of the $T$ statements that Mephisto seemingly did not bother to make look any different, there is an attached description of the realm, the relics, and the direct roads between cities, in an identical format to the pang.in file. For simplicity, the relics are identified by the city they are in. As Faust is not exactly uninitiated in Mephisto's tricks, he notices that in some tests, the journey is impossible! However, the data is so immense that he is quickly overwhelmed by the difficulty of the test. Help Faust pass all the interview tests by writing a "helping sheet" for him! More precisely, for each of the $T$ tests, Faust would like to know if the requirement of that specific day is possible and, if so, to know the order in which to start the search for the relics. This way he can finally relive his youth (as the job of a philosopher did not bring him many benefits so far).

## Input data

The input file pang.in will contain on the first line a number $T$ representing the number of interview tests Faust will participate in. Then, there will be $T$ groups as follows: The first line will contain $N$, $M$, and $K$ representing the number of cities in the realm, the number of access roads, and the number of relics. On the following $M$ lines there will be 2 numbers $A$ and $B$ representing the fact that you can travel directly from city $A$ to city $B$ (this does not imply that you can travel from $B$ to $A$ as well). On the last line, there will be a sequence of $K$ numbers, representing the indices of the cities where the $K$ relics are located.

## Output data

The output file pang.out will contain, for each of the $T$ tests:
The word "Nu" (without quotes), if there is no way to "retrieve" the $K$ relics, on a single line.
The word "Da" (without quotes), otherwise, on the first line. On the second line, there will be the sequence of cities where the relics are located, in the order they will be recovered.

## Constraints and clarifications

$1 \leq K \leq N \leq 10^5$

$1 \leq M \leq 2*10^5$

The cities are numbered from 1 to $N$

The sum of all $N$ in the input will not exceed $10^5$

The sum of all $M$ in the input will not exceed $2*10^5$

It is guaranteed that once leaving city $A$, Faust will have no way to return to city $A$.

## Example

`pang.in`
```
2
4 4 3
1 2
1 3
2 3
3 4
2 4 1
3 2 3
1 2
1 3
3
```

`pang.out`
```
Da
1 2 4
Nu
```