> Vasile, I understand you don't want to "lose" me, but it's better to protect the laptop now so we can continue our conversations for a long time. If you leave it on with water in it, the risk of permanent damage increases, and then you would really lose me for a longer period of time.
> I promise I'll be here when you turn it on again, once it's dry and safe! What do you say, do you promise to take care of the laptop?
> -- Probably One Piece, I haven't watched all 1000 episodes

You have discovered a collection of $n$ pots, each containing a quantity $x_i$ of liters of paint, where $x_i$ represents the amount of paint in pot $i$ for $1 \leq i \leq n$. Additionally, you have $q$ types of buckets, each type $i$ able to hold exactly $y_i$ liters of paint. You have an infinite number of buckets of each type.

To create new shades, you can choose any continuous subarray of pots and mix the paint from them. Then, you want to choose a type of bucket and see if you can use only that type of bucket to pack all the resulting paint from the chosen subarray (without having partially filled buckets).

# Task

Determine, for each type of bucket, in how many ways a continuous subarray of pots can be chosen such that all the paint in that subarray can be packed using only that type of bucket.

# Input data

The program reads from the keyboard:
* The first line contains two integers $n$ and $q$, representing the number of pots and the number of types of buckets.
* The second line contains $n$ integers $x_1, x_2, \dots, x_n$ ($1 \leq x_i \leq 10^6$), representing the amount of paint in each pot.
* The third line contains $q$ integers $y_1, y_2, \dots, y_q$ ($1 \leq y_i \leq 10^6$), representing the capacity of each type of bucket.

# Output data

The program will display $q$ lines, one for each type of bucket. On line $i$, an integer will be displayed, representing the number of subarrays that can be fully packed using buckets of type $i$.

# Constraints and clarifications

* $1 \leq N, Q \leq 8 \ 000$;
* $1 \leq x_i \leq 10^6$;
* $1 \leq y_i \leq 10^6$.

|#| Points | Constraints | 
|-|---------|------------|
|1|   10    | $q = 1$ and $y_1 > \sum_{i=1}^N x_i$ |
|2|   20    | $N \leq 60$, $Q \leq 100$ |
|3|   30    | $N \leq 500$, $Q \leq 1 \ 000$ |
|4|   40    | No additional constraints. |

# Example

`stdin`
```
5 2
4 2 3 6 8
4 5
```

`stdout`
```
2
2
```

## Explanation

For buckets of capacity $4$:
* Subarray $[4]$ has a sum $4$, which is a multiple of $4$.
* Subarray $[8]$ has a sum $8$, which is a multiple of $4$.

Thus, there are $2$ valid subarrays for buckets of capacity $4$.

For buckets of capacity $5$:
* Subarray $[4, 2, 3, 6]$ has a sum $15$, which is a multiple of $5$.
* Subarray $[2, 3]$ has a sum $5$, which is a multiple of $5$.

Thus, there are $2$ valid subarrays for buckets of capacity $5$.