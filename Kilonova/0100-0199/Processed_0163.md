Mirșid Village is made up of `N` houses numbered with natural numbers from `1` to `N`. In house number `1`, there is a generator that supplies electricity to all the houses in the village as follows: house number `1` supplies a number of houses with electricity, each of these houses in turn supplying other houses, and so on. Each house is powered by exactly one power source (which can be another house powered by electricity or the generator in the case of house number `1`). Each house has a single electric fuse. In the event of a malfunction of an electrical appliance in a house, the house's fuse burns out. In this case, the electricity supply to the house is interrupted, causing the interruption of electricity in all houses powered from it, directly or indirectly.

The fuse manufacturing company has a journal in which each day a fuse was burned or replaced was recorded, along with the number of the house where the event took place. The journal contains a total of `M` events. To determine the level of customer satisfaction, the company wants to find out the total number of houses that had electricity on certain days of interest.

# Task
Write a program to determine the number of houses that had electricity for each of the days of interest specified by the company's management.

# Input data
The input file `curent.in` contains on the first line the natural number `N`. The second line contains `N-1` non-zero natural numbers at most equal to `N`, separated by a single space, where the `k`-th number (`1 \leq k < N`) represents the number of the house from which the house numbered `k+1` receives electricity. The third line contains a natural number `M` representing the number of events recorded in the company's journal. Each of the next `M` lines contains `3` natural numbers `a b c`, separated by a single space, which describe an event as follows: if `c` is `0` then on day `a` the fuse in house `b` burned out, if `c` is `1` then on day `a` the fuse in house `b` was replaced. Line `M+4` of the file contains a natural number `T` representing the number of days for which the number of houses with electricity needs to be determined, and line `M+5` of the file contains a strictly increasing series of `T` natural numbers, separated by a single space, representing the days of interest specified by the company's management. The days are numbered from `1` to $10^{9}$.

# Output data
The output file `curent.out` will contain `T` lines, each line` k` (`1 \leq k \leq T`) will contain a natural number representing the number of houses that had electricity on the `k`-th day of interest (in the order from the input file).

# Constraints and clarifications
* `0 < N < 100011; 0 < M < 100022; 0 < T < 100033`
* if  `a b c`  and  `a' b' c'` are the values describing, in the input file, two events, and `a = a'`  then `b \neq b'`.

# Example

`curent.in`
```
11
1 2 3 3 3 5 5 2 1 10
6
9 9 0
2 3 0
10 10 0
22 3 1
14 5 0
31 1 0
4
8 13 23 33    
```

`curent.out`
```
5
2
5
0
```

Explanations
---

On day `2`, the fuse in house `3` burned out, and houses `3, 4, 5, 6, 7, 8` were no longer supplied with electricity. The fuse was not replaced until day `8`, leaving only `5` houses supplied (`1, 2, 9, 10, 11`), the value `5` being written on the first line of the `curent.out` file. On days `9` and `10` the fuses in houses `9` and `10` burned out. Thus, on day `13` only `2` houses (`1` and `2`) are supplied with electricity, the value `2` being written on the second line of the file. On day `14` the fuse in house `5` burned out, which did not change the number of houses supplied with electricity. On day `22` the fuse in house `3` was repaired, and on day `23` there were `5` houses supplied with electricity (`1, 2, 3, 4, 6`), the value `5` being written on the third line of the file. On day `31` the fuse in house `1` burned out, so on day `33` no house is supplied with electricity, the value `0` being written on the fourth line of the file.