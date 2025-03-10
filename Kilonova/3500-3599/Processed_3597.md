Certainly! Below is the translated competitive programming problem statement in English, with the specified rules applied:

---

**Liverpool Football Team** is training intensively to win the championship, and the coach, Arne Slot, monitors the players' passes during training. Each pass is coded as follows:
* `P`: precise pass, executed correctly; 
* `G`: faulty pass, executed incorrectly. 

The coach offers players the chance to correct **at most two faulty passes**, transforming them into precise passes.

Help Arne Slot determine, from a sequence of $N$ passes:
1. **The longest continuous sequence of precise passes** that can be obtained after correcting at most two faulty passes.
2. **The starting index of this sequence** (starting from $1$).

# Task

Write a program that determines and displays the maximum length of a sequence of precise passes, as well as the starting index of this sequence. The length of the longest sequence is determined after correcting at most two faulty passes.

# Input data

The input file `pase.in` contains on the first line the natural number $N$, representing the total number of passes, then on the next line, the string of characters representing the sequence of precise or faulty passes, represented by the letters `P` (precise pass) and `G` (faulty pass). 

# Output data

The output file `pase.out` contains on a single line two natural numbers, separated by a space, representing the maximum length of the sequence of precise passes, and the starting index of this sequence, which is obtained after correcting at most two faulty passes. If there are multiple sequences of maximum length, the leftmost sequence will be chosen.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000$;
* The string in the input file contains only the letters `P` and `G`;
* The indices of the letters in the string start from $1$;
* Each pass string contains at least two faulty passes. 

# Example 1

`pase.in`
```
9 
PPGPGPPPG
```

`pase.out`
```
8 1
```

## Explanation

After correcting the two faulty passes (the third and fifth letters in the string, representing the first and second `G` letters), the string becomes `PPPPPPPPG`.

# Example 2

`pase.in`
```
10 
PGPGGPPPPG
```

`pase.out`
```
7 3
```

## Explanation

After correcting two faulty passes (the fourth and fifth letters in the string), the string becomes `PGPPPPPPPG`.

--- 

I hope this translation meets your expectations! Please let me know if you need further adjustments.