# rdf2popper
## Package overview
This package contains method for converting RDF N-Triples knowledge graphs to datasets used by the ILP system [Popper](https://github.com/logic-and-learning-lab/Popper).
## Dependencies
- none
## Input
- `.nt` file containing all triples
## Output
- `bk.pl`
- `exs.pl`
- `bias.pl`
## Example
This example is also covered in `rdf2poper_usage.ipynb`.
**rdf2popper** has three required input parameters. Most of the parameters have default values and can be ignored.

- file_name
    - name of N-Triples file without .nt extension
- head_pred_name
    - name of head predicate (predicate symbol of positive examples)
- negative_predicate
    - predicate symbol of negative examples
    - if left empty, the positive one is used with false value at the object position
- output_directory: output
    - name of prefix appended to output directory
- output_prefix: rdf2popper
    - name of prefix appended to output for particular dataset directory
- universal_predicate_1: has_property
        - predicate symbol name for unary atoms
        - works automatically for **rdf:type** predicates
- unary_exs_values: [true, false] list
    - list of true/false values for unary examples recognition

The following line of code will generate the output from the input files to the "output" folder, if the .nt file is present in the current directory. Before running the code, define the name of the input .nt file minus the extension, positive and negative predicate, if needed.
```  
nt_file_name = "" # enter .nt file name
positive_exs_pred = "" # enter predicate symbol denoting positive examples
negative_exs_pred = "" # enter predicate symbol denoting negative examples
rdf2popper(nt_file_name, positive_exs_pred, negative_exs_pred)
```
