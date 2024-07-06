Fie $S$ un șir de caractere de lungime $N$ indexat de la 1. Pe un astfel de șir se definește  operația `swap`: se alege un indice $i$ ($1 \leq i < N$) și se interschimbă caracterele $S[i]$ și $S[i+1]$.

Numărul norocos corespunzător unui șir $S$ este egal cu numărul minim de operații `swap` ce trebuie efectuate succesiv pentru a obține cel puțin o subsecvență `bingo` în șirul $S$. Dacă subsecvența `bingo` apare în șirul inițial, numărul norocos este egal cu $0$.

# Task

Se dă un număr natural $T$ și $T$ șiruri de caractere. Să se determine pentru fiecare șir dat $S_i$ ($1 \leq i \leq T$), numărul său norocos.

# Input data

Fișierul de intrare `bingo.in` conține pe prima linie un număr natural nenul $T$. Următoarele $T$ linii conțin fiecare câte un șir de caractere format doar din litere mici ale alfabetului englez.

# Output data

Fișierul de ieșire `bingo.out` conține numerele norocoase determinate pentru fiecare dintre cele $T$ șiruri date. Acestea se vor afișa fiecare pe câte un rând, în ordinea în care șirurile sunt date în fișierul de intrare.

# Constraints and clarifications

* $1 \leq T \leq 10\ 000$;
* $\sum_{i=1}^{T}|S_i| \leq 100\ 000$, unde se notează cu $|S|$ numărul de caractere din șirul $S$;
* O subsecvență de lungime $L$ a unui șir de caractere $S$ reprezintă o succesiune de $L$ caractere aflate pe poziții consecutive în șirul $S$.
* Se garantează că fiecare șir citit conține cel puțin o dată fiecare caracter din mulțimea $\{b,i,n,g,o\}$;
* Pentru $17$ puncte, $|S_i|=5$ ($1 \leq i \leq T$);
* Pentru $21$ puncte, în fiecare șir $S_i$ ($1 \leq i \leq T$) fiecare caracter din mulțimea $\{b,i,n,g,o\}$ apare exact o dată;
* Pentru $11$ puncte, $1 \leq T \leq 10$ și în fiecare șir $S_i$ ($1 \leq i \leq T$) fiecare caracter din mulțimea $\{b,i,n,g,o\}$ apare de cel mult 10 ori;
* Pentru $51$ puncte, nu există restricții suplimentare.

# Example

`bingo.in`

```
8
nbbigo
ibhpnogg
bihhhhhhhhngo
nbxgyoi
uobsioboisinosaogvnibn
hgibaisianiaosanbviaobi
ybingo
btgpntoipipqiamytoghoi
```

`bingo.out`
```
3
6
16
8
7
14
0
9
```

## Explanation

Numărul norocos al primului șir citit este $3$, iar o succesiune posibilă de operații este: $nbbigo \xrightarrow{} bnbigo \xrightarrow{} bbnigo \xrightarrow{} bbingo$.