# Oltenesc

A number $X$ is called *oltenesc* if it does not contain any power of $2$ with at least $2$ digits as a subarray in its decimal representation. Nea Mărin has a number $N$ consisting of at most $100$ digits and wonders how many natural numbers at most equal to $N$ are *oltenesc*. Because the answer can be quite large, only the remainder when divided by $10^9 + 7$ is required. 

## Task

You are given $T$ queries, each consisting of a single number $N$. For each query, calculate how many numbers $0 \leq X \leq N$ are *oltenesc*, modulo $10^9 + 7$. 

## Input data

The first line of the file `oltenesc.in` contains the number $T$. The next $T$ lines contain one number $N$ consisting of at most $100$ decimal digits, representing a query. 

## Output data

The output file `oltenesc.out` will contain $T$ lines, containing the answers to the $T$ queries from the input file. 

## Constraints and clarifications 

$1 \leq T \leq 10$ 

$1 \leq N \leq 10^{100}$ 

For $10\%$ of the tests, we have $T = 1$ 

and $N \leq 10^6$. 

For $50\%$ of the tests, we have $N \leq 10^{18}$. 

A subarray of a decimal number is understood to mean the number obtained by keeping a continuous sequence of digits from the original number. 

For example, $234$, $12$, and $12345$ are subarrays of the number $12345$, but $135$ and $432$ are not. 

## Example

`oltenesc.in`

```
4
33 
999 
232323 
992391662939123897
```

`oltenesc.out`

``>
32 
938 
194003 
515744048 
```

## Explanation

The only numbers that are not *oltenesc* between $0$ and $33$ are $16$ and $32$. 

The only numbers that are not *oltenesc* between $0$ and $999$ are $128$, $256$, $512$ and those of the forms $16\_$ , $32\_$ , $64\_$ , $\_16$, $\_32$, $\_64$ (note how the number $164$ appears twice in this list).