Certainly! Here is the translated competitive programming problem statement:

---

A traveler wants to travel a distance of $n$ kilometers by taxi, such that the price he pays is minimized. The taxi company this person is using has a fixed unit rate of $C$ lei per kilometer, but also has some special offers of the form $(k, L)$ meaning that for a road portion of $k$ kilometers the traveler can pay $L$ lei (instead of a unit rate for the number of kilometers). Unfortunately, these offers are very odd, and if they are not careful, our traveler can be easily tricked. For example, the taxi company may charge $1370.89$ lei for $2.43$ km and $1509.43$ lei for $3.8$ km.

# Task

As our traveler has difficulties in handling such numbers, he asks you to help him find the optimal way to organize his trip, knowing both the number of kilometers he needs to cover and the rates charged by the taxi company.

# Input data

The first line of the file `taxi.in` contains the number $n$ of kilometers the traveler needs to cover. The second line contains the unit rate $L$ charged by the taxi company. The following lines (at most $100$), until the end of the file, contain pairs of the form $k$, $C$ representing the company's special offers. All numbers in the input file are real numbers, strictly positive, less than $1 \ 000$, and exactly $2$ decimals.

# Output data

The first line of the file `taxi.out` must contain the minimum amount the traveler can pay, written with **three** exact decimals. The next line will contain a sequence of numbers, representing the order in which the special offers are chosen. These numbers can be both natural numbers and negative real numbers. Natural numbers indicate which offer from the input file was chosen at some point, and negative real numbers indicate the number of kilometers traveled (in absolute value), using the unit rate.

# Constraints and clarifications

* $0 < n \leq 100$
* $0 < L \leq 1 \ 000$
* $0 < k \leq 1 \ 000$
* $0 < C \leq 1 \ 000$
* Numbers $n$, $L$, $k$, $C$ are **real** and have a maximum of **two** decimals.

# Example

`taxi.in`
```
52.65
0.80
8.75 5.50
60.35 20.47
20.40 10.20
```

`taxi.out`
```
28.380
-0.69 1 3 3 -2.41
```

---