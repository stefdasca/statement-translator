
# Task

Ualpa is a being passionate about nicknames, so she started collecting them. For Christmas, a friend gave her a list of nicknames, but not all are to her liking, so she will eliminate some of them.
Ualpa will remove all nicknames that have a different number of characters than her name. She will also remove all nicknames that differ from her name by more than one character (she will remove the string `alata` but not the string `alatu`). The order of the letters in the word is irrelevant.
Being very busy during this period, she asks for your help to find out how many nicknames need to be eliminated.

# Input data

The first line contains the number $N$ representing the number of nicknames found by her friend, followed by $N$ lines each containing one of the $N$ nicknames.

# Output data

$K$, the number of nicknames Ualpa will have after elimination.

# Constraints and clarifications

* It does not matter if the letters in the strings are uppercase or lowercase (Ualpa will overlook them)
* $1 \leq N \leq 10$;
* $1 \leq length_{string} \leq 100$;
* Her name is of course, ualpa

# Example

`stdin`
```
4
ualpa
pauala
laupu
lllup
```

`stdout`
```
2
```

## Explanation

The nicknames that will be deleted by `Ualpa` are `pauala` (different number of letters) and `lllup` (differs by more than one letter).
