
def expr_perm(values, operations="+-*/", stack=[]):
    solution = []
    if len(stack) > 1:
        for op in operations:
            new_stack = list(stack)
            new_stack.append("(" + new_stack.pop() + op + new_stack.pop() + ")")
            solution += expr_perm(values, operations, new_stack)
    if values:
        for i, val in enumerate(values):
            new_values = values[:i] + values[i+1:]
            solution += expr_perm(new_values, operations, stack + [str(val)])
    elif len(stack) == 1:
        return stack
    return solution

def main():
    res = expr_perm([4,5,6,2])
    print("\n".join(res))
    #print(res)


if __name__ == "__main__":
    main()
