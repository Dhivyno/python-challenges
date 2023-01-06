def print_list(node):
    output = "["
    while node is not None:
        output += str(node)
        if node.next is not None:
            output += ", "
        node = node.next
    output += "]"
    print(output)
