We say that the non-zero natural number $n_1$ can _attach over $K$ bits_ with the non-zero natural number $n_2$ if their binary representations each have at least $K$ bits (with the first bit being $1$), and the last $K$ bits of the number $n_1$ coincide with the first $K$ bits of the number $n_2$. After attachment, another number results, formed by concatenating $n_1$ with $n_2$, but in which the common sequence of $K$ bits appears only once and each bit in it is replaced with its complement (0 becomes 1 and vice versa).

_Example:_ The number $78$ = $1001110_2$ _can attach over $3$ bits_ with $25$ = $11001_2$ resulting in the number $100100101_2 = 293$.

The numbers $nr_1$, $nr_2$, $\dots$, $nr_M$ form a list of attachments over $K$ bits, of length $M \geq 1$, ending with $P$, if $nr_1$ attaches over $K$ bits with $nr_2$, the result attaches over $K$ bits with $nr_3$, $\dots$, the result attaches over $K$ bits with $nr_M$, and the final result is the number $P$. _Note:_ If $M = 1$, then we must have $nr_1$ = $P$.

# Task

For a given sequence of non-zero natural numbers and the non-zero natural values $K$ and $P$, it is required: 

a) to determine the maximum length of a list of attachments over $K$ bits, formed with elements from the given sequence, not necessarily in the order of this sequence;  
b) to verify if it is possible to obtain, with numbers from the given sequence, a list of attachments over $K$ bits ending with $P$; if affirmative, to specify a list of minimal length of attachments over $K$ bits ending with $P$.

# Input data

Input file: `alipiri.in`

* Line 1: $N \; K \; P$ - three non-zero natural numbers, separated by a space, representing the number $N$ of given numbers, the length $K$ of common sequences in attachments, and the value $P$ of the number that must be obtained through attachments;
* Line 2: $nr_1 \; nr_2 \; \dots \; nr_N$ - $N$ non-zero natural numbers, separated by a space, representing the given sequence.

# Output data

Output file: `alipiri.out`

* Line 1: $M$ - non-zero natural number, representing the result for task $a)$; 
* Line 2: _message_ - if task $b)$ can be satisfied, this line will contain `YES`, otherwise it will contain `NO`; 
* Line 3: $nr_1 \; nr_2 \; \dots$ - if on line 2 you wrote 'YES', on this line will be written a list of attachments (over $K$ bits) of minimum length ending with $P$; the numbers in the list will be separated by a space.

# Constraints and clarifications

* $1 \leq K \leq 8$;
* $1 \leq N \leq 9$;
* $1 \leq P \leq 2 \cdot 10^9$;
* if task $b)$ is satisfied by multiple lists (of minimum length), only one will be written in the file.
* for both tasks, each number in the input sequence can appear at most once in the considered attachment lists.
* **Note:** Partial scores are awarded: $a) \; 40\%; \; b) \; 60\%$

# Example

`alipiri.in`
```
4 3 291        
14 59 36 31
```

`alipiri.out`
```
4
YES
59 31 14
```
