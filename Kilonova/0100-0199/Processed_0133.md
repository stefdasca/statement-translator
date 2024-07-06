```markdown
Tsubasa-chan loves sweets! Recently, a new type of dessert has appeared. Thus, she decided to establish a new factory to produce this delicious product.

The factory contains a huge square container, full of dough, of $10^6 \times 10^6$ units. Each point in the container has coordinates as a pair of real numbers `(x, y)`, where $0 \leq x, y \leq 10^6$, and each point has a sweetness level. The sweetness of a point is initially `0`. For the production of the dessert, `Q` operations are required, which can be of the following types:
* A *vertical sweetening*, determined by an integer coordinate $x_u$ and an integer value `v`. After this operation, all points in the container `(x, y)` where $x_u \leq x < x_u + 1$ become sweeter by `v`.
* A *horizontal sweetening*, determined by an integer coordinate $y_u$ and an integer value `v`. After this operation, all points in the container `(x, y)` where $y_u \leq y < y_u + 1$ become sweeter by `v`.
* A *tasting*, determined by `4` integers coordinates $x_q, y_q, x'_q, y'_q$. For this operation, Tsubasa takes a spoon, dips it into the dough at the point $(x_q, y_q)$, and then moves it in a straight line to the point $(x'_q, y'_q)$. The movement is performed within one second at a constant speed. After that, Tsubasa tastes the dessert, wanting to find out the *total sweetness* of the dough in the spoon. This value is calculated as follows: if the spoon passes through sweetness zones $d_1$ for $t_1$ seconds, $d_2$ for $t_2$ seconds, $\ldots$, and $d_k$ for $t_k$ seconds, then the total sweetness in the spoon is $t_1d_1 + t_2d_2 + \ldots + t_kd_k$. The sweetness in the container is not altered.

# Task
Given all the operations undertaken in the production of the dessert, find the total sweetness values found during all tasting operations.

# Input data
The first line of the input file `dulciuri.in` contains the number `Q` of operations.
The next `Q` lines contain descriptions of all operations, one per line, in order. An operation is encoded as follows:
* A vertical sweetening is encoded as $1 \; x_u \; v$.
* A horizontal sweetening is encoded as $2 \; y_u \; v$.
* A tasting is encoded as $3 \; x_q \; y_q \; x'_q \; y'_q$.

# Output data
The output file `dulciuri.out` should contain all the results of the tastings, in order, one per line. The result of a tasting is considered correct if the absolute or relative error with respect to the commission's solution is at most $10^{-7}$. If the commission's and the contestant's solutions are $s^\ast$, $s$, then the absolute error is $|s^\ast − s|$ and the relative error is $|s^\ast − s|/|s^\ast|$.

# Constraints and clarifications
* All coordinates from the input data are integers in the range $[0, 10^6]$.
* `0 \leq v \leq 1000`.
* `v` is an integer.
* `1 \leq Q \leq 100000`.
* For `20` points: No horizontal sweetenings are made. `Q \leq 2000`.
* For another `20` points: For each tasting, either $x_q = x'_q$ or $y_q = y'_q$. `Q \leq 2000`.
* For another `10` points: At most one tasting is made.
* For another `20` points: All tastings are done after all sweetenings.
* For another `10` points: `Q \leq 2000`.
* For another `20` points: Without additional restrictions.

# Examples

`dulciuri.in` 

```
3
1 2 60
2 3 60
3 0 0 3 4
```

`dulciuri.out`

```
35
```

`dulciuri.in` 

```
4
1 2 10
3 2 0 2 1
3 3 0 3 1
3 2 0 2 0
```

`dulciuri.out`

```
10
0
10
```

`dulciuri.in` 

```
6
1 4 413
1 3 234
2 5 244
2 3 777
3 1 2 14 15
3 31 4 2 40
```

`dulciuri.out`

```
128.3076923077
29.0881226054
```

# Explanation

The situation for the tasting in the first example is explained in the diagram below.

~[dulceata1.png]

The pink areas are the zones where sweetening has been applied, and the numbers represent by how much they were sweetened. The area in the intersection of the sweetenings has a sweetness of `120`. The dotted diagonal line represents the trajectory.
The trajectory has a length of $ \sqrt{3^2+4^2}=5$, and it is completed within one second — thus it has a speed of `5` units per second. The segment from `(2, 2.(6))` to `(2.25, 3)` has a length of $ \sqrt{(2.25 − 2)^2 + (2.(6) − 3)^2} = \sqrt{(1/4)^2 + (1/3)^2} = 5/12$, and has a sweetness of `60` — thus it is traversed in `(5/12) × (1/5) = 1/12` seconds, and contributes with `(1/12) × 60 = 5` to the total sweetness. The segment from `(2.25, 3)` to `(3, 4)` has a length of $ \sqrt{(3 − 2.25)^2 + (4 − 3)^2} = 5/4`, and has a sweetness of `120` — thus it is traversed in `(5/4) × (1/5) = 1/4` seconds, and contributes with `(1/4) × 120 = 30` to the total sweetness. Thus, since the segment from `(0, 0)` to `(2, 2.(6))` contributes with `0`, the total sweetness is `35`.

The situation for the tastings in the second example is explained in the diagram below.

~[dulceata2.png]

In the first trajectory (the one on the left), we always pass through a zone with a sweetness of `10`, so the tasting result is `10`. In the second trajectory (the one on the right), we always pass through a zone with a sweetness of `0`, so the tasting result is `0`. In the third trajectory, we stay put for one second in a sweetness zone of `10`, so the answer is `10`.
```