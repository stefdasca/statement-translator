At the beginning of 2023, Gosu created a list of resolutions. Among the most important things Gosu wishes to achieve this year is reading $ N $ books on his bookshelf. Each book has a score assigned by a critic, a strictly positive integer. The list of scores is represented by $ A_1, A_2, \ldots, A_N $, where $ A_i $ represents the score of the $i$-th book on the shelf.

Gosu's list of resolutions contains strict rules that he wishes to follow. Among them is the restriction to read the books only once, in the exact order they are on the shelf. Although he is extremely motivated to fulfill all his resolutions, he is aware that it will not be easy. Therefore, he aims to maximize the benefits of reading by prioritizing books from his favorite literary genres. A literary genre is represented by a prime number $ p $. A book belongs to a literary genre $ p $ if its associated score is divisible by $ p $. A book can also belong to multiple genres.

In order to read as many books from his favorite genres as possible in case he abandons this resolution later, Gosu is willing to interchange any two books on the shelf to initially read the books with the highest score from a literary genre. Two books can only be interchanged if they have at least one literary genre in common.

# Task

Being an analytical and realistic person, Gosu imagines $ M $ scenarios in the form "After the first $ q $ books are read, what will be their maximum score sum after an unlimited number of interchanges between books from literary genre $ p $?". These are hypothetical situations, so the order of the books on the shelf is not actually modified during the queries. Find the answers in these situations, represented by independent queries in the form $ (p, q) $.

# Input data

The first line of input data contains a single integer $ N $, representing the number of books.

The next line contains $ N $ integers, separated by spaces, representing the list of scores associated with the books.

The third line of input contains a single integer $ M $, representing the number of queries.

The following $ M $ lines contain a query, represented by a pair of integers separated by a space, $ (p, q) $, where $ p $ is a prime number denoting the genre of books that can be interchanged, and $ q $ represents the number of books Gosu plans to read.

# Output data

The output file will display, on different lines, the answers to the queries.

# Constraints and clarifications

* $ 1 \leq N, M \leq 10^5 $;
* $ 1 \leq A_i \leq 10^6 $, $ 1 \leq i \leq N $;
* $ 1 \leq p \leq 10^6 $, $ p $ is a prime number;
* $ 1 \leq q \leq N $;
* Subtask 1 (20\%): For all queries, $ p = 2 $ and $ A_i $ is even, $ 1 \leq i \leq N $;
* Subtask 2 (20\%): For all queries, $ p = 2 $;
* Subtask 3 (20\%): $ 1 \leq N, M \leq 1 \ 000 $;
* Subtask 4 (40\%): No other restrictions.

# Example

`stdin`
```
10
5 3 33 2 9 8 10 11 10 7
4
5 4
11 5
2 6
7 5
```

`stdout`
```
48
52
70
52
```

## Explanation

The list of scores associated with the books is $ [5, 3, 33, 2, 9, 8, 10, 11, 10, 7] $ and we have 4 queries.

For the first query, by interchanging the first book with the ninth, we obtain the maximal score of the first 4 books to be 48. After the interchange, the list of books would become $ [10, 3, 33, 2, 9, 8, 10, 11, 5, 7] $.

For the second query, no interchange is necessary; the total score obtained is 52.

For the third query, two interchanges are necessary; for example, by interchanging the fourth book with the seventh, and then the sixth book with the ninth, the maximal score of the first 6 books is 70. The rearranged list of books is $ [5, 3, 33, 10, 9, 10, 2, 11, 8, 7] $.

In the last query, no interchange is possible since none of the first 5 books has an associated score divisible by 7. The sum of the scores is 52.