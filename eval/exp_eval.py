from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    postfix_stack = Stack(30)
    str_list = input_str.split()
    operands = 0
    operators = 0
    if input_str == '':
        raise PostfixFormatException("Empty input")
    for char in str_list:
        if char.isdigit() or (char.replace(".", "").isdigit() and char.count('.') == 1) or (
                char.replace("-", "").isdigit() and char.count("-") == 1) or \
                (char.translate({ord(i): None for i in '-.'}).isdigit() and len(char) > 1):
            operands += 1
        elif char == "+" or char == "-" or char == "*" or char == "/" or char == "**" or char == ">>" or char == "<<":
            operators += 1
        else:
            raise PostfixFormatException("Invalid token")
    if operands > operators + 1:
        raise PostfixFormatException("Too many operands")
    elif operands < operators + 1:
        raise PostfixFormatException("Insufficient operands")
    for char in str_list:
        if char.isnumeric() or (char.replace("-", "").isdigit() and char.count("-") == 1):
            postfix_stack.push(int(char))
        elif (char.replace(".", "").isdigit() and char.count('.') == 1) or (
                ((char.translate({ord(i): None for i in '-.'}).isdigit() and len(char) > 1))):
            postfix_stack.push(float(char))
        elif char == "+":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            postfix_stack.push(first_val + second_val)
        elif char == "-":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            postfix_stack.push(second_val - first_val)
        elif char == "*":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            postfix_stack.push(first_val * second_val)
        elif char == "/":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            if first_val != 0:
                postfix_stack.push(float(second_val / first_val))
            else:
                raise ValueError
        elif char == "**":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            postfix_stack.push(second_val ** first_val)
        elif char == ">>":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            try:
                postfix_stack.push(second_val >> first_val)
            except:
                raise PostfixFormatException("Illegal bit shift operand")
        elif char == "<<":
            first_val = postfix_stack.pop()
            second_val = postfix_stack.pop()
            try:
                postfix_stack.push(second_val << first_val)
            except:
                raise PostfixFormatException("Illegal bit shift operand")

    return postfix_stack.pop()


def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    operator_precedence = {">>": 4, "<<": 4, "**": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
    infix_list = input_str.split()
    operator_stack = Stack(30)
    postfix_list = []
    for char in infix_list:
        if char.isdigit() or (char.replace(".", "").isdigit() and char.count('.') == 1) or (
                char.replace("-", "").isdigit() and char.count("-") == 1) or \
                (char.translate({ord(i): None for i in '-.'}).isdigit() and len(char) > 1):
            postfix_list.append(char)
        elif char == "(":
            operator_stack.push(char)
        elif char == ")":
            while operator_stack.peek() != "(":
                postfix_list.append(operator_stack.pop())
            operator_stack.pop()
        else:
            for i in range(operator_stack.size()):
                if (char != "**" and operator_precedence[char] <= operator_precedence[operator_stack.peek()]) or (
                        char == "**" and 3 < operator_precedence[operator_stack.peek()]):
                    postfix_list.append(operator_stack.pop())
            operator_stack.push(char)
    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())
    return ' '.join(postfix_list)


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    conversion_stack = Stack(30)
    operators = ["+", "-", "*", "/", "**", ">>", "<<"]
    str_list = input_str.split()
    str_list = str_list[::-1]
    for char in str_list:
        if char in operators:
            first_val = conversion_stack.pop()
            second_val = conversion_stack.pop()
            concat_str = first_val + " " + second_val + " " + char
            conversion_stack.push(concat_str)
        else:
            conversion_stack.push(char)
    return conversion_stack.pop()
