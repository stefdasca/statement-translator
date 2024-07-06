Adela works at a pastry laboratory. She has to prepare two wedding cakes and for this purpose, she will use $n$ cake layers. The cake layers are cylindrical, all having the same height, but potentially different diameters. The cake layers come out of the oven one by one. When a layer comes out of the oven, Adela will place it on top of one of the two stacks of layers on the two trays where the cakes are being prepared.

The cake layers differ in their resistance to pressure. The resistance of a layer increases with the increase in diameter. Thus, a layer will support any number of other layers with diameters smaller than or equal to its diameter. On the other hand, if a layer with diameter $d$ is placed on top of another with a smaller diameter, then both the layer immediately underneath and all layers in the cake with diameters smaller than $d$ will collapse. The layer with diameter $d$ will stabilize on a layer with a larger or equal diameter or, if necessary, on the bottom of the tray.

Adela needs to use all $n$ layers to prepare the two cakes, and place them on the two trays in the order in which they come out of the oven. Adela's desire is for the total number of layers that will not collapse in the two cakes to be maximized.

# Task

Given the diameters of the layers and the order in which they come out of the oven, determine the maximum number of layers that will not collapse.

# Input data

The input file `torturi.in` contains:
- The first line contains the natural number $n$, representing the number of layers.
- The second line contains $n$ natural values: $d_1, d_2, \ldots, d_n$, not necessarily distinct, separated by a space, representing the diameters of the cake layers in the order in which they come out of the oven.

# Output data

The output file `torturi.out` contains:
- The first line contains a natural number representing the maximum number of layers that will not collapse in the two cakes.

# Constraints and clarifications

* $2 \leq n \leq 250\ 000$
* $1 \leq d_i \leq n$
* A cake layer can only be placed on top of another previously placed layer or directly on one of the two trays, if no layer has yet been placed on the tray.

# Example 1

`torturi.in`
```
5
1 3 4 2 1
```

`torturi.out`
```
4
```

## Explanation

The first optimal placement of layers is: $3 \ 2$ for the first cake and $4 \ 1$ for the second cake. The first layer that comes out of the oven with diameter $1$ will collapse.
The second option is: $3 \ 2 \ 1$ for the first cake and $4$ for the second cake.

# Example 2

`torturi.in`
```
5
3 5 3 2 4
```

`torturi.out`
```
5
```

## Explanation

The only optimal placement of layers is: $3 \ 3 \ 2$ for the first cake and $5 \ 4$ for the second cake. No layer collapses.