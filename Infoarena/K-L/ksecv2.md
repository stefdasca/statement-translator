## Ksecv2

After getting bored of driving in Viteza2, Mirel went to the supermarket to do his shopping. Having spent a lot of time driving around the city, he realized he needed many products from the supermarket and that he only had $K$ shopping bags (the supermarket he usually goes to does not sell bags). There, he picks out his products, takes them to the cashier to get a bill, and then goes to the end of the checkout lane to bag the items in the order they come. Each purchased item has a fragility represented by an integer; the higher the number, the more fragile the item. The bags available are enormous and can hold any number of purchased items, but the items need to be stacked on top of each other. Unfortunately, if a less fragile item is placed on top of a more fragile one, the latter will break. Mirel realizes that because of this, he cannot take home all the products he brought to the checkout and, being impatient, he uses a simple strategy. For each incoming item, he acts as follows:
1. If he wants, he can tell the cashier he will return for it later.
2. If he can place it in the last bag without breaking anything, he does so.
3. Only if he cannot place it in the last bag, he puts the bag aside and takes a new one to place this item in it.

He wants to take home as many of the selected products as possible, so he asks you to tell him the maximum number of products he can keep, while for the rest, he will have to return later. If he cannot fill all $K$ bags using his strategy, he will return to the store to select more products.

## Input data

The input file `ksecv2.in` contains on the first line $N$ and $K$ representing the number of products and the number of bags Mirel has, respectively. The next line contains $N$ integers representing the fragility of the items in the order they come to Mirel.

## Output data

The output file `ksecv2.out` must contain a single natural number representing the maximum number of products he can take with the $K$ bags using the described strategy, or $-1$ if he cannot fill the $K$ bags with the selected strategy.

## Constraints

$1 \leq N \leq 3000$

$1 \leq K \leq 500$

$-1\ 000\ 000\ 000 \leq$ fragility of an item $\leq 1\ 000\ 000\ 000$

For 40% of tests:

$1 \leq N \leq 500$

$1 \leq K \leq 100$

For another 30% of tests:

$1 \leq N \leq 2000$

$1 \leq K \leq 200$

## Example

`ksecv2.in`
```
5 3
10 10 4 0 -8
```

`ksecv2.out`
```
4
```

`ksecv2.in`
```
3 2
1 2 3
```

`ksecv2.out`
```
-1
```

## Explanation

For the first example: Mirel can keep the products with indices $(1, 2)$, $(3)$, and $(5)$ or $(1, 2)$, $(3)$, and $(4)$ (In parentheses, we marked how Mirel puts the products in bags)

For the second example: Whatever part of the products Mirel takes, he can fill at most one bag following his strategy, so he will return to select more products.