Rick

After the success of the song "Get Schwifty!", Rick started considering the possibility of a career in music. Throughout his inter-dimensional travels, he gathered an impressive collection of $N$ sounds. Each sound is described by its frequency, measured in BPM (beats per minute). Rick invented a device that, given a set of $N$ sounds, randomly selects a subset of this set. These sounds are combined, resulting in a melody. The quality of a melody is given by the greatest common divisor of the frequencies of the combined sounds. Rick is never satisfied with the resulting melody, so he always resets the device to get new melodies.

## Task

Rick is satisfied to find the sum of the qualities of all possible subsets from the set of $N$ sounds.

## Input data

The first line of the file rick.in will contain the natural number $N$, with the meaning described above. The second line will contain $N$ natural numbers, representing the frequencies of the sounds in Rick's collection.

## Output data

In the file rick.out, print on the first line the remainder of the sum of the required qualities divided by $1.000.000.007$.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 500,000

1 $\leq$ sound frequencies $\leq$ 500,000

For 15% of the score:

1 $\leq$ $N$ $\leq$ 20

For another 25% of the score:

1 $\leq$ $N$, the absolute difference between any two frequencies $\leq$ 1,000

For another 35% of the score:

1 $\leq$ $N$, sound frequencies $\leq$ 100,000

By uniform probability, we understand that any subset has the same probability to be extracted by the device.

We consider that the empty subset has the greatest common divisor of 1.

## Example

rick.in

```
3
2 6 4
```

rick.out

```
21
```

## Explanation

We have 8 possible subsets. Calculating the greatest common divisor of the elements of each subset, we obtain the values: 1, 2, 6, 4, 2, 2, 2, 2.