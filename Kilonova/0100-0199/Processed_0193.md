In a wonderful country, the `N` cities are connected by `N-1` roads such that any city can be reached from any other city. The fuel costs required to travel each road and the entry costs into each city are known. Țirbi, the postal manager, needs to choose the post office headquarters, knowing that he will have to deliver parcels to `M` specified cities, starting from and returning to the headquarters after delivering the parcels.

He needs to choose the headquarters in such a way as to minimize the transportation costs, given that the post office will have a contract with the government which exempts it from:
* all entry fees in the city where the headquarters is located;
* the first entry into any other city, with the entry fee being paid for subsequent entries.

# Task
Given the number of cities, roads, entry fees for each city, and the `M` cities where parcels have to be delivered, help Țirbi calculate the minimum cost required for the deliveries.

# Input data
The input file `posta.in` contains on the first line two natural numbers `N` and `M` separated by a space, with the significance described in the task. On the next `N-1` lines, there are three numbers `x, y, z`, separated by a space, signifying that there is a road from city `x` to city `y` with a cost of `z`. On the next line, there are `N` natural numbers representing the entry fee for each city. The last line contains `M` natural numbers representing the cities where the post has to deliver parcels.

# Output data
The output file `posta.out` contains the minimum cost of a delivery.

# Constraints
* `2 \leq M \leq N \leq 100.000`
* All entry fees and costs are strictly positive natural numbers less than or equal to `100.000`.
* The vehicle can pass through any city or road any number of times.
* The cities where parcels are delivered are distinct.
* For `10%` of the tests `M \leq 3`
* For `30%` of the tests `N \leq 1.000`

# Example

`posta.in`
```
7 3
1 2 3
2 3 5
2 4 2
4 7 4
1 5 7
5 6 1
2 1 1 2 1 2 1
1 4 6
```

`posta.out`
```
28
```

### Explanation

The headquarters will be chosen in city `1` and the following route will be taken: `1→2→4→2→1→5→6→5→1`
The fuel cost is `26`
The entry fees are `2` (city `2` + city `5`)
In cities `4` and `6`, no fee is paid because they are entered only once.