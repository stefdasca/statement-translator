## Holiday

We are pleased to introduce you to Antonio! Antonio is passionate about algorithms, just like you. He is a computer science student and has prepared some problems for Round 5, inspired by his life. Let the story begin... Not long ago, Antonio met Antonia, a literature student, with whom he spent a lot of time writing essays on pedagogy. Besides essays, the two thought it would be great if they organized their free time. Antonio knows for sure that he will go on vacation starting with week $A$, every $X$ weeks. Similarly, Antonia knows she will go on vacation starting with week $B$, every $Y$ weeks. Antonia's problem is that this $Y$ is unknown. Because she likes Antonio a lot, Antonia wants to choose a $Y$ such that she meets Antonio on vacation as many times as possible during the academic year. Since she has a lot to study for her exams, if there are multiple values of $Y$ that meet the previous condition, Antonia will choose the largest value among them. The academic year starts in week $1$ and ends in week $2^{32} - 1$.

## Input data

The input file `holiday.in` contains on the first line 3 natural numbers, $A$ $B$ $X$, with the meaning described above.

## Output data

The output file `holiday.out` will contain a single natural number $Y$, with the meaning described above.

## Constraints

$1 \leq A$,

$B$,

$X \leq 10^9$

## Example

`holiday.in` `holiday.out`

## Explanation

`1 1 5 5` Both Antonio and Antonia go on vacation starting with week $1$. Antonio goes every $5$ weeks, so Antonia will also go every $5$ weeks to meet Antonio each time.

`2 5 2 1` The only way for Antonia to meet Antonio as often as possible is to go on vacation every week.