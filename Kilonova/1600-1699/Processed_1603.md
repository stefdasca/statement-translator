```markdown
"Year 1905, autumn"

With your help, Badinho received state subsidies, and the construction of the route was completed in record time. Due to this success, he decided to start a new business in Mexico City. On the lands owned by the city's mayor, a rare species of cactus grows, which, upon maturity, will bear pitahaya fruits, also known as "dragon fruits."

The field owned by the mayor has the shape of a row of $N$ cacti, arranged from left to right, numbered from $1$ to $N$. We denote $A_i$ for $1 \leq i \leq N$ the number of ripe fruits on cactus $i$. El Alcalde (the mayor) wants to harvest exactly $K$ fruits from the field, so he has contracted Badinho's company.\
For logistical reasons, the cactus harvesting will be done in at most $S$ stages. In one stage, the drone that collects the fruits will fly over a single plot of cacti and will pick all the ripe fruits from the cacti flown over. A plot is defined as a subarray of cacti. For example, the plot $[6, 9]$ consists of cacti $6, 7, 8$, and $9$. To avoid disturbing the cactus population, each cactus can be flown over at most once during the entire harvesting operation. Flying over a plot means flying over all the cacti in that plot.

To better plan the fruit harvesting, Badinho needs to make a _harvesting plan_. More precisely, such a plan consists of a number $S' \leq S$ of harvesting stages that will be performed and the plots that will be flown over during each of the $S'$ stages. Two harvesting plans are considered different if there is at least one plot flown over in a stage of one plan that is not flown over in any stage of the other. For example, if in a plan consisting of two stages the plot $[1, 2]$ is flown over, followed by the plot $[3, 4]$, and in another plan consisting of two stages the plot $[3, 4]$ is flown over, followed by the plot $[1, 2]$, then the plans are considered identical. However, if in one plan with a single stage the plot $[1, 2]$ is flown over, and in another plan consisting of two stages the plots $[1, 1]$ and $[2, 2]$ are flown over, then the plans are considered distinct. Another example is that if in a plan consisting of two stages the plot $[1, 3]$ is flown over, followed by the plot $[4,4]$, and in another plan consisting of two stages the plot $[1, 2]$ is flown over, followed by the plot $[3, 4]$, then the plans are considered to be distinct.

# Task
To establish his harvesting plan, Badinho is interested in the answers to the following questions:

* $q_1$: What is the minimum total number of cacti that should be flown over in a harvesting plan?
* $q_2$: How many harvesting plans exist where the minimum number of cacti is flown over? Since this number can be very large, only the value modulo $1\ 000\ 000\ 007$ is required.

Badinho wants to find out the answers to these two questions for a number $T$ of scenarios. A scenario is determined by the values $N$, $K$, $S$, $A_1, A_2, \ldots, A_N$.

# Input data

The first line of the `dragonfruit.in` file contains the number $T$, followed by the $T$ scenarios, each in the following format:

* The first line contains the natural numbers $N$, $K$, $S$, separated by spaces;
* The second line contains the numbers $A_1, A_2, \ldots, A_N$ separated by spaces.

# Output data

For each of the $T$ scenarios, a line will be printed in the output file `dragonfruit.out` which will contain two natural numbers separated by a space, representing, in order, the answers to questions $q1$ and $q2$ from the task for the current scenario. If, for a certain scenario, there is no harvesting plan that meets the given requirements, `0 0` will be printed on the respective line.

# Constraints and clarifications

* $1 \leq T \leq 5$
* $1 \leq K \leq 1\ 000$
* $1 \leq S \leq 10$
* $0 \leq A_i \leq 1\ 000$ for any $1 \leq i \leq N$

|#|Points|Constraints|
|-|-|--------|
|1|4|$S = 1$ and $1 \leq N \leq 2\ 000$|
|2|7|$S = 2$ and $1 \leq N \leq 100$|
|3|9|$S = 3$ and $1 \leq N \leq 50$|
|4|10|$S = 1$ and $1 \leq N \leq 100\ 000$|
|5|13|$S = 2$ and $1 \leq N \leq 2\ 000$|
|6|23|$1 \leq N \leq 70$|
|7|34|$1 \leq N \leq 2\ 000$|

# Example

`dragonfruit.in`
```
4
8 7 4
2 1 0 1 0 2 1 99
2 99 10
50 50
3 8 1
1 8 1
5 3 2
2 1 2 1 1
```

`dragonfruit.out`
```
5 3
0 0
1 1
2 9
```

# Explanation

## Scenario 1

The following harvesting plans collect $7$ dragon fruits by flying over a minimum number of cacti:
   
* Plan 1: $[1, 2]$, $[4, 4]$, $[6, 7]$;
* Plan 2: $[1, 1]$, $[2, 2]$, $[4, 4]$, $[6, 7]$;
* Plan 3: $[1, 2]$, $[4, 4]$, $[6, 6]$, $[7, 7]$.

Notice that the harvesting plan $[1, 3]$, $[4, 4]$, $[6, 7]$ is not considered valid, as it flies over $6$ cacti, which is not the minimum, even though $K=7$ dragon fruits were harvested.

## Scenario 2 

There is no harvesting plan where $99$ dragon fruits are harvested.

## Scenario 3 

There is a single harvesting plan where $8$ dragon fruits are harvested: $[2, 2]$.

## Scenario 4 

The following harvesting plans collect $3$ dragon fruits by flying over a minimum of $2$ cacti:
   
* Plan 1: $[1, 2]$;
* Plan 2: $[2, 3]$;
* Plan 3: $[3, 4]$;
* Plan 4: $[1, 1]$, $[2, 2]$;
* Plan 5: $[1, 1]$, $[4, 4]$;
* Plan 6: $[1, 1]$, $[5, 5]$;
* Plan 7: $[2, 2]$, $[3, 3]$;
* Plan 8: $[3, 3]$, $[4, 4]$;
* Plan 9: $[3, 3]$, $[5, 5]$.

Notice that the harvesting plan $[2, 2]$, $[4, 4]$, $[5, 5]$ is not considered valid, as it flies over $3$ cacti, which is not the minimum, even though $K=3$ dragon fruits were harvested.
```
