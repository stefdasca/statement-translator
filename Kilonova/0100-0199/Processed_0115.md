You are the coach of the cyclist Adirem Onamihs. A sporting event will soon take place, and for its organization, `N` intersections and `M` **bidirectional** roads between these intersections have been set up. For each road, the number of minutes required to travel it is known. At each intersection, the cyclist passing through is required to drink an energy and refreshing drink. The drink varies from intersection to intersection and the number of calories of each drink is already known.

As the great coach, you are to prepare a special plan to train Adirem. You want the route that Adirem chooses to take **exactly** `T` minutes, but you don't want to plan the entire route for him (Adirem needs to train his mind, not just his body). You will specify to Adirem the intersection where he starts his route and the intersection where he finishes it. Adirem learns quickly - he always knows how to choose the optimal route (the shortest path between the two intersections). To make him travel exactly `T` minutes, you will prohibit passing through certain intersections under the pretext that the caloric value of the drink served at that intersection is not beneficial for his training. Thus, you will specify a lower limit and an upper limit for the number of calories of the drinks he is allowed to consume. Adirem will only pass through intersections where a drink with a caloric value within the given limits is served.

# Task
Write a program that calculates the four variables in Adirem's training: start intersection, finish intersection, minimum caloric value he can consume, and maximum caloric value, so that the shortest path between the two intersections (that respects the restrictions) takes exactly `T` minutes.

# Input data
The first line of the file `coach.in` contains three integers `N, M`, and `T` - the number of intersections, the number of roads, and the desired time, respectively. The next `N` lines contain one number each - the caloric values (integers between `1` and `10000` inclusive) of the drinks in the intersections, in order (from `1` to `N`). The next `M` lines contain one triplet of numbers: two intersections (distinct numbers between `1` and `N`) and the duration of the road between them (integer between `1` and `10000` inclusive).

# Output data
The file `coach.out` will contain one line with the four values found: start node, finish node, minimum caloric value, and maximum caloric value. The nodes will be integers between `1` and `N`, and the caloric values will be integers between `1` and `10000` (inclusive).

# Constraints and clarifications
* `1 \leq N \leq 100`
* `1 \leq M \leq 4950`
* `1 \leq T \leq 1000000`
* The found intersections (start and finish) must also respect the caloric restrictions.
* A drink with a caloric value $x$ can be drunk if and only if $cmin \leq x \leq cmax$, where `cmin` and `cmax` are the minimum and maximum caloric values set by the coach.
* There is a maximum of one road between two intersections.
* Caloric values are distinct.
* There is always a solution; if there are multiple solutions, any of them can be returned.

# Example

`coach.in`
```
6 9 11
40
10
20
30
60
50
1 2 2
1 3 2
1 4 4
1 6 10
2 3 3
2 4 1
4 5 1
4 6 5
5 6 2
```

`coach.out`
```
3 6 20 55
```
