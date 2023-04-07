# ECE 208 Homework 1: Warm-Up
In this homework assignment, you will be doing some basic warm-up for this course. This assignment includes programming as well as theoretical components to ensure you are comfortable with both sides of the prerequisites of this course. As with all homework assignments in this class, be sure to follow the instructions carefully to ensure that you receive full credit. All coding for this assignment must be done in **Python 3**.

## Problem 1: Least Common Ancestor
An **unrooted tree** is an undirected graph in which any two nodes are connected by exactly one path. Designating one node as the root and orienting all edges away from the root gives a directed graph that represents a **rooted tree**. More generally, any directed graph with no directed cycles is called a **directed acyclic graph (DAG)**. A rooted tree is called **binary** if the degree of all nodes is either one or three, except the root, which has a degree of two; otherwise, it is called **multifurcating**. A node *v* is a **descendant** of a node *u* if and only if (iff) there is a path from *u* to *v*. A node *u* is an **ancestor** of a node *v* iff *v* is a descendant of *u*. Note that, because it is valid to have a single-node path with no edges, every node *u* is considered its own ancestor. A **common ancestor** of two nodes *u* and *v* in a rooted tree or in a DAG is a node that has both *u* and *v* as descendants. A node *x* is called a **least common ancestor (LCA)** of *u* and *v* in a tree or a DAG iff *x* is a common ancestor of *u* and *v* and no other common ancestor of *u* and *v* is a descendant of *x*. Note that two nodes have only one LCA in a tree but can have multiple LCA in a general DAG. Also note that the LCA of a node *u* and itself is itself.

The goal of this problem is to develop a **dynamic programming algorithm** that, given a tree/DAG, produces the LCAs of all pairs of nodes in the tree/DAG.

### Input
The input is a Python [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) `p` representing an input DAG (which may simply be a tree). The keys of the dictionary represent nodes of the DAG (`p` will have *n* keys for a DAG with *n*). For a given node `u`, `p[u]` is a Python [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) containing the parents of `u` (for a tree, this list will have only one element). Note that one (for a tree) or more (for a general DAG) node(s) can have an empty list for `p[u]`; these are the root(s). We suggest that you start by solving the case where the input is a tree and then extend it to a general DAG.

### Output
The output is a Python [nested dictionary](https://www.geeksforgeeks.org/python-nested-dictionary/) (i.e., a dictionary of dictionaries) called `LCA` such that the keys of `LCA` are the keys of `p`, the keys of `LCA[u]` are also the keys of `p`, and the value of `LCA[u][v]` should be a Python [set](https://docs.python.org/3/tutorial/datastructures.html#sets) containing all LCAs of `u` and `v`.

## Starter code
* **[LCA.py](LCA.py):** Given to you, please **DO NOT** modify. This file provides the in/out skeleton of the program.
    * Usage: `python3 LCA.py <parent_dictionary>`
* **[lca/todo.py](lca/todo.py):** The starter code. You will need to **address all the TODO** in the `find_LCAs` function.
* **[autocheck.py](autocheck.py):** Given to you, please **DO NOT** modify. This file runs the tests for your program.

### Autocheck and the manual tests
We provide some tests to help you debug your program. To automatically run the tests, use `autocheck.py` as follow:

`python3 autocheck.py`

There are 7 tests in total. The first two tests are sanity checks of the package distributed to you, so your program will always pass these first two tests. If it does not, please contact your TA to troubleshoot the problem.

The tests on autocheck.py will also be run by "Github Actions" everytime you push your code to the Github repository, so be sure to check the "Actions" tab of your repository to see if the tests passed.

Passing these tests **DOES NOT** guarantee you a full grade. You are encouraged to carefully think about the problem, identify the edge-cases of your program, and add more tests by your own. We will grade your work on **entirely different tests** that are NOT given to you at this stage.

The test cases are all given in [testing/test_data/checking](testing/test_data/checking/). All the files `.in` are sampled inputs and `.out` are associated sampled output. You can manually run the test by calling `LCA.py`, for example:

```python3 LCA.py testing/test_data/checking/binary_small.in myOutput.out```

Then you can compare `myOutput.out` to the file `testing/test_data/checking/binary_small.out`.

### Example Input
```python
{
    'A': [],
    'B': [],
    'C': ['A', 'B'],
    'D': ['A', 'B']
}
```

The above dictionary corresponds to the following graph:

![Alt text](https://g.gravizo.com/svg?digraph%20G%20{A->C;A->D;B->C;B->D;})

### Example Output
```python
{
    'A': {
        'A': {'A'},
        'B': set(),
        'C': {'A'},
        'D': {'A'}
    },

    'B': {
        'A': set(),
        'B': {'B'},
        'C': {'B'},
        'D': {'B'}
    },

    'C': {
        'A': {'A'},
        'B': {'B'},
        'C': {'C'},
        'D': {'A', 'B'}
    },

    'D': {
        'A': {'A'},
        'B': {'B'},
        'C': {'A', 'B'},
        'D': {'D'}
    }
}
```

**Note:** The actual output will be on a single line and will thus be much harder to read. You may want to use a [beautifier](https://codebeautify.org/python-formatter-beautifier) to make it more human-readable.

## Homework Deliverables
* **[student_info.txt](student_info.txt):** Fill in your information in the given text file. If you do not supply this information, your submission is invalid.
* **writeup_<YOUR_PID>.pdf:** A write-up that includes the following pieces of information:
    1. The recursive formula of the dynamic programming
    2. The base case of the dynamic programming
    3. The asymptotic running time of the algorithm
    * Note that, for each of the above three items, you must derive or explain your answer

* **[lca/todo.py](lca/todo.py):** Your Python 3 code for solving the problem
    * We have provided starter code in the file, but you must fill out the `lca` function (labeled with `TODO`)

## Grade Breakdown (100 Points)
* **Writeup: 40 Points**
    * *Correct recursive formula:* 20 points
    * *Correct base case:* 10 points
    * *Correct asymptotic running time:* 10 points

* **Programming: 60 Points**
    * 24 tests in total, each worths 2.5 pts. Time limit per test: 60 seconds
    * *Binary Tree (small):* 4 tests, total 10 points
    * *Binary Tree (large):* 4 tests, total 10 points
    * *Multifurcating Tree (small):* 4 tests, total 10 points
    * *Multifurcating Tree (large):* 4 tests, total 10 points
    * *DAG (small):* 4 tests, total 10 points
    * *DAG (large):* 4 tests, total 10 points
