**XORin** is dissatisfied with the problems received on the first day of the competition at the National Informatics Olympiad and thus decides to join the committee. Soon he becomes the committee's specialist in generating tests consisting of sequences of numbers. From time to time he has to add or remove elements from the sequence. Sometimes he decides to re-add previously deleted elements. Let the sequence of numbers be $a=(a_1, a_2, \ldots, a_N)$ and $N$ the number of elements in the sequence after each operation.

Thus, he has to perform the following operations starting from an empty sequence:

* Insert a value $x$ at the end of the sequence;
* Remove the last $x$ elements from the sequence;
* Re-add to the end of the sequence the first $x$ deleted elements. If, for example, in the previous delete operation of a number $y$ of elements, the elements $a_{N-y+1}, a_{N-y+2}, \ldots, a_N$ were deleted, and now a re-add operation of $x$ elements is to follow, the elements $a_{N-y+1}, a_{N-y+2}, \ldots, a_{N-y+x}$ will be added in order at the end of the sequence.

From time to time **XORin** asks himself the following question: how many times does the value $x$ appear in the sequence?

# Input data

The first line of the file `undo.in` will contain $M$ which represents the number of operations.

The following $M$ lines will contain the operations encoded as follows:

* `1 x` - insert the element $x$ at the end of the sequence
* `2 y` - remove the last $y` elements added to the sequence
* `3 z` - re-add to the end of the sequence the first $z$ deleted elements
* `4 t` - print the number of elements with the value $t$ in the sequence

# Output data

Each line of the file `undo.out` will contain the answers to **XORin**'s questions, each answer on a separate line.

# Constraints and clarifications

* All numbers in the input file are between $1$ and $200\ 000$;
* For $20\%$ of the tests it is guaranteed $M \leq 1\ 000$, for another $40\%$ of the tests, it is guaranteed that the inserted numbers will be distinct;
* Between a re-add operation and the previous delete operation, there will be no insert operations.
* The number of re-added elements will not be greater than the number of elements removed in the last operation.
* Between two re-add operations there will be at least one delete operation.

# Example

`undo.in`

```
16
1 1
1 2
1 3
1 4
4 4
2 2
4 3
3 1
4 4
4 3
1 7
1 7
1 7
4 7
2 2
4 7
```

`undo.out`

```
1
0
0
1
3
1
```

## Explanation

Initially, the sequence is empty.

After the first $4$ insert operations, the sequence is `1, 2, 3, 4`.

Operation `4 4` will display $1$.

Operation `2 2` will remove the last two elements, the sequence becoming `1, 2`.

Since the element $3$ was removed, the seventh operation will display $0$.

Operation `3 1` will re-add the element $3$ at the end of the sequence.

As a result of this operation, the sequence becomes `1, 2, 3`.

Operation `4 4` will display $0$, and operation `4 3` will display $1$.
And so on.