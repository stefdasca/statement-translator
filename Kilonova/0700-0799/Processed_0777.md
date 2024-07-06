Here is the translated problem statement:

On planet ZUZU, a year has $10\ 000\ 000$ days, numbered from $1$ to $10\ 000\ 000$. At the planetary research institute, a group of specialists take care of multiple virus populations. For each population, a working interval $[a, b]$ is allocated, with $a$ and $b$ representing days of the zuzulian year, during which determinations about the number of individuals in the population, new forms of viruses appearing, etc. are made. The institute director has noticed that there are periods with no research activities, which is why he hired Atomel, a famous statistician, to check the longest working period during which researchers are occupied with virus populations, as well as the longest period during which no studies on viruses are conducted.

# Task

Given the number $n$ of working intervals on virus populations, and for each interval the starting day and the ending day of the working interval, determine the longest period during which work on the virus populations is carried out, as well as the longest period during which no observations on viruses are made.

# Input data

The input file `virus.in` contains the first line a value $n$ denoting the number of given intervals; the next $n$ lines contain two space-separated values each, describing a working and observation interval $[a, b]$ on virus populations. The intervals are correct, with $a < b$.

# Output data

The output file `virus.out` contains two space-separated values $L \ P$, where $L$ represents the longest period during which research on virus populations is conducted, and $P$ the longest period during which no observations are made.

# Constraints and clarifications

* $0 < n \leq 5\ 000$;
* $1 \leq a, b \leq 10\ 000\ 000$; where $a$ and $b$ describe a time interval.

# Example

`virus.in`
```
3
700 1200
300 1000
1500 2100
```

`virus.out`
```
900 300
```

## Explanation

The intervals of days are represented as follows:

~[virus.png|width=34em]

The largest working period is between days $300$ and $1200$, which means a period of $900$, and the longest period without observations is between days $1200$ and $1500$, thus a period of $300$.

I have double-checked the statement and corrected any potential grammar and syntax errors in accordance with the rules of English language.