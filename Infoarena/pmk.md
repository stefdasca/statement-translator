## Pmk

The KMP algorithm is used to efficiently search for occurrences of a word in a text. Initially, it computes the prefix function for any prefix of the word. For a string, the function's result is the length of the longest proper prefix which is also a (proper) suffix of the string. A proper prefix of a string is a prefix different from the string (the entire string is not a proper prefix). As an implementation convention, the result of the prefix function stored at position $i$ is the function for the prefix from the first position up to position $i$ exclusively, and for the first position, it is considered that the function returns $-1$. An example for the values of the prefix function is as follows:

\[
\begin{array}{c|cccccccccc}
i & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
\hline
\text{string}[i] & \text{a} & \text{b} & \text{b} & \text{a} & \text{a} & \text{b} & \text{b} & \text{b} & \text{b} & \text{a} \\
\text{prefix}[i] & -1 & 0 & 0 & 0 & 1 & 1 & 2 & 3 & 0 & 0 \\
\end{array}
\]

For example, $\text{prefix}[6] = \text{prefix}("abbaab") = \text{length}("ab") = 2$

Given the result of the prefix function for a string of a given length, determine the first string in lexicographic order for which the prefix function has those respective values. The string will consist only of lowercase letters of the English alphabet.

## Input data

The input file pmk.in contains a single line with the number $N$, the length of the string, followed by $N$ numbers, valid values for the prefix function of a string of length $N$.

## Output data

In the output file pmk.out print a string of characters for which the prefix function has the specified values.

## Constraints

$1 \leq N \leq 10000$

There will be at least one solution containing only lowercase letters of the English alphabet.

## Example

`pmk.in`

`10 -1 0 0 0 1 1 2 3 0 0`

`pmk.out`

`abbaabbbba`