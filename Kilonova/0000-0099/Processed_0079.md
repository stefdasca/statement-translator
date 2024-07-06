Given is a sequence `a` with `N` elements, numbered from `1` to `N`. We will perform `M` operations on the sequence:
* `+` `x` `y` `z` - Add `z` to the elements in the interval `[x y]`
* `=` `x` `y` `z` - The elements in the interval `[x y]` become equal to `z`
* `R` `x` `y` - The elements in the interval `[x y]` are reversed (`a[x]` becomes `a[y]`, `a[x+1]` becomes `a[y-1]`, ... , `a[y]` becomes `a[x]`)
* `D` `x` - The element at position `x` is deleted, `a[1...n]` becomes `a[1...x-1] ∪ a[x+1...n]`
* `I` `x` `z`- The element `z` is added at position `x`, `a[1...n]` becomes `a[1...x-1] ∪ z ∪ a[x...n]`
* `Q` `x` `y` - The sum of the elements in the interval `[x y]` is requested

Respond to all queries of type `Q` and at the end of the queries, print the sequence `a`.

# Input data
The first line contains `N` and `M`. The second line contains `N` numbers, the elements of `a`. The next `M` lines contain the queries, according to the format described above.

# Output data
Each line will contain the response for `Q` queries. The last line will print the final sequence `a`, separated by spaces.

# Constraints and clarifications
* `1 \leq N \leq 100 000`
* `1 \leq M \leq 200 000`
* Only non-null numbers $ \leq 10^9$ will be read and the result of a query will be $ \leq 10^{18}$.
* It is guaranteed that operations will be performed on elements of `a` which exist at that moment.
* It is guaranteed that `a` will not have more than `N` elements at any moment.

# Example

`stdin`
```
5 11
1 2 3 4 5
Q 2 4
+ 1 3 1
Q 2 4
= 4 5 1
Q 2 4
R 1 3
Q 2 4
D 2
Q 2 4
I 3 5
Q 2 4
```

`stdout`
```
9
11
8
6
4
8
4 2 5 1 1
```