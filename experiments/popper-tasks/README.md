# rdf2popper evaluation experiments
- [Popper](https://github.com/logic-and-learning-lab/Popper/tree/main) v4.3.0
- [numsynth-aaai23](https://github.com/celinehocquette/numsynth-aaai23/tree/main)
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
## 1.2 Install Popper/numsynth-aaai23
Instructions [here](https://github.com/logic-and-learning-lab/Popper) and [here](https://github.com/celinehocquette/numsynth-aaai23/tree/main).
## 1.3 Obtaining a solution
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
## 1.3.1 Popper original solution

The Popper solution, which is the information we want to match on transformed dataset was produced by [numsynth-aaai23 branch of Popper](https://github.com/celinehocquette/numsynth-aaai23/tree/main). The solution was produced on unchanged dataset and is as follows:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:30 FN:0 TN:30 FP:0 Size:5
zendo(A):- piece(A,B),contact(B,C),size(C,D),geq(D,4.12).
******************************
```
## 3. numeric-zendo2
- dataset [source](https://github.com/celinehocquette/numsynth-aaai23/tree/main/numsynth/examples/numeric-zendo2)
- dataset contains 60 examples, 30 positive and 30 negative

## 2.1 Obtaining a solution
Once you have succesfully installed Popper, download the `rdf2popper_numeric-zendo2` folder.
These are some changes in the `bias.pl` from the source dataset, as any _n_-ary relation (where _n > 2_) is transformed into set of binary relations. The changes are as follows:
| **Original bias lines** | **Changed bias lines** |
| :----------------------------------- | :------------------------------------------- |
| body_pred(position,3).            | body_pred(position_p1,2).                  |
|                                      | body_pred(position_p2,2).                  |
|                                      | body_pred(position_p3,2).                  |
| type(position,(piece,real,real)). | type(position_p1,(piece,piece)).          |
|                                      | type(position_p2,(piece,real)).          |
|                                      | type(position_p3,(piece,real)).           |
| direction(position,(in,out,out)). | direction(position_p1,(in,out)).          |
|                                      | direction(position_p2,(in,out)).          |
|                                      | direction(position_p3,(in,out)).          |

After getting the folder, run numsynth-aaai23 (as there are numerical values in this dataset) and let it produce solution.

The solution on **rdf2popper_numeric-zendo2** dataset:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:30 FN:0 TN:30 FP:0 Size:10
zendo(A):- piece(A,D),rotation(D,B),geq(B,0.94),leq(B,4.309).
zendo(A):- piece(A,D),position(D,B,E),add(E,B,F),leq(F,6.459).
******************************
```
## 2.1.1 Popper original solution
The Popper solution, which is the information we want to match on transformed dataset was produced by [numsynth-aaai23 branch of Popper](https://github.com/celinehocquette/numsynth-aaai23/tree/main). The solution was produced on unchanged dataset and is as follows:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:30 FN:0 TN:30 FP:0 Size:15
zendo(A):- piece(A,B),size(B,D),leq(D,4.069),geq(D,3.0).
zendo(A):- piece(A,D),rotation(D,B),geq(B,5.07),leq(B,5.179).
zendo(A):- piece(A,D),rotation(D,B),geq(B,0.94),leq(B,4.309).
******************************
```
## 3. trains1
- dataset [source](https://github.com/logic-and-learning-lab/Popper/tree/main/examples/trains1)
- dataset contains 1 000 examples, 394 positive and 606 negative

## 2.1 Obtaining a solution
Once you have succesfully installed Popper, download the `rdf2popper_trains1` folder.
To generate the original Popper result, the bias was left to default. No adjustments in original bias were needed for the dataset converted by `rdf2popper`.

After getting the folder, run Popper or numsynth-aaai23 and let it produce solution.

The solution on **rdf2popper_trains1** dataset:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:394 FN:0 TN:606 FP:0 Size:6
f(A):- has_car(A,C),three_wheels(C),has_car(A,B),long(B),roof_closed(B).
******************************
```
## 2.1.1 Popper original solution
The Popper solution, which is the information we want to match on transformed dataset was produced by [Popper](https://github.com/logic-and-learning-lab/Popper). The solution was produced on unchanged dataset and is as follows:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:394 FN:0 TN:606 FP:0 Size:6
f(A):- has_car(A,B),long(B),roof_closed(B),has_car(A,C),three_wheels(C).
******************************
```
## 4. imdb3
- dataset [source](https://github.com/logic-and-learning-lab/Popper/tree/main/examples/trains1)
- dataset contains 121 801 examples, 4 075 positive and 117 726 negative

## 4.1 Obtaining a solution
Once you have succesfully installed Popper, download the `rdf2popper_imdb3` folder.
To generate the original Popper result, the bias was left to default. No adjustments in original bias were needed for the dataset converted by `rdf2popper`.

After getting the folder, run Popper or numsynth-aaai23 and let it produce solution.

The solution on **rdf2popper_imdb3** dataset:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:4075 FN:0 TN:117726 FP:0 Size:10
f(A,B):- actor(A),director(B),movie(C,B),movie(C,A).
f(A,B):- gender(B,C),gender(A,C),movie(D,A),movie(D,B).
******************************
```
## 4.1.1 Popper original solution
The Popper solution, which is the information we want to match on transformed dataset was produced by [Popper](https://github.com/logic-and-learning-lab/Popper). The solution was produced on unchanged dataset and is as follows:
```
********** SOLUTION **********
Precision:1.00 Recall:1.00 TP:4060 FN:15 TN:10000 FP:0 Size:10
f(A,B):- movie(C,B),director(B),actor(A),movie(C,A).
f(A,B):- movie(C,B),movie(C,A),gender(A,D),gender(B,D).
******************************
```
