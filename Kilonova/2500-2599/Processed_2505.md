Consider a pair of character strings, $S$ and $T$, of length $n$ and $m$, respectively, formed exclusively from lowercase letters of the English alphabet. The positions of the letters are numbered in the string starting from $1$.

There are two types of operations that can be performed on string $T$:

* $1 \ p$: the letter at position $p$ is deleted;
* $2 \ st \ dr$ (with $st \leq dr$): the letters in the subarray corresponding to the interval of positions $[st, dr]$ are sorted in increasing (alphabetical) order;

where $p$, $st$, and $dr$ are positions of letters in string $T$.

Initially, all the letters of string $T$ are uncolored. An operation of type $2$ can be performed only if all the letters in the subarray corresponding to the interval of positions $[st, dr]$ are uncolored. After sorting, all letters in this subarray become colored.

# Task

For each pair of strings of type $S$ and $T$ given:

* Display the distinct letters that appear in at least one of the strings and, for each of them, the symbol of the string (letters $S$ or $T$) in which it appears more often. In case of a tie, choose string $T$.
* Determine a sequence of operations of type $1$ and/or $2$ that can be applied to string $T$, transforming it into a string equal to $S$. Display `YES` if such a sequence of operations exists, or `NO` otherwise.

# Input data

The input file `opsir.in` contains on the first line the natural number $c$, representing the task that needs to be solved ($1$ or $2$) for each of the given pairs of strings.

On the second line of the file, there is the natural number $k$, representing the number of tests. Each test includes specific data for a pair of strings of the type specified in the statement, with data found on three lines in the file, as follows: on the first line $n$ and $m$, in that order, with the meaning from the statement, on the second line string $S$, and on the third line string $T$.

# Output data

For $c = 1$, the output file `opsir.out` will contain, for each test, a natural number $nr$, representing the number of distinct letters that appear in at least one of the strings, followed by $nr$ lines, each containing such a letter, as well as the uppercase letter $S$ or $T$, corresponding to the string in which it appears more often. The lowercase letters will be displayed in alphabetical order.

For $c = 2$, the output file `opsir.out` will contain $k$ lines, each line containing the answer (`DA` or `NU`) corresponding to a test, in the order in which they appear in the input file.

# Constraints and clarifications

* $1 \leq k \leq 100$;
* $1 \leq n, m \leq 200 \ 000$;
* For $c = 2$, $n \leq m$;
* The sum of the lengths of strings of type $S$ in the $k$ tests does not exceed $200 \ 000$;
* The sum of the lengths of strings of type $T$ in the $k$ tests does not exceed $200 \ 000$.

|# | Points | Constraints|
| - | - | ------------|
|1|20|$c = 1$|
|2|15|$c = 2$, strings of type $S$ in each test have the letters sorted in increasing/alphabetical order.|
|3|25|$c = 2$, strings of type $T$ in each test can be transformed into the corresponding string of type $S$ by applying only operations of type $1$.|
|4|40|$c = 2$|

# Example 1

`opsir.in`
```
1 
3
2 4
cc
cbbd
3 2
aab
aa
2 2
ac
da
```

`opsir.out`
```
3
b T
c S
d T
2
a T
b S
3
a T
c S
d T
```

## Explanation

There are $3$ distinct letters according to the task: letter `b` appears more often in $T$, `c` appears more often in $S$, and `d` appears only in $T$.

# Example 2

`opsir.in`
```
2 
1
2 2
zx
zx
```

`opsir.out`
```
DA
```

## Explanation

The strings are equal without needing to apply any operation.

# Example 3

`opsir.in`
```
2
2
2 3
ab
bca
4 4
bacc
cbac
```

`opsir.out`
```
DA
NU
```

## Explanation

For the first test, we can sort the entire string $T$, obtaining "$\texttt{\underline{abc}}$". We can then delete the third letter, obtaining a string equal to $S$.

For the second test, if we apply an operation of type $2$ for the subarray formed from the first $2$ letters, we obtain "$\texttt{\underline{bc}ac}$". Considering that the first $2$ letters become colored after sorting (represented by underlining in this case), we cannot apply an operation of type $2$ for the subarray "$\texttt{\underline{c}a}$" anymore. Therefore, we cannot transform string $T$ into a string equal to $S$.