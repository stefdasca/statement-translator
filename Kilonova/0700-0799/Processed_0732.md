Lidorienii și senopictii sunt în conflict pentru ronul fermecat, fiind arbitrați de orintieni, aleși de părțile beligerante drept judecători. Orintia a propus: „Ronul fermecat va fi ascuns printre alți $k$ roni cu același aspect, dar toți realizați dintr-un material mai greu decât originalul, având masa, standard, diferită de cea a ronului femecat. Pentru a-l descoperi, vă gandiți că aveți la dispoziție o balanță și toți cei $k+1$ roni. Lidorienii, apoi senopictii vor spune un singur număr, reprezentând numărul maxim de cântăriri admis pentru descoperirea ronului fermecat. Dacă nici una dintre părți nu spune numărul corect, atunci ronul fermecat va rămâne în Orintia. Dacă ambele părți spun numărul corect, ronul va rămâne tot la orintieni.”.

# Task

Your task is to indicate the country that will win the magic ron: Lidoria - $L$, Senopictia – $S$, Orintia – $O$.

# Input data

The file `ron.in` contains in the first line the number $k$, and in the second line two numbers $RL$, respectively $RS$ separated by a space. $RL$ represents the answer of the Lidorenians, and $RS$ the answer of the Senopictians.

# Output data

The file `ron.out` contains one of the letters $L, S$ and $O$.

# Constraints and clarifications

* $1 < k < 10\ 000$;
* $RL, RS$ are natural numbers at most equal to $k$;
* The magic ron is a cuboid engraved with fixed signs of power;
* The maximum allowed number of weighings is not obtained by weighing a ron multiple times or by weighing the rons as many times as possible; weighing means having an equal number of rons on each arm of the balance ($1 - 1$, $2 - 2$, etc.)

# Example 1

`ron.in`
```
7
1 3
```

`ron.out`
```
O
```

## Explanation

The maximum allowed is $2$, so the magic ron remains in Orintia.

# Example 2

`ron.in`
```
4
2 2
```

`ron.out`
```
O
```

## Explanation

The maximum allowed is $2$, but since it is a tie, the ron remains in Orintia.