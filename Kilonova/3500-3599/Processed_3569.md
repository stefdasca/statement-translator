
# Task

You are given a text consisting of lowercase alphabetic letters and spaces. The text is arranged in a rectangular grid with $N$ rows and $N$ columns, one character in each position. We consider a word to be a maximal sequence of letters located on the same row, in consecutive positions.

Rules for the text:
- There are no consecutive spaces.
- There are no spaces at the beginning or the end of a row.
- All rows are complete, including the last one.

**Cursor position**: The cursor is always positioned on a character (either a letter or a space).
- At the beginning of a row means on the first character of that row.
- At the end of a row means on the last character of that row.

The cursor can move with the following operations, each operation has **cost 1**:
1. **Arrows** (left, right, up, down): the cursor moves by one character in the respective direction.
2. **Ctrl + Left/Right Arrow**: the cursor moves to the beginning of the previous/next word on the same row.
3. **Home**: the cursor moves to the first character of the current row.
4. **End**: the cursor moves to the last character of the current row.

Special conditions for cursor movement:
- If we are at the end of the row and press **right arrow** or **Ctrl + right arrow**, the cursor stays in place.
- If we are at the beginning of the row and press **left arrow** or **Ctrl + left arrow**, the cursor stays in place.
- If we are on any character of a word and press **Ctrl + right arrow**, we move to the first character of the next word on the same row (if it exists). Otherwise, the cursor stays in place.
- If we are on the first character of a word and press **Ctrl + left arrow**, we move to the first character of the previous word (if it exists). Otherwise, the cursor stays in place.
- If we are on a character inside a word (not the first), and press **Ctrl + left arrow**, we move to the first character of that word.

The initial position of the cursor is known, and we want to move it to a final position, also known, with a minimum number of operations.

# Input data
The file `editsmart.in` contains on the first line a number $N$ representing the size of the given matrix (which is a square). On each of the $N$ lines, there are $N$ characters which can be spaces or lowercase alphabetic letters. On the next line, there are $4$ numbers $x_{start}, y_{start}, x_{end}, y_{end}$ representing respectively the row and column of the initial cursor position and then the row and column of the final position.

# Output data
The file `editsmart.out` will contain a single value, representing the minimum number of operations needed to move the cursor from the initial position to the final position.

# Constraints and clarifications

* $3 \leq N \leq 1 \ 000$
* For $24$ points, $3 \leq N \leq 100$
* For $12$ points, the given text will **not** contain any spaces.
* For $8$ points, the starting position and the final position will be on the same row.
* For $5$ points, the starting position and the final position will be in the same column.
* For the remaining $51$ points, there are no additional restrictions.

# Example

`editsmart.in`
```
6
abc xy
a bc t
abcdef
abc pf
xbcdef
xbcdef
5 2 3 5
```

`editsmart.out`
```
3
```

## Explanation

We start from position $(5, 2)$. With an up arrow operation, we move to position $(4, 2)$, where the character `b` is on row $4$. Next, we use the Ctrl+right arrow operation and move to character `p` at position $(4, 5)$. Finally, we press the up arrow from this position and reach the final location.
```
