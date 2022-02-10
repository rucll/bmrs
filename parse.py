import copy
from structure import Node


def parse_file(file_name: str):
    file = open(file_name)
    s = file.read().replace("\n", " ")
    file.close()
    return parse(s)


# takes in s such as only the then, else parts of an entire statement
# if <condition> then <terms> else <terms>

def parse(s: str) -> Node:
    if_index = s.find("if")
    this_node = Node()
    then_index = -1
    if ('if' not in s) and ('then' not in s) and ('else' not in s):
        this_node.condition = s
        return this_node
    # handle condition part
    after_if = copy.deepcopy(s[if_index + 3:])
    if ('if' in after_if) and (after_if.find('if') < after_if.find('then')):
        current_index = after_if.find('then', after_if.find('then') + 4)
        while not (after_if[:current_index].count('then') == after_if[:current_index].count('else') == after_if[:current_index].count('if')):
            current_index = after_if.find('then', current_index + 4)
        then_index = current_index + if_index + 3
        this_node.condition = parse(after_if[:current_index])
    else:
        then_index = s.find("then")
        this_node.condition = s[(if_index + 3):then_index]
    # _____________________________________

    sbs = s[then_index + 4:]
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

        if then_index == -1 and else_index == -1:
            raise "weird stuff"

    then_part = s[s.find("then") + 4:sep_index - 4]
    else_part = sbs
    this_node.the = parse(then_part)
    this_node.els = parse(else_part)
    return this_node


# root = parse("if if a(x) then true else false then if b(x) then c(x) else d(x) else c(p(x))")
root = parse("if if a(x) then TRUE else FALSE then if b(x) then c(x) else d(x) else c(p(x))")
print(root.condition)
print(root.the.condition)
print(root.the.the.condition)
print(root.els.condition)
