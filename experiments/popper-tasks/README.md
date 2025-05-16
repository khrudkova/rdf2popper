# rdf2popper evaluation experiments
## 1. numeric-zendo1
- dataset [source](https://github.com/celinehocquette/numsynth-aaai23/tree/main/numsynth/examples/numeric-zendo1)
- dataset contains 60 examples, 30 positive and 30 negative

Zendo is a game of inductive logic, where one player invents a rule that the rest of the players try to figure out by creating configurations of the game pieces. The winning condition is to correctly induce the rule. The pieces are of several colors, and shapes and can be in various positions, have various sizes, can be in contact or not, and so on. 

An example of Prolog atoms in dataset:
```
piece(0, p0_0).
position(p0_0, 9.05, 5.6).
size(p0_0, 3.14).
color(p0_0, red).
orientation(p0_0, lhs).
rotation(p0_0, 0.89).
```
To receive a Prolog atoms, find a KG in N-Triples serialization format (or N-Triples like format) and run `rdf2popper`. For the described experiment, the dataset was created by transforming original dataset from the source by [`popper2rdf`](https://github.com/khrudkova/popper2rdf/edit/main/) to KG and then back to Prolog atoms. These datasets are provided within this repository.
## 1.2. Install Popper/numsynth-aaai23
Instructions [here](https://github.com/logic-and-learning-lab/Popper) and [here](https://github.com/celinehocquette/numsynth-aaai23/tree/main).
## 1.3. Obtaining a solution
Once you have succesfully installed Popper, download the `rdf2popper_numeric-zendo1` folder. It should contain three files:
```
bias.pl
bk.pl
exs.pl
```
These are some changes in the `bias.pl` from the source dataset, as any _n_-ary relation (where _n > 2_) is transformed into set of binary relations. The changes are as follows:
| **Original bias lines** | **Changed bias lines** |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| body_pred(position,3).            | body_pred(position_p1,2).<br>body_pred(position_p2,2).<br>body_pred(position_p3,2).                                 |
| type(position,(piece,real,real)). | type(position_p1,(piece,piece)).<br>type(position_p2,(piece,real)).<br>type(position_p3,(piece,real)).             |
| direction(position,(in,out,out)). | direction(position_p1,(in,out)).<br>direction(position_p2,(in,out)).<br>direction(position_p3,(in,out)).             |

After downloading this folder (or obtaining it by first using `popper2rdf` and then `rdf2popper`), just run numsynth-aaai23 (as there are numerical values in this dataset) and let it produce solution.

The solution on **rdf2popper_numeric-zendo1** dataset:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:30 FN:0 TN:30 FP:0 Size:5
zendo(A):- piece(A,B),contact(B,D),size(D,E),geq(E,4.12).
******************************
```
## 1.4. Qualitative evaluation of solution similarity
The evaluation of solution similarity follows four principles:
1. Subset of rules in the RDFRules output is identical or nearly identical with Popper solution.
2. When evaluating similarity, small differences in interval boundaries are tolerated as long as the solutions are identical or nearly identical.
3. A small differences in rule coverage are investigated, and if these are results of different interval boundaries or by nature of AMIE, these are tolerated.
4. A Popper solutions match exactly, with the exception of slight differences of numerical values, which are expected and tolerated, as [Clingo answer set solver](https://potassco.org/clingo/) used in numsynth-aaai23 is non deterministic. The different labeling of variables in solutions is not a factor.

The Popper solution, which is the information we want to match on transformed dataset have been produced by [numsynth-aaai23 branch of Popper](https://github.com/celinehocquette/numsynth-aaai23/tree/main). The solution was produced on unchanged dataset and is as follows:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:30 FN:0 TN:30 FP:0 Size:5
zendo(A):- piece(A,B),contact(B,C),size(C,D),geq(D,4.12).
******************************
```
On **numeric-zendo1** dataset, we were able to get the exact same solution on the converted dataset as we got with the original data with the exact same coverage of positive examples, which is in line with Principle 3 and 4, and the solutions are therefore _similar_.
