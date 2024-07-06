Marian is a programmer at a company that produces antivirus software and has been tasked with writing the search engine for the product. The company, being recently established, has provided only a small number of known viruses. The engine will be tested on a bit string extracted from an executable, and it needs to produce a statistic that contains the number of occurrences of each virus in the bit string.

# Task
Write a program to help Marian obtain the required statistic.

# Input data
The first line of the input file `virus.in` contains two natural numbers `L` and `N`, separated by a space, where `L` represents the length of the bit string, and `N` represents the number of known viruses. The second line of the file contains a string of length `L`, consisting only of the characters `0` and `1`, representing the bit string. The following `2*N` lines contain the descriptions of the viruses provided by the analysts. Each virus is described over two consecutive lines; the first of these lines contains a natural number `k` representing the length of this virus (expressed in bits), and the second line contains a string of length `k`, consisting only of the characters `0` and `1`, representing its description.

# Output data
The output file `virus.out` will contain exactly `N` lines. Each line will contain a natural value representing the number of occurrences of each known virus, in the order given in the input file.

# Constraints and clarifications
* `1 \leq N \leq 1\ 000`
* `1 \leq L \leq 100\ 000`
* `1 \leq k \leq 1\ 000`
* The total number of occurrences will not exceed `1\ 000\ 000`

# Example

`virus.in`
```
7 3
0110101
5
11111
1
0
3
101
```

`virus.out`
```
0
3
2
```

Explanation
---

There are `3` viruses. The first virus from the file, `11111`, does not appear in the bit string, so the value `0` will be written on the first line of the `virus.out` file. The second virus from the file, `0`, appears in the bit string `3` times (positions `1, 4`, and `6`), so the value `3` will be written on the second line of the `virus.out` file. The last virus from the file, `101`, appears in the bit string `2` times (starting at positions `3` and `5`), so the value `2` will be written on the third line of the `virus.out` file.