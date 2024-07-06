# Task
It's time for Anarchy in the Sad City! In a revolt against subcultural manifestations, you want to bring the city to a standstill. Following an illegal raid at the City Hall, you "borrowed" a map and realized that there are `M` one-way streets among the `N` intersections of Sad City. Each intersection has two lampposts. The first one lights half of each street that leaves the intersection, and the second one lights half of each street that enters the intersection. For example, the first half of the street between intersections `A` and `B` is lit by the first lamppost in intersection `A`, and the second half is lit by the second lamppost in intersection `B`. A turned-off lamppost does not light anything. A street is **safe** only when it is lit **entirely**.

# Task
Firstly, you must ensure that no street will be completely lit, so that the safety of the citizens is minimized. But this goal does not fully satisfy you, so in addition, you want a maximum number of lit lampposts to give a heavy blow to the budget of the City Hall of Sad City. Once these conditions are fulfilled, the Revolution can begin.

# Input data
The input file `felinare.in` contains on the first line two strictly positive natural numbers `N` and `M`, representing the number of intersections and the number of streets in the Sad City. Each of the following lines contains a pair of natural numbers `A` and `B` between `1` and `N` representing a street that leaves intersection `A` and arrives at intersection `B`.

# Output data
The output file `felinare.out` will contain on the first line a single natural number representing the maximum number of lampposts that can be lit. On the next `N` lines, there will be numbers between `0` and `3`, with the following meanings:
* `0` : both lampposts at the intersection are turned off;
* `1` : only the first lamppost at the intersection is lit;
* `2` : only the second lamppost at the intersection is lit;
* `3` : both lampposts at the intersection are lit.

# Constraints and clarifications
* `1 \ \leq N \ \leq 8191`
* `1 \ \leq M \ \leq 20000`
* There are no streets that connect an intersection to itself.
* Determining the maximum number of lampposts accounts for `40%` of the score. 

# Example

`felinare.in`
```
4 4
1 2
4 1
4 2
4 3
```

`felinare.out`
```
6
2
3
3
2
```
