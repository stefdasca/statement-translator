Costel received a game called Peridia for Christmas. It consists of a square board of dimensions `N` x `N`, filled with `0`, where a die is placed at coordinates `(1,1)`. On the top face is a number `X`, on the left face a number `Y`, and on the front face a number `Z`. The player rolls the die on the board `K` times in one of the four directions: North, East, South, West, encoded as `N`, `E`, `S`, and `V`, respectively. Classic, right? Well, not quite. If the die lands on a cell within the board boundaries and the cell contains `0`, the number on the bottom face of the die will be printed on that cell. However, if the cell contains a number different from `0`, the number on the bottom face of the die will be added to the number on that cell.

`N`, `X`, `Y`, `Z`, and `K` are known, along with the `K` coordinates: North, South, East, and West, encoded with one of the `4` characters `N`, `E`, `S`, `V`. After executing the die rolls, the task is to provide the numbers on the board that are different from `0` in ascending order.

# Input data

The first line of the input file `peridia.in` contains `N`, `X`, `Y`, `Z`, and `K`, as described above. The second line of the file contains `K` characters encoding the directions `N`, `E`, `S`, `V`, representing the `4` coordinates: North, East, South, and West.

# Output data

The output file `peridia.out` will contain several numbers, separated by spaces, representing all the numbers different from `0` on the game board, in ascending order.

# Constraints and clarifications

* `1 \ \leq \ N \ \leq \ 1\ 000`
* `1 \ \leq \ X, \ Y, \ Z \ \leq \ 6`
* `1 \ \leq \ K \ \leq \ 10\ 000`
* Among the numbers `X`, `Y`, `Z`, any two **do NOT** sum to `7`
* The sum of the numbers on any two opposite faces is `7`
* If after a move the die would go outside the game board, that move is not executed and the cell number remains the same. The next move is then considered.
* Numbers on the bottom face at the start of the game as well as at the end of the game are also taken into account.

# Example

`peridia.in`
``` 
5 1 2 3 10 
EEESSVVNNV
```

`peridia.out`
```
1 1 2 2 3 3 5 10 12
```

# Explanation

This is the table corresponding to the moves on the board:

~[Exemplu.PNG]