Sure, here is the translated document:

---

Shaka, the king of the Zulus, ordered the creation of a communication system based on drums (tam-tam) that would cover the entire country. For this, he instructed those who would transmit the messages. The problem that arose was that some of the trainees could not distinguish between the sounds and could not faithfully reproduce the sequence of sounds on paper. The following notation convention was established: a long sound will be represented by `+`, a short one by `-`, and an undecided one (the receiver is not sure of the length of the sound) by `*`.

At the end of the training, Shaka went to check the trainees' level of preparation. For this, he gathered $n$ trainees and asked them to receive and note down a message composed of $m$ sounds. After transmitting the message, it was found that many of the trainees had written very different sequences, which led to a significant alteration of the original message, even though the least prepared trainee was undecided on no more than half of the sounds. Upset, Shaka called the chief instructor and, to punish him, asked him to determine how many distinct messages could be formed from the sequences written by the trainees.

# Task

Write a program that determines the number of distinct resulting messages.

# Input data

The file `aritma.in` contains on its first line the numbers $n$ and $m$ separated by a space, and on the next $n$ lines strings of length $m$ composed only of the symbols `+`, `-`, or `*`.

# Output data

The first line of the file `aritma.out` will contain the number of distinct messages.

# Constraints and clarifications

* $1 < n < 25$
* $1 < m < 19$

# Example

`aritma.in`
```
3 3
+-*
+*+
-*+
```

`aritma.out`
```
5
```

## Explanation

The resulting messages are: `+--, +-+, +++, +-+, --+, -++`. The first two messages result from the first identification, the next two are from the second identification, and the last two are from the last string, but only five are distinct.

---

Please let me know if you need any further adjustments.