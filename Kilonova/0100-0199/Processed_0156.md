Below is the translated competitive programming problem statement from Romanian to English while preserving the format, structure, and custom image syntax:

---

Fie expresia: $log_{a_1}b_1 \cdot log_{a_2}b_2 \cdot \ldots \cdot log_{a_n}b_n$

A calculator needs to evaluate this expression by reducing it to a single real number. For this, it can perform the following calculations:
- Product = the product of two real numbers in $t_1$ units of time;
- Reduction = replacing the expression $log_ab \cdot log_bc$ with $log_ac$ in $t_2$ units of time;
- Calculation = calculating a logarithm, the result being a real number; to calculate $log_ab$, it takes $t_3 \cdot (a-b)^2$ units of time.

# Task
Determine the minimum time to compute a given expression.

# Input data
The file `log.in` contains:
- the first line contains a natural numeric value `n` as described in the statement;
- the second line contains three natural numeric values $t_1 t_2 t_3$ separated by spaces, as described in the statement;
- each of the next `n` lines contains two natural numeric values $a_i b_i$ as described in the statement.

# Output data
The file `log.out` must contain a single value representing the number of units of time needed to evaluate the expression.

# Constraints and clarifications
* For `70%` of the tests, `0 < n \leq 500`; for the other `30%` of the tests, `n \leq 10000`;
* $1 < a_i, b_i < 100$
* $1 \leq t_1, t_2, t_3 \leq 100$
* The factors of the initial expression or of any intermediate expression during the evaluation **CANNOT** be commuted.

# Example

`log.in`
```
3    
2 1 3
2 3
3 4
4 5
```

`log.out`
```
13
```
Explanation 
---

Each of the three logarithms is calculated, resulting in three numbers, each calculation taking `3` units of time; the first two numbers are multiplied in `2` units of time, then the result is multiplied by the third number also in `2` units; in total: `3+3+3+2+2=13` units of time.

`log.in`
```
4    
2 1 2
2 2
3 4
4 4
4 5
```

`log.out`
```
9
```

Explanation 
---
The first logarithm is calculated in `0` units; the second and third are reduced to one logarithm in `1` unit, and this logarithm is calculated in `2` units; the fourth is calculated in `2` units; three numbers result, which can be reduced to one single number through two multiplications, taking `1+2+2+2+2=9` units of time.