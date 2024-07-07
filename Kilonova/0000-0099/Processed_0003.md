# Task

As part of a genetic engineering experiment, a group of researchers is conducting extensive analysis sets on a section of the human genome. The aim of the study is to select optimal sequences of hybridizations between two chromosomes.

The analyzed genome consists of $n$ chromosomes interconnected through unidirectional crossing-over mechanisms that allow efficient gene exchanges favoring mutations and overall genome evolution. Each crossing-over mechanism has a specific transfer coefficient, $c$, defined by the number of genes it can transfer at a time from chromosome $x$ to chromosome $y$.

The researchers are interested in a special pair of chromosomes, $u$ and $v$. A valid chromosome sequence is defined as a sequence that starts with chromosome $u$, ends with chromosome $v$, and does not contain the same chromosome twice. The task is to identify the first $k$ valid sequences in terms of the sums of the transfer coefficients.

Good luck!

# Input data

The first line of the input file `chromosome.in` contains the values: $n$ – the number of chromosomes per genome section, $m$ – the number of crossing-over mechanisms, $k$ – the maximum number of recombination sequences to be determined, $u$ and $v$ – the special pair of chromosomes.

The next $m$ lines each contain a triplet of the form $x$, $y$, $c$ defined as: there is a unidirectional transfer mechanism from chromosome $x$ to chromosome $y$ with a specific coefficient $c$.

# Output data

The first line of the output file `chromosome.out` will contain the value $r$ – the number of found combination sequences ($k$ or fewer), and the following lines the descriptions of the sequences:

- The first line of sequence $i$ will contain two values: $c_i$ – the cost of sequence $i$ and $p_i$ – the number of chromosomes involved in sequence $i$;
- The second line of set $i$ will contain the $p_i$ chromosomes in the order they appear in sequence $i$.

# Constraints and clarifications

- It is guaranteed for each test that there is at least one recombination sequence between chromosomes $u$ and $v$;
- The sequences will be displayed in ascending order of costs, and with equal costs in the [colexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order#Colexicographic_order) of the chromosomes involved;
- If there are not $k$ sequences, only the found ones will be displayed;
- $1 \leq n \leq 1\ 000$;
- $1 \leq m \leq 8\ 000$;
- $1 \leq c \leq 10\ 000$;
- $1 \leq k \leq 500$;
- $1 \leq u, v, x, y \leq n$.

# Example

`chromosome.in`
```
6 8 4 6 4
5 3 3
5 1 1
6 5 1
2 1 4
2 6 3
3 4 2
1 3 1
6 1 2
```

`chromosome.out`
```
3
5 5
6 5 1 3 4 
5 4
6 1 3 4 
6 4
6 5 3 4 
