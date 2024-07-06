Certainly! Here is the translated text:

---

Eric is a passionate fisherman on the Olt River and the lakes in the Danube floodplain. He has now arrived in the Delta and plans to fish on the channels here. Eric's stay in the Delta begins on day $0$, when he arrives at the fishery in Tulcea. Every day for the next $n$ days, he starts from the fishery he is in, goes to fish on a channel, and then deposits the caught fish in another fishery (from where he will start the next day). He has planned from the beginning, establishing exactly which channel he will fish on each day and in which fishery he will deposit the caught fish at the end of that day. However, he wants to travel the shortest possible distance.

The channels are represented by lines in the plane and the fisheries by points. On the first day of fishing, he leaves from the fishery in Tulcea (let's denote it as fishery $0$), goes to fish in a place on channel $1$, then deposits the fish in fishery $1$. He stays here overnight, then on day $2$, he starts from fishery $1$, fishes in a place (point) on channel $2$ and deposits the fish in fishery $2$, etc.

# Task

Considering that the fisherman Eric can move however he wants, determine the minimum distance he will travel (the sum of the lengths of all the segments he travels).

# Input Data

The file `cherhanale.in` contains on the first line the value $n$, representing the number of days Eric fishes. Each of the next $n$ lines contains $6$ integers, separated by a space: $X_1$, $Y_1$, $X_2$, $Y_2$, $X_C$, $Y_C$. The points ($X_1, Y_1$) and ($X_2, Y_2$) determine the supporting line of the channel, and the point ($X_C, Y_C$) represents the point indicating a fishery.

# Output Data

The file `cherhanale.out` will contain a real number, which represents the required value.

# Constraints and Clarifications

* $1 \leq n \leq 10$;
* $-100 \ 000 \leq X_i, Y_i, X_C, Y_C \leq 100 \ 000$;
* the point corresponding to the fishery in the city of Tulcea is ($0, 0$);
* crossing a channel is considered negligible;
* the channels extend on both sides beyond the segment determined by the given points;
* for the same channel, $X_1 \neq X_2$ or $Y_1 \neq Y_2$;
* the solution will be displayed with exactly 5 decimals, without rounding, i.e., in the form: $\\frac{\\lfloor(sol \cdot 100 \ 000) \\rfloor}{100 \ 000.0}$;
* For any channel, both the fishery immediately before fishing in it and the one immediately after fishing in it are not on that channel.

# Example

`cherhanale.in`
```
1
5 1 1 5 3 0
```

`cherhanale.out`
```
6.70820
```

---

Please double-check the translation for accuracy and clarity.