import os
import re

def rdf2popper(file_name, head_pred_name='', negative_predicate='', mode='popper', output_directory='output', output_prefix = 'rdf2popper',
               universal_predicate_1='has_property', unary_exs_values=None):
    """
    Method for converting N-Triples to Popper Prolog files.
    :param mode: select mode (ILP system) to format the output files; popper (default), aleph, general (puts everything to one .pl file)
    :param file_name: name of N-Triples file without .nt extension
    :param head_pred_name: name of head predicate (predicate symbol of positive examples)
    :param negative_predicate: predicate symbol of negative examples
    :param output_directory: name of output directory
    :param output_prefix: name of prefix appended to output for particular dataset directory
    :param universal_predicate_1: predicate symbol name for unary atoms
    :param unary_exs_values: list of true/false values for unary examples recognition
    :return: folder containing three Prolog files - BK, exs, bias
    """
    input_file = f'{file_name}.nt'

    if mode not in ['popper', 'aleph', 'general']:
        raise ValueError('Mode must be one of popper, aleph, general.')

    if mode == 'popper':

        output_file_bias = f'{output_directory}\\{output_prefix}_{file_name}\\bias.pl'
        output_file_bk = f'{output_directory}\\{output_prefix}_{file_name}\\bk.pl'
        output_file_exs = f'{output_directory}\\{output_prefix}_{file_name}\\exs.pl'

    if mode == 'aleph':

        output_file_bk = f'{output_directory}\\{output_prefix}_{file_name}\\{file_name}.b'
        output_file_negative_exs = f'{output_directory}\\{output_prefix}_{file_name}\\{file_name}.n'
        output_file_positive_exs = f'{output_directory}\\{output_prefix}_{file_name}\\{file_name}.f'

    if mode == 'general':
        output_file_pl = f'{output_directory}\\{output_prefix}_{file_name}\\{file_name}_general.pl'

    # default negative predicate if not provided
    if negative_predicate is None:
        negative_predicate = head_pred_name

    # default values for unary atoms input exs
    if unary_exs_values is None or not isinstance(unary_exs_values, list) or len(unary_exs_values) != 2:
        unary_exs_values = ['true', 'false']

    # create output directory structure
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    if not os.path.exists(f'{output_directory}/{output_prefix}_{file_name}'):
        os.mkdir(f'{output_directory}/{output_prefix}_{file_name}')

    triples = []

    with open(input_file, 'r') as f:
        for line in f:
            parts = line.split(' ')
            if len(parts) < 4 or len(parts) > 5:
                raise ValueError(f'Wrong number of values in line "{line}"')
            subj = parts[0][1:-1]
            pred = parts[1][1:-1]
            obj = parts[2]

            if obj[0] == '<':
                obj = obj[1:-1]
            else:
                pattern = re.compile(r'"(.*)".*')
                match = pattern.match(obj)
                if match:
                    obj = match.group(1)
                else:
                    raise ValueError(f'Invalid object "{obj}"')
            triples.append((subj, pred, obj))

    if mode != 'general':

        if head_pred_name not in [val[1] for val in triples]:
            raise ValueError(f'Missing head predicate in the {input_file}')

        exs_list = []
        bk_list = []

        for triple in triples:
            if triple[1] == head_pred_name or triple[1] == negative_predicate:
                exs_list.append(triple)
            else:
                bk_list.append(triple)

        # BIAS

        bias_output_list = []

        # head_pred
        # arity 1
        if negative_predicate not in [val[1] for val in exs_list] and len([val[2] for val in exs_list if val[2] not in unary_exs_values]) == 0:
            bias_output_list.append(f'head_pred({head_pred_name},1).')
        # arity 2
        elif len([val[1] for val in exs_list if val[1] not in [head_pred_name, negative_predicate]]) == 0:
            bias_output_list.append(f'head_pred({head_pred_name},2).')
        # arity > 2 - error for now
        else:
            raise ValueError('Arity > 2 not implemented yet.')

        # body_pred
        # GREATER_ARITY_SUFFIX_1 = ['_p1']
        # GREATER_ARITY_SUFFIX_2 = ['_p2']
        # GREATER_ARITY_SUFFIX_3 = ['_p3']
        body_pred_list_1 = []
        body_pred_list_2 = []
        # body_pred_list_3 = []

        if mode == 'popper':
            for triple in bk_list:
                # arity 1
                if triple[1] == universal_predicate_1 or triple[1] == 'rdf:type':
                    if triple[2] not in body_pred_list_1:
                        body_pred_list_1.append(triple[2])
                        bias_output_list.append(f'body_pred({triple[2]},1).')
                # TODO: everything else goes to arity 2. Other arities must be added.
                # elif triple[1][-3:] input GREATER_ARITY_SUFFIX_1:
                #     if triple[1] not input body_pred_list_3:
                #         body_pred_list_3.append(triple[1])
                #         bias_output_list.append(f'body_pred({triple[1]},1).')
                # elif triple[1][-3:] input GREATER_ARITY_SUFFIX_2:
                #     if triple[1] not input body_pred_list_3:
                #         body_pred_list_3.append(triple[1])
                #         bias_output_list.append(f'body_pred({triple[1]},2).')
                # elif triple[1][-3:] input GREATER_ARITY_SUFFIX_3:
                #     if triple[1] not input body_pred_list_3:
                #         body_pred_list_3.append(triple[1])
                #         bias_output_list.append(f'body_pred({triple[1]},2).')
                else:
                    if triple[1] not in body_pred_list_2:
                        body_pred_list_2.append(triple[1])
                        bias_output_list.append(f'body_pred({triple[1]},2).')

            with open(output_file_bias, 'w') as f:
                f.write('\n'.join(bias_output_list))

        # BK

        bk_output_list = []
        # greater_arity_helper_1 = {}
        # greater_arity_helper_2 = {}
        # greater_arity_helper_3 = {}

        for triple in bk_list:
            if triple[1] == universal_predicate_1:
                bk_output_list.append(f'{triple[2]}({triple[0]}).')
            else:
                s = triple[0].replace(':', '_').replace('/', '_').replace('(', '_').replace('.', '_').replace(',', '_').replace(')', '_')
                bk_output_list.append(f'{triple[1]}({s},{triple[2]}).')

        # TODO: arity > 2

        if mode == 'popper':
            with open(output_file_bk, 'w') as f:
                f.write(':-style_check(-discontiguous)\n')
                f.write('\n'.join(bk_output_list))

        if mode == 'aleph':
            with open(output_file_bk, 'w') as f:
                f.write('\n'.join(bk_output_list))
        # EXS

        exs_output_list_pos = []
        exs_output_list_neg = []

        if mode == 'popper':
            for triple in exs_list:
                if triple[2] == unary_exs_values[0]:
                    exs_output_list_pos.append(f'{triple[1]}({triple[0]})')
                elif triple[2] == unary_exs_values[1]:
                    exs_output_list_neg.append(f'{triple[1]}({triple[0]})')
                elif triple[1] == negative_predicate:
                    exs_output_list_neg.append(f'{head_pred_name}({triple[0]},{triple[2]})')
                else:
                    exs_output_list_pos.append(f'{triple[1]}({triple[0]},{triple[2]})')

            with open(output_file_exs, 'w') as f:
                for line in exs_output_list_pos:
                    f.write(f'pos({line}).\n')
                for line in exs_output_list_neg:
                    f.write(f'neg({line}).\n')

        if mode == 'aleph':
            for triple in exs_list:
                if triple[2] == unary_exs_values[0]:
                    exs_output_list_pos.append(f'{triple[1]}({triple[0]}).')
                elif triple[2] == unary_exs_values[1]:
                    exs_output_list_neg.append(f'{triple[1]}({triple[0]}).')
                elif triple[1] == negative_predicate:
                    exs_output_list_neg.append(f'{head_pred_name}({triple[0]},{triple[2]}).')
                else:
                    exs_output_list_pos.append(f'{triple[1]}({triple[0]},{triple[2]}).')

            with open(output_file_positive_exs, 'w') as f:
                for line in exs_output_list_pos:
                    f.write(f'{line}\n')

            with open(output_file_negative_exs, 'w') as f:
                for line in exs_output_list_neg:
                    f.write(f'{line}\n')

        if mode == 'general':
            triples_output_list = []

            for triple in triples:
                if triple[1] == universal_predicate_1:
                    triples_output_list.append(f'{triple[2]}({triple[0]}).')
                else:
                    s = triple[0].replace(':', '_').replace('/', '_').replace('(', '_').replace('.', '_').replace(',',
                                                                                                                  '_').replace(
                        ')', '_')
                    triples_output_list.append(f'{triple[1]}({s},{triple[2]}).')

            with open(output_file_pl, 'w') as f:
                f.write('\n'.join(triples_output_list))