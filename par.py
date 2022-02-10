import copy
from treeplotter.tree import Node, Tree
from treeplotter.plotter import create_tree_diagram


def parse_file(file_name: str):
    file = open(file_name)
    s = file.read().replace("\n", " ")
    file.close()
    return build_tree(s)


def build_tree(s: str, wai='root') -> Node:
    if_index = s.find("if")
    # this_node = Node(value=None, name=wru + str(v))
    this_node = Node(value=None, name=wai)

    this_node.children = []
    then_index = -1

    # if it's the smallest unit. (base case)
    if ('if' not in s) and ('then' not in s) and ('else' not in s):
        this_node.value = s
        return this_node

    # handle condition part
    after_if = copy.deepcopy(s[if_index + 3:])
    if ('if' in after_if) and (after_if.find('if') < after_if.find('then')):
        current_index = after_if.find('then', after_if.find('then') + 4)
        while not (after_if[:current_index].count('then') ==
                   after_if[:current_index].count('else') ==
                   after_if[:current_index].count('if')):
            current_index = after_if.find('then', current_index + 4)
        then_index = current_index + if_index + 3
        this_node.children.append(build_tree(after_if[:current_index], wai='condition'))
    else:
        then_index = s.find("then")
        this_node.children.append(build_tree(s[(if_index + 3):then_index], wai='condition'))

    # find where then part ends
    then_start = then_index + 4
    sbs = s[then_start:]

    then_count = 1
    else_count = 0

    sep_index = then_index + 4
    while then_count != else_count:
        then_index = sbs.find("then")
        else_index = sbs.find("else")

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

    then_part = s[then_start:sep_index - 4]
    else_part = sbs

    this_node.children.append(build_tree(then_part, wai='then'))
    this_node.children.append(build_tree(else_part, wai='else'))
    return this_node


# (full sentence, expression, current index)
def parse_exp(sentence: str, exp: str, i: int) -> bool:
    shorten = ''.join(filter(str.isalpha, exp))
    for c in shorten:
        if i < 0 or i > len(sentence):
            raise 'invalid index'
        if c == 'P':
            i -= 1
        elif c == 'S':
            i += 1
        else:
            if not sentence[i] == c:
                return False

    return True


def parse(sentence: str, exp: str):
    root = build_tree("if if a(x) then true else false then if b(x) then c(x) else d(x) else c(P(x))")
    tree = Tree(root=root)
    print(tree)
    return None


# exp: "if if a(x) then TRUE else FALSE then if b(x) then c(x) else d(x) else c(P(x))"
# Usage:
# node.children[0~2] = condition node, then node, else node {node obj}
# node.value = string of condition                          { P(x), S(x), }
# node.name = type of node (Who Am I)                       { 'root', 'then', 'else', 'condition' }


# root = build_tree("if if a(x) then true else false then if b(x) then c(x) else d(x) else c(P(x))")
# root = build_tree("if a(x) then if b(x) then g(S(x)) else d(x) else c(P(x))")
#
# tree = Tree(root=root)
# print(tree)
# print(root.children)
# print(root.children[0].children)
# then_cod = root.children[1].children
# print(then_cod[0].value)
# print(root.children[2].children)

#    01234
s = 'xfadf'
exs = 'P(P(P(P(x)))))'
print(parse_exp(s, exs, 4))
