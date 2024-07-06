*It seems that all great ideas which have been etched forever in the heart of Humanity had to first present themselves to the world with monstrous and terrifying masks.* - Friedrich Nietzsche

Given an array with `N` elements, specify how many of its subarrays have a majority element.

# Input data

The file `bvarcolaci.in` contains on the first line the natural number `N`, and on the second line the `N` elements of the array, separated by a space.

# Output data

The file `bvarcolaci.out` will contain on the first line the number of subarrays that have a majority element.

# Constraints and clarifications

* `1 \leq N \leq 250\ 000`
* All values in the array are between `1` and `N`
* A subarray is a subsequence of elements that appear in consecutive positions in the initial array. Subarrays are uniquely defined by the indices of the first and last element in the subarray in the initial array.
* A value is a majority element in an array with `K` elements if it appears at least `[K/2] + 1` times in the array, where `[x]` denotes the integer part of `x`.

# Example

`bvarcolaci.in`
```
6
1 2 1 2 3 2
```

`bvarcolaci.out`
```
10
```

### Explanation

Each subarray of one element has a majority element.

The other subarrays are:
**1 2 1** 2 3 2  
1 **2 1 2** 3 2  
1 2 1 **2 3 2**  
1 **2 1 2 3 2**