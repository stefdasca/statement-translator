# Taxi

The city X3 was designed by computer scientists so that the streets divide the city in the form of a matrix. The intersections between streets are practically points with integer coordinates within the interval $[0, A]$ for the $X$ coordinate and $[0, B]$ for the $Y$ coordinate. In this city, there are exactly two taxis. Because they have come to an agreement, both taxi drivers charge the same rate for the same distance traveled. Therefore, people do not care which taxi they travel with. When a taxi is needed, the only criterion is the one that is closer. Citizens are very well-informed and know the exact coordinates of the taxis. Serious problems arise when the taxis are at an equal distance because citizens cannot decide and remain in place for hours. Today being a very busy day, at every intersection there is exactly one person who wants to call a taxi.

## Task

Write a program that determines how many people will remain undecided.

## Input data

The input file `taxi.in` contains on the first line the number of tests $ T $. In the next $ T $ lines, there are $ 6 $ integers separated by a space representing $ A $ and $ B $ (with the meanings from the statement) and $ x1 $ $ y1 $ $ x2 $ $ y2 $ the coordinates of the two taxis ($ x1 $ and $ x2 $ represent the $ x $ coordinates of the $ 2 $ taxis).

## Output data

The output file `taxi.out` will contain $ T $ lines, one for each test. Each line will contain an integer representing the number of undecided people for that test.

## Constraints and clarifications

$1 \leq T \leq 100\ 000$

$1 \leq A \leq 10\ 000$

$1 \leq B \leq 10\ 000$

$0 \leq x1, x2 \leq A$

$0 \leq y1, y2 \leq B$

## Example

`taxi.in` 
```
1
9 9999 0 0 2 0
```

`taxi.out`
```
10000
```