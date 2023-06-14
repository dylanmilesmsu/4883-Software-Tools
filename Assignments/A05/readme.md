## A05
### Dylan Miles
### Description:
Programmatically generate a graphviz dot file from a family tree 

### Files

|   #   | File            | Description                                        |
| :---: | --------------- | -------------------------------------------------- |
|   1   | Main.java         | Main driver of my project, contains all logic      |
|   2   | Person.java  | Person data structure         |
|   3   | clan_names.txt | List of clan names to be mixed into family tree data |
|   4   | tree.csv | family tree data, generated from http://mcdemarco.net/tools/family-tree-generator/lineage.html |
|   5   | output.dot | Output of java program |
|   6   | graphviz.png | Output png from graphviz online, obtained by pasting output.dot into it|
|   7   | graphvizGen.jar | Binary of the program|

### Instructions

Java JRE 11 or newer is required
A binary is provided
Make sure a clan_names.txt file and a tree.csv file are both included in the same directory as the jar

- Example Command:
    - `java -jar graphvizgen.jar`
