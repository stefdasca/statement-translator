## Rally

After driving around Bucharest, Alex decided he needs to participate in a rally championship. His only problem is that he doesn't have much gasoline, so he needs to use the gas stations provided by the organizers. The route is circular and has $N$ gas stations placed along it. For each of the $N$ gas stations, the number of liters available for fueling is known, as well as the number of kilometers to the next gas station. Help Alex choose a gas station from which to start so that he can make a complete lap of the route without running out of gasoline.

## Input data

The input file raliu.in contains on the first line $T$, the number of tests. Each test has the following format: the first line contains $N$, the number of gas stations, the next line contains $N$ integers, the $i$-th number representing the number of liters of gasoline available at the $i$-th gas station, and the third line contains $N$ integers, the $i$-th number representing the distance from the $i$-th gas station to the $i+1$-th gas station.

## Output data

The output file raliu.out will contain the responses for the $T$ tests. The response for a test can be "DA" (without quotes) followed by a line containing the index of the gas station from where Alex can start, or "NU" (without quotes) if it is not possible to complete a full lap of the route.

## Constraints and clarifications

$1 \leq T \leq 5$  
$2 \leq N \leq 1\,000\,000$  
$0 \leq$ number of liters, number of kilometers $\leq 2\,147\,483\,640$  
Initially, Alex's car's fuel tank is empty and has unlimited capacity.  
The route is circular, so after gas station $N$, the next one is gas station $1$.  
A complete lap of the route means starting from a gas station $i$, traveling through all gas stations, and returning to gas station $i$.  
Alex's car consumes 1 liter of gasoline for each kilometer traveled (it's not a very good car).  
If there are multiple solutions, the one with the smallest index will be displayed.  
Attention! Alex recommends using 64-bit data types.

## Example

raliu.in
```
2
5
2 6 1 7 3
3 5 3 3 4
3
1 3 4
7 2 2
```

raliu.out
```
DA 4
NU
```