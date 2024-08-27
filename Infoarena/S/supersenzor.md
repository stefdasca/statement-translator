# Supersensor

In the mythical land of Zalău, where a day lasts $10^{100}$ seconds, Marcel decided to start a business. He opened a store and, with his digital skills, managed to automate it completely. However, there is still one problem: the light. He decided to use a smart sensor to automatically turn on the lights only when needed for periods of $val$ seconds, so as not to waste energy. Each day, a single customer visits the store (there are very few people in Zalău, the population of Zalău is not high enough for a higher frequency, but we exaggerated for the sake of the problem), and the sensor turns on the light for a multiple of $val$ seconds so that the light is on for the entire duration of the customer's stay. Being a smart sensor, it keeps the light on for a minimal period of time that meets these conditions. You need to find the total minimum time the light is on (for economic reasons, Marcel wants to minimize electricity costs), by setting an appropriate value for $val$. However, Marcel's equipment has limited precision, so the value $val$ must be greater than or equal to a time value $T$, as the sensor does not perceive smaller time durations.

## Task

Determine the total minimum time the light will be on given the constraints and settings provided.

## Input data

In the input file `supersenzor.in`, the first line contains the values $N$ and $T$ separated by a space. The second line contains the $N$ values $A[i]$ representing how long the customer of day $i$ stays in the store.

## Output data

In the output file `supersenzor.out`, print a single number representing the total minimum time the light stays on.

## Constraints

$1 \leq N \leq 50$

$1 \leq T \leq 10^9$

$1 \leq A[i] \leq 10^9$

For 24 points, all values in the file are less than or equal to $10^5$.

Tests 1, 2, 3 are not grouped.

For the remaining 76 points, tests 4-14 are grouped.

## Example

`supersenzor.in`
```
5 2
1 2 3 4 5
```
`supersenzor.out`
```
18
```

`supersenzor.in`
```
5 7804348
761747669 613711320 559766994 200028176 222599851
```
`supersenzor.out`
```
2363658292
```

## Explanation

In the first example, we choose the period $val$ equal to $2$. In the $5$ days, the light stays on, in turn, for $2$, $2$, $4$, $4$, $6$ seconds, staying on for a total of $18$ seconds.