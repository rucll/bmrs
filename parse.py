import copy
from treeplotter.tree import Node, Tree
from treeplotter.plotter import create_tree_diagram


def build_tree(sentence: str, wai='root'):
    if_index = sentence.find("IF")
    this_node = Node(value=None, name=wai)

    this_node.children = []
    then_index = -1

    # if it's the smallest unit.(base case)
    if ('IF' not in sentence) and ('THEN' not in sentence) and ('ELSE' not in sentence):
        this_node.value = sentence.strip()
        return this_node

    # handle condition part
    after_if = copy.deepcopy(sentence[if_index + 3:])
    if ('IF' in after_if) and (after_if.find('IF') < after_if.find('THEN')):
        current_index = after_if.find('THEN', after_if.find('THEN') + 4)
        while not (after_if[:current_index].count('IF')==
                   after_if[:current_index].count('ELSE') ==
                   after_if[:current_index].count('THEN')):
            current_index = after_if.find('THEN', current_index + 4)
        then_index = current_index + if_index + 3
        this_node.children.append(build_tree(after_if[:current_index], wai='condition'))
    else:
        then_index = sentence.find('THEN')
        this_node.children.append(build_tree(sentence[(if_index + 3):then_index], wai='condition'))

    # find where then part ends
    then_start = then_index + 4
    sbs = sentence[then_start:]

    then_count = 1
    else_count = 0

    sep_index = then_index + 4
    while then_count != else_count:
        then_index = sbs.find("THEN")
        else_index = sbs.find("ELSE")

        # next one is then
        if (then_index != -1 and then_index < else_index) or else_index == -1:
            then_count = then_count + 1
            sbs = sbs[then_index + 4:]
            sep_index = sep_index + then_index + 4
            continue

        # next one is else
        if (else_index != -1 and else_index < then_index) or then_index == -1:
            else_count = else_count + 1
            sbs = sbs[else_index + 4:]
            sep_index = sep_index + else_index + 4
            continue

    then_part = sentence[then_start:sep_index - 4].strip()
    else_part = sbs.strip()

    this_node.children.append(build_tree(then_part, wai='THEN'))
    this_node.children.append(build_tree(else_part, wai='ELSE'))
    return this_node

# (full sentence, expression, current index)
# process functionName(f2(f3(f4(f5(x))))
def parse_exp(sentence: str, exp: str, i: int):
    i = i + exp.count('S') - exp.count('P')
    if i < 0 or i > len(sentence):
        raise 'invalid index'
    return i
