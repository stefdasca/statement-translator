# March

In Romania, March is the month we celebrate spring. According to tradition, on March 1st, we offer Martisor (a traditional Romanian amulet) to our loved ones. The "Spring Time" factory produces Martisor. These are packaged in boxes and placed in order on a conveyor belt. Each box has a label with the number of Martisor in that box. Tommy is the manager of this store, and he is responsible for labeling the boxes. To be more efficient, Tommy creates the labels on a computer, and each time he obtains the number that needs to be written on a box from the previously written number (except for the first number), using as few operations as possible of the type: $I(k,c) = insert digit c at position k$; $D(k) = delete digit at position k$; $C(k,c) = replace the digit at position k with digit c$. For obtaining the first number, only insertion operations are performed. Tommy also has to manage the orders he receives. For each order, Tommy knows the number of Martisor ordered. He has to send the requester boxes with Martisor, placed consecutively on the belt, so that the number of Martisor sent is at least equal to the number of Martisor ordered.

## Input data

The input file `march.in` contains on the first line a natural number $v$ representing the task that needs to be solved $(1,2$ or $3)$. The second line contains the natural numbers $n$ and $m$, as specified in the description. The following line contains $n$ natural numbers, separated by space, representing the numbers written on the boxes, in the order they are placed on the belt.

## Output data

If the task is $v = 1$, then the first line of the file `march.out` will contain a natural number representing the minimum number of operations Tommy needs to perform to label all $n$ boxes. If the task is $v=2$, then the output file `march.out` will contain, on the first line, a natural number representing the number of distinct ways in which Tommy can honor the order. If the task is $v=3$, then the output file `march.out` will contain, on the first line, a natural number representing the minimum number of boxes that can be sent, so that the order can be fulfilled.

## Constraints and clarifications

$2 \leq n \leq 1000$

$1 \leq m \leq$ the label of any box is a natural number within the range

two ways to honor the order are distinct if the sequence of the box numbers in the order differs;

$m \leq$ the number of Martisor in the $n$ boxes;

For $50\%$ of the tests, the task is $1$,

for $30\%$ of the tests, the task is $2$, and

for $20\%$ of the tests, the task is $3$.

## Example

`march.in`

`1 5 3500 1234 3134 313 143 123`

`march.out`

`10`

`march.in`

`2 5 3500 1234 3134 313 143 123`

`march.out`

`6`

`march.in`

`3 5 3500 1234 3134 313 143 123`

`march.out`

`2`

## Explanation

For the first example:

To write the $5$ numbers, a minimum of $10$ operations are used:

For the second example:

There are $6$ ways to honor the order of $3500$ Martisor:

$1234 + 3134$

$1234 + 3134 + 313$

$1234 + 3134 + 313 + 143$

$1234 + 3134 + 313 + 143 + 123$

$3134 + 313 + 143$

$3134 + 313 + 143 + 123$

For the third example:

To fulfill the order, at least $2$ boxes need to be sent ($1234 + 3134$)