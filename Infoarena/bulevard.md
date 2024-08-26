Boulevard

On a large boulevard in the locality of CCEX, numerous traffic incidents occur. Due to their experience, the local police can specify the times when incidents frequently happen. Thus, the police have $N$ natural numbers representing the times when there is a high risk of danger. The local police have hired two new officers and want to send them into the field to monitor traffic. Each of the two officers has a working time of $T$ units. Determine when each of the two officers should start their shift so that their working schedule includes the maximum number of given incidents.

## Input data

The input file `bulevard.in` contains on the first line a natural number $N$ which represents the number of times when an incident can occur. The next line contains exactly $N$ natural numbers, in ascending order, separated by spaces, representing the times when the incidents occur. The third and last line of the file contains the natural number $T$, the working time for each officer.

## Output data

The output file `bulevard.out` will contain a single line which will have the maximum number of incidents that can be covered in the officers' working schedule. The second line contains two natural numbers, representing the times when the two officers start their shifts. If there are multiple solutions, the one where the first number is as small as possible will be displayed. If there are still multiple solutions, the one where the sum of the two numbers is the smallest will be displayed.

## Constraints and clarifications

$1 \leq N \leq 100\,000$  
$1 \leq T \leq 1\,000\,000$  
The incident times are less than $100\,000\,001$  
There may be two incidents occurring at the same time  
Officers cannot start their shifts before time $0$

## Example

`bulevard.in`  
8  
1 3 8 12 19 22 25 36  
7

`bulevard.out`  
6  
1 18

## Explanation

The first officer works during the period $[1, 8]$, and the second officer works during the period $[18, 25]$. Thus, the events at times $1$, $3$, $8$, $19$, $22$, and $25$ are monitored.