Emilian is an illustrious neurosurgeon who has just opened a clinic in the city of Saint Genesius. Since he is known throughout the city as the best neurosurgeon in the country, there is always a multitude of requests from patients who want to be scheduled for a consultation. Because he is normally very busy, he lets the clinic's secretarial staff handle the appointments. Unfortunately, all the secretarial staff is on vacation during the busiest time of the year, and thus, Emilian asks for your help to schedule his patients.

In one day, he receives requests from $N$ patients, and to make it easier for him to create his schedule, Emilian has allowed each patient to propose only two moments in time when they can be called for a consultation.

# Task

Knowing that Emilian's staff is on vacation for $T$ days, and every day Emilian has other patients he needs to schedule, help him decide for each day whether he can or cannot schedule all patients on that day.

# Input data

The first line contains a natural number $T$, representing the number of days. Then for each of the $T$ days, the first line contains two natural numbers separated by a space: $N$, representing the number of patients on that day, and $M$, which represents how many moments of time exist on that day. On the next $N$ lines, there are two numbers separated by a space, representing the preferences of each patient.

# Output data

Print $T$ lines representing the answers for the $T$ days. For a feasible schedule (where each patient is scheduled at one of their preferred moments), print "DA". For an unfeasible schedule, print "NU".

# Constraints and clarifications

* $1 \leq T \leq 10$;
* $1 \leq N \leq 100\ 000$;
* $1 \leq M \leq 2*N$;
* Subtask $1$ ($20$p): $1 \leq N \leq 10$;
* Subtask $2$ ($30$p): $1 \leq N \leq 1\ 000$;
* Subtask $3$ ($50$p): No other constraints.

# Example

`stdin`
```
2
3 4
1 3
2 4
3 4
4 3
1 2
2 3
3 1
2 3
```

`stdout`
```
DA
NU
```

# Explanation

We have $T=2$ days for which we want to determine if a schedule exists or not. On the first day, we can call patient $1$ at time $3$, patient $2$ at time $2$, and patient $3$ at time $4$. Therefore, the answer will be "DA". For the second day, we cannot choose a different time for each patient, so the answer is $NU$.