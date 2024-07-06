The City Hall of ONI has signed a contract with the company Gigel.SRL to arrange the fence of the Botanical Garden. The company's boss noticed that the given fence is made up of only three types of planks arranged without any rule. Being a person with "aesthetic taste," he proposed to rearrange the planks so that the fence contains the planks grouped as follows: first the planks of the smallest size, then the medium ones, and lastly, the largest ones. The team designated to carry out the job has one worker who wants to know the minimum number of swaps required to solve the problem and arrange the planks as decided by the company's boss. The swap operation involves choosing two different planks and placing one in the other's position.

# Task

Given a number $n$ representing the number of planks that make up the fence, as well as the way the planks are arranged in the fence, determine the minimum number of swaps that need to be done so that the fence has the planks arranged in ascending order. The planks are encoded by size with values $1$, $2$, and $3$.

# Input data

The file `sort.in` contains the following:
- The first line contains a natural number $n$.
- The second line contains $n$ values $1$, $2$, or $3$ separated by spaces, representing the arrangement of the planks in the garden's fence.

# Output data

The file `sort.out` will contain a number representing the minimum number of swaps required to arrange the fence so that it is sorted in ascending order.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$

# Example

`sort.in`
```
10
1 3 1 2 2 3 1 3 2 1
```

`sort.out`
```
3
```

## Explanation

- Swap the values at positions $2$ with $10$, then $4$ with $7$, and $6$ with $9$.
- The successive results will be:
$1 \\ \textcolor{red}{1} \\ 1 \\ 2 \\ 2 \\ 3 \\ 1 \\ 3 \\ 2 \\ \textcolor{red}{3}$
$1 \\ 1 \\ 1 \\ \textcolor{red}{1} \\ 2 \\ 3 \\ \textcolor{red}{2} \\ 3 \\ 2 \\ 3$
$1 \\ 1 \\ 1 \\ 1 \\ 2 \\ \textcolor{red}{2} \\ 2 \\ 3 \\ \textcolor{red}{3} \\ 3$