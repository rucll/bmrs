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
    then_index = s.find("then")
    this_node = Node()
    this_node.condition = s[(if_index + 2):then_index]

    if s.count("then") == s.count("else") <= 1:
        this_node.the = s[then_index+4:s.find("else")]
        this_node.els = s[s.find("else")+4:]
        return

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
    # print(this_node.condition, "|", then_part, "|", else_part)
    this_node.the = parse(then_part)
    this_node.els = parse(else_part)
    return this_node


parse("if a(x) then if b(x) then c(x) else d(x) else c(p(x))")
