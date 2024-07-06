> "A nation that destroys its soils destroys itself." - Franklin D. Roosevelt

This is the main problem of the hackathon and it is worth the most points.  
**ATTENTION:** The problem will be referred to as **META-TASK** throughout the rest of the contest.  
**ATTENTION:** This problem is worth $700$ points. In "submissions" the maximum score is rescaled to $100$ points, but the true score will be visible on the *[leaderboard](https://kilonova.ro/contests/179/leaderboard)*.

# About Soil Pollution

The origin of soil pollution can be natural or anthropogenic and, therefore, may have occurred long ago or recently. Certain contaminants are often associated with specific activities, such as the use of pesticides in agriculture or radionuclides from nuclear power plants, while many other contaminants may result from various pollution sources. (source: UN)

# Agricultural Soil

The main sources of soil pollution in agricultural areas can be grouped according to direct sources (pollution from the point of origin), such as the application of pesticides and mineral fertilizers, and indirect sources (diffuse pollution), such as floods and atmospheric deposition. Polluted soils also represent a secondary source of contaminant emissions to the surrounding air, surface waters, groundwater, and subsequently, to oceans.

The main sources of soil pollution in agricultural areas can be grouped as follows: i) pesticides; ii) mineral fertilizers; iii) organic fertilizers (manure and sewage sludge); iv) wastewater for irrigation; v) plastics such as mulch films and greenhouses, drip irrigation tubes, and empty packaging; vi) and rural waste. Different contaminants are associated with each source. (source: UN)

~[AdobeStock_450099198-768x432.jpeg.webp|align=center]

$$
\text{fig 1. Severe case of soil contamination, Alan Boswell Group}
$$

# Task

The notorious megacorporation Chert And, known for its activities in the agriculture sector, is accused of serious soil contamination at one of its farms in Romania. Specifically, a number of mini pesticide depots have broken at certain locations, contaminating the entire adjacent arable land.

Chert And officials have refused to provide statements about this incident, and also about the exact locations of contamination on the thousands of hectares of land. Therefore, as dedicated environmental activists and programmers, your goal is to use all the digital tools at your disposal to create a most accurate report on the produced pollution.

# Formal

The agricultural land can be thought of as an $N \times N$ matrix of cells. Each cell can be in one of the following states:

- **source of contamination cell**, meaning where a pesticide depot has broken
- **arable cell**, meaning where various products of the corporation were planted
- another type of cell, irrelevant for the problem.

A cell is called **contaminated** if it **is arable** *and* is adjacent to **at least one** of the following:

- adjacent to a **source of contamination** ("adjacent" means having a common side)
- adjacent to another contaminated cell ("adjacent" means having a common side)

Your goal is to report the positions of as many arable cells as possible, and for each whether it is **contaminated** or **not**.

**ATTENTION: Notice that cells that are the source of contamination (where pesticide depots have broken) are not arable cells and should not be reported.**

# Output

This problem is **output only**, meaning you only need to submit the data found to the committee through the platform, in a .txt file (or print copy-paste).

The first line in the text file you submit must contain a number $K$, the number of **arable** cells you report.

On the next $K$ lines, display triples in the form: $i, j, status$, where $i$ represents the row, $j$ the column of the arable cell, and $status$ represents whether it is contaminated ($status = 1$) or not ($status = 0$).

# Obtaining Data

Each of the other tasks of the competition, besides the fact that they will also reward you with points (a smaller number than for this problem), will reveal information about the map.

More specifically, if a subtask in another problem is solved correctly, the verdict will include a *Google Drive* link to more data.

A *batch* of data consists of multiple triples in the form: $i, j, status$, where $i$ represents the row, $j$ the column of the cell, and $status$ represents whether it is an arable cell ($status = 0$) or a source of contamination ($status = 1$). **Notice the different meaning of $status$ in this section. An arable cell from a *batch* can be or not be contaminated, and $status$ will still be $0$.**

Example of a Google Drive file with data:
```
1 2 0
56 89 1
3 4 0
123 456 0
12 345 1
```

# Scoring

The scoring is done partially, as you report more arable cells.

Specifically, it is ensured that there are **$7000$** arable cells.

For each such distinct arable cell reported in your input, you will receive:

- $0.1$ points if the reported status matches the real one
- $0.05$ points if the reported status does not match the real one

If the report is perfect, you will obtain a total of $700$ points for this problem.

**ATTENTION!** If you report a cell, but it is not an arable cell, then the score for that submission will be **null**. If you include a cell twice but with a different $status$, then the score for that submission will be null. If you repeat a triplet of values, it will only be considered once in the evaluation.

# Constraints and clarifications

- $N = 500$

# Example

~[example.jpg|width=15cm|align=center]
$$
\text{fig 2. Example of a farm}
$$

In this example, a possible mini-farm is illustrated, where red cells represent sources of contamination, orange cells represent contaminated arable cells, and green cells represent uncontaminated arable cells. **Only orange and green cells should be reported. Competitors must determine whether arable cells are contaminated or not.**

A complete submission for the illustrated example would look as follows:

```
25
2 6 1
2 7 1
3 7 1
4 2 1
5 2 1
5 3 1
6 1 1
6 3 1
7 2 1
9 9 1
9 10 1
10 9 1
4 9 0
5 7 0
5 8 0
5 9 0
6 7 0
6 8 0
6 9 0
7 5 0
7 8 0
11 11 0
```
