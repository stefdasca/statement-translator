# Clocks

A clockmaker has decided to create personalized mechanical clocks for more special clients. Thus, clocks can be ordered that have the number of hours in a day and the number of minutes in an hour specified by the customer (the duration of an hour in minutes is the same as the duration of a minute in seconds). The clocks have an hour hand, a minute hand, and a second hand. A complete rotation of the hour hand represents half a day, and the movement of the hands is the same as on regular clocks. The clockmaker wants to determine how many times exactly the three hands overlap during a day for each ordered clock.

## Input data

The input file `ceasuri.in` will contain on the first line $ T $, the number of clocks ordered. The next $ T $ lines will contain the number of hours in a day $ (N) $ and the number of minutes in an hour $ (M) $ for each clock.

## Output data

The output file `ceasuri.out` will contain $ T $ lines; line $ i $ will contain the number of exact overlaps of the three hands during a day.

## Constraints and clarifications

$ 1 \leq T \leq 20 $

$ 4 \leq N \leq 2000 $

$ 2 \leq M \leq 1000 $

$ T $, $ N $, and $ M $ are natural numbers, and $ N $ is even.

## Example

`ceasuri.in`
```
3
24 60
8 10
12 6
```

`ceasuri.out`
```
2
6
10
```

## Explanation

If the day has $ 24 $ hours, and the hour has $ 60 $ minutes, then during the day the only moments when the three hands overlap are at hour $ 0 $ and hour $ 12 $.