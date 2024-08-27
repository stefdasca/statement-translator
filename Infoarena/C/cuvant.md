# Word

Victoras has cut out several letters from the newspaper. He's wondering how many distinct words of length $L$ he can form from the letters he has available. Since the result can be quite large, it will be displayed modulo $666013$.

## Input data

The input file `cuvant.in` contains on the first line the natural number $T$ representing the number of tests. Then follows the description of the $T$ tests. Each test consists of two lines. The first line contains a string of at most $10000$ lowercase letters of the English alphabet. The second line contains the natural number $L$ with the significance described in the statement.

## Output data

The output file `cuvant.out` will contain for each test one line with the obtained result.

## Constraints

$1 \leq T \leq 5$

$1 \leq L \leq 1000$

## Example

`cuvant.in`

```
1
aab
3
```

`cuvant.out`

```
3
```

## Explanation

The words $aab$, $aba$, $baa$ are obtained.