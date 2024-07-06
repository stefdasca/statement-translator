Sure! Here is your translated and formatted text in English:

```
Misopan and Trofonaced are two heroes who want to join forces in the fight against evil. The kingdom is represented by a rectangular matrix of `N` rows and `M` columns. Each element of the matrix corresponds to a piece of dry land or swamp. The two heroes do not venture into the swampy parts of the kingdom – they will only move on dry land. They can move from one position in the matrix to one of the `4` neighboring positions horizontally or vertically, if that position corresponds to a dry land area. Some dry land positions can be transformed by spell into swamps.

# Task
Help an evil wizard choose a minimum number of "transformable" positions, by changing which the two heroes cannot meet (there will be no land path between them).

# Input data
The first line of the `magic.in` file contains two integers `N` and `M` representing the number of rows and columns of the matrix. The next `N` lines contain `M` characters with the following meanings: 
* `.` - for a dry land position
* `x` - for a swampy position
* `*` - for a "transformable" dry land position into a swamp by the wizard 
* `M` - for the position of the hero Misopan
* `T` - for the position of the hero Trofonaced 

# Output data
The first line of the `magic.out` file will contain the integer `R`, representing the minimum number of positions that need to be transformed. On the following `R` lines will appear `2` numbers each, representing the chosen positions. The first number will be the row (between `1` and `N`), and the second will be the column (between `1` and `M`).

# Constraints and clarifications
* `1 \leq N, M \leq 50`
* `R` (the displayed result) can be `0`
* There will always be a solution for the given tests
* It is guaranteed that the characters `M` and `T` each appear exactly once in the entire matrix
* The positions of the heroes are implicitly dry land areas that cannot be transformed by the wizard

# Example

`magic.in`
```
4 4
MxxT
.x*.
.**.
**x.
```

`magic.out`
```
1
3 3
```
```

Please verify that all grammar and syntax are correct according to English language rules. Let me know if you need further assistance!