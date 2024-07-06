Sure, here is the translated text:

---

We all know what a binary search tree is. It is that binary tree in which the information in any node is greater than the information in the nodes of the left subtree of that node and smaller than those in the right subtree.

When searching for information in a binary search tree, we start from the root of the tree and compare with the information from the root. If the searched information is smaller than the information in the root, the search continues in the left subtree, and if it is larger, in the right subtree. If the two pieces of information are equal, the search ends successfully. If in the direction in which we continue the search (left or right) the subtree no longer has nodes, it means that the searched information is not found in the tree. Obviously, the number of comparisons made in a search depends on the distance between the root and the node in which the information is found, or the one where we can decide that the information is not in the tree.

What would happen if, before building the binary search tree, we knew what information was going to be searched in it? Couldn't we build the tree in such a way as to minimize the number of comparisons made?
For example, with the information `1, 2` and `3` we can build a binary search tree in the following `3` ways (out of a total of `5` possible):

 | | 
:-:|:-:|:-:
~[cautare1.jpg] | ~[cautare2.jpg] | ~[cautare3.jpg]

If we search for the information (`1, 1, 3, 1, 2`), then the total search time is for the left tree `1+1+3+1+2 = 8`, for the center tree `2+2+2+2+1 = 9`, and for the right tree `3+3+1+3+2 = 12`.

So the left tree is the most suitable for our searches, and the minimum total search time is `8`.

It should be noted that if a piece of information that does not exist in the tree is searched for, the number of comparisons made during the search is equal to the level of the last queried node. For example, if the information `4` is searched on the three trees, then the times will be: `3, 2,` and `1` (from left to right).

# Task
Write a program that, for certain searched information, determines the minimum total search time.

# Input data
From the file `cautare.in` read the number `T` of tests from the first line. The file continues with the `T` tests. For each test, the following lines are written in the file:
* The first line contains `N`, the number of nodes of the search tree and `M` the number of queries, separated by a space;
* The next line contains `N` distinct integers, separated by a space, representing the information in the nodes of the tree;
* Each of the following `M` lines contains `2` integers separated by a space, representing a searched number and how many times it was searched (between `1` and `100`).

# Output data
In the file `cautare.out`, write for each test a line that contains the minimum total search time for the queries from that test.

# Constraints and clarifications
* `0 < T, N < 101, 0 < M < 1001`
* The information in the tree nodes are integers in the interval `[-10000, 10000]`
* The searched information are integers in the interval `[-1000000, 1000000]` and can be searched a number of times between `1` and `100`.
* For `50` points `T<4`.

# Example

`cautare.in`  
```
3
3 3
1 2 3
1 3
2 1
3 1
3 3
1 2 3
1 50
2 49
3 51
3 2
1 2 3
2 1
4 20
```

`cautare.out`
```
8
251
22
```

Explanations
---

The first test is the one discussed. In the second test, `1` is queried `50` times, `2` `49` times, and `3` `51` times. The best result is obtained in the case of the center tree, namely `251` (`2*50+49+2*51`). The third test contains a query for `4` (which is not in the tree) many times (`20`). Obviously, the best is the right tree, where we quickly realize that `4` is not in the tree. The total time is (`1*20+2`).

---

I have double-checked the statement for grammar and syntax errors in English. Everything should be correct now.