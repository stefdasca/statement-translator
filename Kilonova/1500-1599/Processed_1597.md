Alexandra reads a text composed of lowercase and uppercase English letters and spaces. Being interested in cryptography, she removes all spaces and then frames the letters, in the order they appear in the text, into a two-dimensional array, where the number of rows is less than or equal to the number of columns. Since there can be multiple ways to frame the text, Alexandra chooses the one for which the absolute difference between the number of rows and the number of columns in the array is minimal. Filling the two-dimensional array with the text letters is done in ascending order of rows and within each row, in ascending order of columns.

# Task

1. Denoting with $N$ the number of rows and with $M$ the number of columns of the obtained two-dimensional array, display its elements on the first $N$ lines of the output file, each line containing exactly $M$ letters without spaces between them. The display will be in ascending order of row indices and within each row in ascending order of column indices.
2. Determine the longest palindrome on a row or column of the obtained array. In case there are multiple palindromes of the same length, the lexicographically largest one according to the ASCII code will be displayed.
3. Determine the maximum number of elements in a rectangular subarray that contains only vowels.

# Input data

The input data is read from the file `text.in`, which has the following structure:

* The first line contains the natural number $C$ which can have the values $1, 2,$ or $3$, indicating the number of the requirement to be solved;
* The second line contains the text that Alexandra will process.

# Output data

The output data will be displayed in the file `text.out`, which has the following structure:

* If $C = 1$, $N$ lines, each containing $M$ letters, representing the elements of the obtained array;
* If $C = 2$, a single line containing the longest determined palindrome;
* If $C = 3$, a single line containing a natural number representing the number of elements in the determined subarray.

# Constraints and clarifications

* $2 \leq$ the total number of characters in Alexandra's initial text $\leq 200\ 000$;
* The vowels are: `A`, `E`, `I`, `O`, `U`, `a`, `e`, `i`, `o`, `u`
* It is guaranteed that $N$, the number of rows of the obtained array is $> 1$.
* For $16$ points, $C = 1$ and the number of characters in the initial string $\leq 10\ 000$;
* For $36$ points, $C = 2$ and the number of characters in the initial string $\leq 1\ 000$;
* For $16$ points, $C = 3$ and the number of characters in the initial string $\leq 1\ 000$;
* For $16$ points, $C = 3$ and the number of characters in the initial string $\leq 50\ 000$;
* For $16$ points, $C = 3$, with no additional restrictions.

# Example 1

`text.in`
```
1
Ana nu are mere
```

`text.out`
```
Anan
uare
mere
```

## Explanation

The number of characters after removing spaces is $12$. The text placed in the array contains $N = 3$ rows and $M = 4$ columns.

# Example 2

`text.in`
```
1
A fost odata ca niciodata
```

`text.out`
```
Afostod
atacani
ciodata
```

## Explanation

The number of characters after removing spaces is $21$. The text placed in the array contains $N = 3$ rows and $M = 7$ columns.

# Example 3

`text.in`
```
2
A fost odata ca niciodata
```

`text.out`
```
oao
```

## Explanation

$\text{Afostod}$
$\text{atacani}$
$\text{ciodata}$
The array has the palindrome `oao` in column $3$ and the palindrome `ata` in rows $2$ and $3$.

# Example 4

`text.in`
```
3
Aceasta oaie e alba
```

`text.out`
```
6
```

## Explanation

$\text{Ac\textcolor{blue}{ea}}$
$\text{st\textcolor{blue}{ao}}$
$\text{ai\textcolor{blue}{ee}}$
$\text{alba}$