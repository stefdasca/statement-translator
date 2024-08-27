# Socks

You read the local tabloid as you do every day. You shouldn't, but you do. Among the articles: 
- "Ten optimizations that compilers don't want you to know!"
- "See which renowned Olympian is moving to ASE!"
- "Searching through invoices: which Olympian replaced their morning coffee with $\dots$ their morning FFT."
- "<I thought about my future and decided it is optimal to go to UNIBUC and financially support myself by doing the homework of those in Poli.> A startling confession by a 12th-grade student."
- "SURVEY: What is most in demand in the job market? Intelligence, persistence, or Aliens' frauds?"

Same old, same old. Instead, in the "Gossip about info-celebrities" section, you see an article that stimulates you algorithmically: 
Alex Velea and his girlfriend have troubles with$\ldots$socks?

The renowned artist-tractorist Alex Velea was recently seen with his girlfriend buying socks. As our readers know too well, Alex has a complicated history with socks. This time, Alex wants to buy $P$ types of socks out of the $N$ types available at the chosen store. Each type is defined by two parameters: color and size. Rumor has it that Alex's girlfriend imposes an unusual$\ldots$ restriction on his purchase. She knows Alex is very careless when it comes to putting on his socks. More precisely, for Alex, it is acceptable to wear two socks if they have the same size or the same color. Alex's girlfriend calls a pair where the socks have the same size or the same color but do not have both the same size and the same color a "weird" pair. She would like Alex to buy $P$ types of socks such that the total number of weird pairs of sock types formed is as minimal as possible. She wants the answer for each $P$ from 1 to $K$.

## Input data

The input file `socks.in` will contain on its first line the numbers $N$ and $K$, representing the number of available types of socks and respectively the upper limit of $P$ for which Alex's girlfriend wants to know the answer. The next $N$ lines will contain a pair $color$ $size$, where $color$ is a string, and $size$ is a natural number. 

## Output data

The output file `socks.out` will contain $K$ lines, the $i$-th containing the answer for $P = i$.

## Constraints and clarifications

$1 \leq K \leq N \leq 1000$

$1 \leq Sizes\ of\ the\ socks \leq 10^9$

The colors of the socks are strings of maximum length 20, without spaces.

All the $N$ available types of socks are distinct pairwise (they differ either in size, color, or both).

## Example

`socks.in` 
```
3 3
Nelachet 45
Lachet 43
Lachet 45
```

`socks.out` 
```
0
0
2
```

## Explanation

For $P = 1$ Alex can buy any of the three types of socks.

For $P = 2$ Alex will buy types 1 and 2, which have both distinct colors and sizes. Thus, no weird pair is formed.

For $P = 3$ Alex will be forced to also buy the third type of socks. This forms a weird pair with type 1 (because they have the same size but different colors) and with type 2 (because they have the same color but different sizes). Thus, the answer is 2.