
# Task

Miki has finished preparing pickles for winter and now wants to label the $N$ jars he has filled. He has $K$ labels available, numbered from $1$ to $K$.

The labeling process of the jars will take place as follows:

* Initially, Miki chooses a jar with index $idx_1$ ($1 \leq idx_i \leq N$), and applies the label number $1$ to it $(e_{idx_1}=1)$;
* For each subsequent label, from $2$ to $K$, Miki selects a new jar with index $idx_i$ ($1 \leq idx_i \leq N$), in such a way that the difference between the indices of consecutive jars is exactly $1$ $(\lvert idx_i - idx_{i-1} \rvert = 1)$. The selected jar will receive the corresponding label number;
* If a selected jar already has a label, Miki will replace the existing label with the new one.

His friend, Denis, proposed a final labeling of the jars$^1$ - $e_1, e_2, \ldots, e_N$. Now, Miki is wondering in how many distinct ways he could achieve the proposed labeling, respecting the labeling process mentioned above$^2$. Help Miki calculate this number modulo $998\ 244\ 353$.

# Input data

The first line contains two integers $N$ and $K$ - the number of jars and the number of labels.

The second line contains $N$ numbers $e_1, e_2, \ldots, e_N$ - the labeling proposed by Denis.

# Output data

Print a single line containing a single integer - the number of distinct ways Miki can achieve the proposed labeling by Denis modulo $998\ 244\ 353$.

# Constraints and clarifications

* $^1$In case a jar with index $i$ remains unlabeled, its label will be $e_i=0$;
* $^2$A labeling process is considered different from another process if the order of the labeled jars is different;
* $2 \leq N \leq 5\ 000$;
* $1 \leq K \leq 10\ 000$;
* $0 \leq e_i \leq K$;
* If $i \neq j$, $e_i \neq 0$ and $e_j \neq 0$, then $e_i \neq e_j$;
* It is guaranteed that the labeling proposed by Denis is valid.

# Subtasks

|#|Points|Constraints|
|-|-|-----------|
|0|0|Example|
|1|13|$1 \leq N, K \leq 20$|
|2|21|$1 \leq N, K \leq 200$|
|3|26|$1 \leq N \leq 2\ 000$ and $1 \leq K \leq 5\ 000$|
|4|40|No additional constraints|

# Example 1

`stdin`
```
4 9
1 8 9 6
```

`stdout`
```
2
```

## Explanation

For the first example, there are two distinct labeling processes:

* $1\ 2\ 3\ 4\ 3\ 4\ 3\ 2\ 3$; 
* $1\ 2\ 3\ 2\ 3\ 4\ 3\ 2\ 3$. 

# Example 2

`stdin`
```
6 16
0 5 16 15 12 11
```

`stdout`
```
18
```
