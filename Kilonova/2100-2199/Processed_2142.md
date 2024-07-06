Mugurel has finally decided to become the greatest entrepreneur in the "Rubber Duck Empire". Thus, he has started a business with his favorite fruits: oranges and bananas.

He receives the harvest plan of fruits: for $N$ days, each day Mugurel receives $M$ heaps of oranges and $M$ heaps of bananas, represented by their number of kilograms. Mugurel must pack all these fruits, but his box supplier offers him two options, from which he can choose only one: producing $K$ boxes for oranges and $K$ boxes for bananas (separate packing), or producing $K$ mixed boxes (packing oranges and bananas together). However, there are some rules regarding the packing:

* A box can contain only consecutive heaps of fruits (a heap must be placed in the box before another heap of the same type comes).
* A heap of fruits cannot be split into multiple heaps.
* Any open box must be closed at the end of the day (in short, a box cannot contain fruits from different days).
* Mixed boxes must contain the same number of heaps of oranges and bananas (not necessarily the same number of kilograms).

However, everything comes at a price. Let $c_{port}$, $c_{ban}$, $c_{mixt}$ be the capacities of the orange boxes, banana boxes, and mixed boxes, respectively. Then, Mugurel will pay $A \text{ maci} \cdot c_{port} + B \text{ maci} \cdot c_{ban}$ or $C \text{ maci} \cdot c_{mixt}$, depending on the chosen packing option. Mugurel will choose the packing method so that the total money spent is minimized.

After paying and receiving the boxes, the packing begins. Each time he closes a box, he places it at the end of the series of already closed boxes (Mugurel first takes care of the orange heap, then of the banana heap). At the end of fruit packing, he must split the series of boxes into two consecutive series, which we will call lots.

# Task

The lots will be sent to the two cities of the Empire, but Mugurel does not want to start a war between the two cities, so he wants to split them carefully. We call the **discrepancy** of a lot the difference between the box with the maximum number of kilograms and the one with the minimum number. The split must be made so that the sum of the **discrepancies** of the two lots is minimum, for packing.

With so many responsibilities, Mugurel asks for your help with the business.

# Input data

The first line contains two integers, $N$ and $M$, representing the number of days and the number of daily heaps.

The second line contains the integers $K$, $A$, $B$, $C$, representing the number of boxes that are manufactured of a certain type, as well as the prices of the three types of boxes.

The following $N$ lines contain $M$ integers each, representing the kilograms of orange heaps, in the order they arrive.

The following $N$ lines contain $M$ integers each, representing the kilograms of banana heaps, in the order they arrive.

# Output data

The first line will contain a single number, $S$, representing the total number of maci that Mugurel has to spend for all the boxes.

The second line will contain a single number, $T$, representing the total number of closed boxes with fruits.

The following $T$ lines will contain the details of the boxes in the order they were closed, with each line containing two values: the number of kilograms in the respective box, as well as the type of box, represented by a single character (`P` for oranges, `B` for bananas, `M` for mixed).

The last line will contain a single number, $D$, representing the minimum sum of the discrepancies of the two lots that can be obtained after a split of the series of boxes formed from the chosen packing.

# Constraints and clarifications

* $2 \leq N,M \leq 1\ 000$
* $N \leq K \leq N \cdot M$
* $1 \leq A,B,C \leq 10^6$
* Each fruit heap contains at most $10^6$ kilograms.
* Boxes of different types can have different capacities, but all boxes used for the same purpose (oranges, bananas, mixed) have the same capacity.
* It is not necessary for all boxes to be used (but the amount spent remains the same), so $T \leq K$ for mixed packing and $T \leq 2K$ for separate packing.
* Each lot must contain at least one box, but the smallest box can coincide with the largest box. It is guaranteed that the resulting series of boxes after packing consists of at least two boxes.
* If there are multiple correct solutions, any of them can be displayed.
* The mac is the official currency of the Rubber Duck Empire.
* For tests worth $5$ points, $K = N$.
* For other tests worth $5$ points, $K = N + 1$.
* For other tests worth $15$ points, all heaps have the same number of kilograms.
* For other tests worth $15$ points, $N,M \leq 100$, and the sum of the heaps from each day is $\leq 1\ 000$ kilograms.
* For other tests worth $30$ points, $K \leq 1\ 000$.
* For other tests worth $30$ points, there are no additional constraints.

# Example 1

`mugurel.in`
```
2 4
4 2 3 7
2 9 9 1
10 9 8 9
2 3 5 3
20 19 13 4
```

`mugurel.out`
```
98
8
11 P
10 P
13 B
20 B
19 P
19 B
17 P
17 B
6
```

## Explanation

In the first example, the cheapest will be to pack the fruits in separate boxes. One possible packing where we will spend a minimum amount of maci would be (with orange marking the oranges, and yellow the bananas):
~[img1.jpg|align=center|width=40em]

Following this packing, we obtain the following series of boxes:
~[img2.jpg|align=center|width=40em]

Thus, the capacity of the orange boxes will be $19 \text{ kg}$, and the capacity of the banana boxes will be $20 \text{ kg}$. The prices of the boxes are $2 \text{ maci/kg}$ for oranges and $3 \text{ maci/kg}$ for bananas, thus spending: $19 \cdot 2 + 20 \cdot 3 = 98 \text{ maci}$.

The optimal split into the two lots is given by the red line, obtaining the minimum sum of discrepancies: $3 + 3 = 6$.

# Example 2

`mugurel.in`
```
3 3
5 14 18 7
2 2 2
3 3 3
4 5 7
1 1 4
3 3 3
6 1 8
```

`mugurel.out`
```
112
5
12 M
6 M
12 M
16 M
15 M
7
```

## Explanation

In the second example, to spend as little money as possible, the fruits should be packed together. One possible packing would be:
~[img3.png|align=center|width=23em]

It can be observed that the number of orange heaps is equal to the number of banana heaps for each box. Thus, we obtain the following series of boxes:
~[img4.png|align=center|width=26em]

Thus, the capacity of the mixed boxes will be $16 \text{ kg}$. The price of the box is $7 \text{ maci/kg}$, thus spending: $16 \cdot 7 = 112 \text{ maci}$.

The optimal split into the two lots is given by the red line, obtaining the minimum sum of discrepancies: $6 + 1 = 7$.