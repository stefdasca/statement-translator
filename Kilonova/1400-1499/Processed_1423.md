Scooby-Doo, the famous cartoon character, has gotten into trouble again. He is now in a rectangular room with dimensions \( n \cdot m \) made up of square cells with side \( 1 \), variously colored.

Definitions:

* **Zone** - as a group with a maximum number of cells of the same color, adjacent by row or column.
* **SUPERZONE** - as a set \( A \) of zones, with the property that each zone has at least \( k \) neighboring zones in the same set \( A \).

To be safe, Scooby-Doo needs to find shelter in a **SUPERZONE** with the **maximum number** of cells in the matrix.

# Task

Abandoned by his friends, Scooby-Doo can't manage on his own and asks you to solve the mystery and calculate the number of cells of the largest **SUPERZONE** in the matrix.

# Input data

The input file `zone.in` contains on the first line the natural numbers \( n, m \) and \( k \) separated by spaces. On the next \( n \) lines there are \( m \) characters, without spaces between them, representing the color of each cell in the matrix.

# Output data

The output file `zone.out` will contain on the first line a natural number representing the number of cells of the largest **SUPERZONE** in the matrix.

# Constraints and clarifications

* \( 2 \leq n, m, k \leq 300 \)
* Colors are represented by lowercase English alphabet letters (`a` - `z`)
* Two cells are considered adjacent if they share a common side
* Two zones are considered neighbors if they each have at least one adjacent cell

# Example

`zone.in`
```
4 3 2
aaa
bad
baa
cda
```
`zone.out`
```
11
```

# Explanation

The entire matrix is selected minus the zone formed by the letter `d` on the last column.