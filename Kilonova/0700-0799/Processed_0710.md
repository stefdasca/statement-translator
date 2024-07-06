The primary mission of a scientific expedition is to study the evolution of life on a newly discovered planet. Following the conducted studies, researchers have associated a characteristic code with each living organism discovered on that planet. The characteristic code is a natural number of up to $200$ non-zero decimal digits.

Researchers have also observed that for any living organism on the planet, the characteristic codes of its ancestors on the evolutionary scale can be obtained by deleting some digits from the characteristic code of the respective organism, and an organism is more evolved if its characteristic code has a higher value.

# Task

Given the characteristic codes of two different living organisms, write a program that determines the characteristic code of their most evolved common ancestor.

# Input data

The input file `cod.in` contains:

* $n$ - the characteristic code of the first organism
* $m$ - the characteristic code of the second organism

# Output data

The output file `cod.out` contains on the first line:

* $p$ – the characteristic code of the most evolved common ancestor of $n$ and $m$

# Constraints and clarifications

* The characteristic code is a natural number of up to $200$ non-zero decimal digits.

# Example

`cod.in`
```
7145
847835
```

`cod.out`
```
75
```