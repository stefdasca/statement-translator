Echipa SG1 se află în fața unei noi provocări. Un dispozitiv antic are un sistem foarte ciudat prin care poate fi pus în funcțiune. Dispozitivul are $n$ butoane numerotate de la stânga la dreapta de la $1$ la $n$. Pe fiecare buton se găsește un număr natural. Suma tuturor numerelor de pe butoane este divizibilă cu $n$.

S-a constatat că la atingerea butoanelor din capete (butonul $1$ și butonul $n$) numărul scris pe acestea scade cu o unitate, iar numărul de pe butonul vecin crește cu o unitate. Dacă se atinge unul dintre celelalte butoane (cele numerotate cu $2, 3, \dots, n-1$) numărul corespunzător scade cu două unități, iar cele corespunzătoare vecinilor cresc cu câte o unitate. Dispozitivul va fi pus în funcțiune dacă toate cele $n$ numere devin egale.

Ajutați echipa SG1 să pună dispozitivul în funcțiune folosind un număr minim de atingeri ale butoanelor.

# Task

Fișierul de intrare `butoane.in` conține pe prima linie numărul natural $n$, reprezentând numărul de butoane. Pe cea de-a doua linie conține $n$ numere naturale, separate prin câte un spațiu, reprezentând în ordine valorile înscrise inițial pe cele $n$ butoane.

# Output data

Fișierul de ieșire `butoane.out` will contain $n$ lines. Each line $i$ ($1 \leq i \leq n$) will contain a natural number representing the number of touches of button $i$.

# Constraints and clarifications

* $3 \leq n \leq 1 \ 000$
* The initial numbers on the $n$ buttons are natural numbers less than or equal to $100$. The sum of the $n$ numbers is divisible by $n$.
* The number of touches of any button will be $\leq 2 \ 000 \ 000 \ 000$ (two billion).
* Scoring. If the program displays a solution that opens the device with a minimum number of touches, it gets the full score for that test. If the number of touches is not minimal, but the displayed solution opens the device, $30\%$ of the score is obtained.

# Example

`butoane.in`
```
3
10 11 12
```

`butoane.out`
```
0
1
2
