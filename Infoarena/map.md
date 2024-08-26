# Map

Max Damage, in order not to get lost in his travels, wants to make a map. To prevent it from being read by anyone, he encodes it in the form of a matrix with $N$ rows and $M$ columns. Because he has poor handwriting, he goes to a friend who has a printer and asks him to print the map. The printer, being old, is broken and prints the map twice on the same sheet, but with an offset (to the right). The police arrive and Max flees with the poorly printed sheet. At his hideout, he sees the disaster: the portion where the two prints overlapped happened to coincide, so he cannot tell where one ends and the other begins. He now wants a program that, given such a matrix, returns the smallest dimension of the original matrix such that, when overlaid twice with the correct right offset, the final map is obtained. Help Max solve this overwhelming problem.

## Task

## Input data

The first line of the file `map.in` will contain the numbers $M$ and $N$, representing the dimensions of the matrix. The next $M$ lines will contain $N$ lowercase letters of the English alphabet each (the poorly printed matrix).

## Output data

The file `map.out` will contain a single value on the first line, representing the minimum horizontal dimension of the original matrix.

## Constraints and clarifications

$1 \leq N$

$M \leq 2000$

## Example

`map.in` 
```
3 5
anana
arara
mamam
```

`map.out` 
```
3
```

## Explanation

Starting with the matrix of length $3$

```
ana
ara
mam
```

overlaid twice, we get:

```
anana
arara
mamam
```

`map.in` 
```
1 4
abcd
```

`map.out` 
```
4
```

## Explanation

The only solution is for the second print to be perfectly overlaid on the first.

`map.in` 
```
1 4
aaaa
```

`map.out` 
```
3
```

## Explanation

If the length were smaller, it would not overlap.