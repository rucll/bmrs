import copy
from treeplotter.tree import Node, Tree
from treeplotter.plotter import create_tree_diagram


def parse_file(file_name: str):
    file = open(file_name)
    s = file.read().replace("\n", " ")
    file.close()
    return parse(s)


def parse(s: str, wru='root') -> Node:
    if_index = s.find("if")
    # this_node = Node(value=None, name=wru + str(v))
    this_node = Node(value=None, name=wru)

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
        this_node.children.append(parse(after_if[:current_index], wru='condition'))
    else:
        then_index = s.find("then")
        this_node.children.append(parse(s[(if_index + 3):then_index], wru='condition'))

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

    this_node.children.append(parse(then_part, wru='then'))
    this_node.children.append(parse(else_part, wru='else'))
    return this_node


# exp: "if if a(x) then TRUE else FALSE then if b(x) then c(x) else d(x) else c(P(x))"
# string: "ababab"
# ind: x val
def evl_helper(r, s, x):
    return None


def evl(exp, s, x):
    t = Tree(parse(s))
    return None


# root = parse("if if a(x) then true else false then if b(x) then c(x) else d(x) else c(P(x))")
root = parse("if a(x) then if b(x) then g(S(x)) else d(x) else c(P(x))")

# vis(root)

tree = Tree(root=root)
print(tree)
print(root.children)
print(root.children[0].children)
print(root.children[1].children)
print(root.children[2].children)