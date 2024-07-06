Little Prince arrived in the land of palindrome numbers with an odd number of digits where he received from the king's advisor a list containing \(N\) natural numbers, each with an odd number of digits. A number is a palindrome if its first digit is equal to the last one, the second to the penultimate one, and so on. The advisor informed him that the king is very ill. Along with the king, the numbers on the list also became "ill". The advisor told him that the correct list can be obtained by replacing each number in it with the smallest palindrome greater than or equal to that number.

After following the advisor's recommendation, Little Prince noticed that in the obtained correct list, all the palindromes are distinct. Looking more closely at the palindromes in this list, he observed that there are pairs of palindromes where the smaller one can be obtained from the larger one by removing the same number of digits from both ends. For example, for the pair \(7531357\) and \(313\), the palindrome \(313\) is obtained from \(7531357\) by removing two digits from both ends.

We consider a sequence of palindromes from the correct list and denote by \(X\) the maximum value of this sequence. We will say that the sequence is magical if all the palindromes in it can be obtained by the method described above, from the palindrome of value \(X\). An example of a magical sequence is \(4, 53435, 7534357, 89753435798\), assuming that all these numbers are in the correct list.

# Task

Write a program that reads the numbers from the list received from the king's advisor and displays:

1. The correct list obtained by Little Prince;
2. The number of elements in the longest magical sequence that can be obtained from the correct list;
3. The palindromes that make up the longest magical sequence, displayed in ascending order. If there are multiple such sequences in the correct list of Little Prince, the one ending in the largest number will be displayed.

# Input data

The input file `pal.in` contains on the first line the natural number \(P\), which can only have the values \(1, 2,\) or \(3\) and indicates the number of the task to be solved. The second line contains the natural number \(N\) representing the number of numbers on the list received from the king's advisor. The third line contains the natural numbers from the list received from the advisor, separated by spaces.

# Output data

The output file `pal.out` will contain on the first line the response to the solved task. If the first task is solved, the output file will contain an array of \(N\) natural numbers, separated by spaces, representing the numbers from the correct list, in the order corresponding to the initial list. If the second task is solved, the first line of the output file will contain the length of the longest magical sequence. If the third task is solved, the output file will contain the determined numbers displayed according to the task.

# Constraints and clarifications

* \(0 < N \leq 50\ 000\);
* The numbers on the advisor's list are nonzero natural numbers and each has at most \(17\) digits;
* For a correct solution to the first task, \(20\) points are awarded, for a correct solution to the second task, \(20\) points are awarded, and for a correct solution to the third task, \(50\) points are awarded.

# Example 1

`pal.in`
```
1
3
345 214 64325
```

`pal.out`
```
353 222 64346
```

## Explanation

The palindrome sequence from the correct list obtained by Little Prince.

# Example 2

`pal.in`
```
2
8
2 3 120 4 432 5643461 7 21211
```

`pal.out`
```
3
```

## Explanation

The correct list contains the palindromes \(2 \ 3 \ 121 \ 4 \ 21212 \ 434 \ 5643465 \ 7\) and the longest magical sequence is \(3 \ 434 \ 5643465\).

# Example 3

`pal.in`
```
3
8
2 3 5643461 7 120 4 21211 432
```

`pal.out`
```
3 434 5643465
```

## Explanation

The magical sequence \(2 \ 121 \ 21212\) has the same length but ends with a smaller number.