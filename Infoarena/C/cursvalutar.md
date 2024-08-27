Curs Valutar

The International Students' Bank makes transactions both in the local currency and with $N$ different types of international currencies. Every day the bank displays the exchange rate with the quotation of each currency relative to the local currency. Students do not like work but have various ideas of getting rich quickly and safely. One such idea is to profit from the fluctuations in the bank's exchange rates. A student has a scholarship that is worth $S$ units in the local currency. Given the exchange rate forecast of the $N$ international currencies relative to the local currency over a period of $Z$ days, we want to determine the maximum amount that can be obtained after those $Z$ days, also in the local currency. It is known that at any time an unlimited number of buying or selling transactions can be made between the local currency and any other currency, within the limits of the available budget at that moment.

## Input data

The input file `cursvalutar.in` contains on the first line a natural number $T$, the number of tests. Each of the $T$ subsequent tests is described as follows: The first line contains 3 numbers $S$, $N$, $Z$ having the meanings given in the statement. Then follows a matrix with $N$ rows and $Z$ columns, the element on row $i$ and column $j$ representing the quotation of the $i$-th international currency on day $j$. 

## Output data

In the output file `cursvalutar.out` you will print the results for each of the $T$ tests, each on a separate line and in the order of the input file. 

## Constraints and clarifications

$1 \leq T \leq 2000$  
$1 \leq N \leq 10$  
$1 \leq Z \leq 25$  
$1.0 \leq S \leq 100.0$  
$1.0 \leq the\ quotation\ of\ any\ currency \leq 4.0$  
The evaluation of the results will be performed with a margin of error of $10^{-3}$ 

## Example

`cursvalutar.in`  
```
1  
10.0 2 5  
1.0 2.0 4.0 3.0 2.0  
2.0 3.0 2.0 2.0 3.0  
```

`cursvalutar.out`  
```
60.000000  
```

## Explanation

A possible solution would be the following:  
day 1: convert the entire sum to the first currency  
day 3: sell the entire sum now valued at $40.0$ (local currency), then convert to the 2nd currency  
day 5: convert back to local currency