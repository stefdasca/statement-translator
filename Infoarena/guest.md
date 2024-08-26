# Guest

Your fellow villager, Dorel, owns a hotel and, like all hoteliers, he wants to maximize his profit. His hotel can be visualized as a sequence of $N$ rooms, some occupied, some empty, from $1$ to $N$. The life of a hotelier, however, is not so simple. From time to time, he needs to free up a room for various reasons (e.g., the arrival of a VIP, or maybe pest control). In this case, he moves the person from that room to another room, then moves the person from that room to another room, and so on, until he moves a person into an empty room. Of course, if the room is already empty, he has nothing to do. The displaced guests clearly dislike this procedure and will thus negotiate a monetary compensation for the trouble caused. Each guest has a certain natural positive negotiation skill $S$, and with it, they will be able to negotiate compensation of $S * x$ Swiss francs if they are moved $x$ rooms to the right or left. Dorel tells you that if you help him predict what the total compensation would be if he were forced to free up each room, he will pay you 10% of all his profits for the next month. Can you help him?

## Task

## Input data

The input file `guest.in` will contain on the first line $T$ the number of tests in the file. Next will follow the descriptions of the $T$ tests. On the first line of each test, the number $N$ will be found. On the next line, $N$ numbers will be found. If the $i$-th number is equal to a nonzero natural number $x$, then the $i$-th room contains a guest with a negotiation skill equal to $x$. Otherwise, if the $i$-th number is equal to $0$, then the $i$-th room is empty.

## Output data

The output file `guest.out` will contain $T$ lines, the answers for the $T$ tests. The answer for a test is calculated as follows. If the cost to free the $i$-th room is $r_i$, then the answer is $(r_1 * 29^{(n-1)} + r_2 * 29^{(n-2)} + \dots + r_n * 29^0) \mod 1\ 000\ 000\ 007$. We suggest using the following code to transform the array $r$ into the answer for the test:
```cpp
/* the function takes r as an array of long long indexed from 1, and n, and returns the answer */
long long calculate_answer(long long r[], int n){
    long long ret = 0;
    for(int i = 1; i <= n; ++i){
        ret = (29 * ret + r[i]) % 1000000007ll;
    }
    return ret;
}
```

## Constraints and clarifications

$1 \leq T \leq 10$ 

$1 \leq N \leq 100\ 000$ 

$1 \leq x \leq 1\ 000\ 000\ 000$ 

There is at least one empty room for each test.

## Example

guest.in 
```
3
8
0 1 3 5 5 4 2 0
4
0 5 8 1
4
1 0 0 1
```
guest.out 
```
683506829
4527
24390
```

## Explanation

The arrays $r$ for the tests are:

For the first test: $0\ 1\ 4\ 9\ 11\ 6\ 2\ 0$

For the second test: $0\ 5\ 11\ 3$

For the third test: $1\ 0\ 0\ 1$