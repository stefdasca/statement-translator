# Shells

As summer approaches, Denisa and Alexandra, childhood friends, go to the seaside. Walking all day along the shore, they start collecting shells. After collecting $N$ shells, Alexandra strings them on a thread and finds that they are colored in a maximum of $C$ colors. Denisa now wants to choose from the $N$ shells, a harmonious subarray, as long as possible, to make a beautiful necklace. A harmonious necklace means that it has shells of all available colors and each has the same frequency of appearance. Since the number of collected shells can be quite large (because the girls are very patient), your help is needed.

## Task

Help Denisa determine the longest harmonious subarray from the $N$ shells to make the most beautiful necklace.

## Input data

The input file `scoici.in` contains on the first line the number of shells $N$ and the number of colors $C$. The second line will contain the colors of the collected shells, encoded by natural numbers from $1$ to $C$.

## Output data

The output file `scoici.out` will contain two numbers: the position in the sequence of shells where the necklace starts and its length.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  
$2 \leq C \leq 10$  
If there are multiple optimal solutions with the same length, determine the one with the smallest initial position.  
It is guaranteed that a solution exists and that in the given sequence there is at least one shell of each color.

## Example

`scoici.in`  
`9 3`  
`1 2 1 3 3 2 1 1 3`  

`scoici.out`  
`1 6`

## Explanation

The longest subarray is $1\ 2\ 1\ 3\ 3\ 2,$ with frequencies equal to $2$ and all $3$ colors present.