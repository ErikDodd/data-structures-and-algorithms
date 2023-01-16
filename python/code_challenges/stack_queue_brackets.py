def multi_bracket_validation(string):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in string:
        if char in brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            elif brackets[stack[-1]] != char:
                return False
            else:
                stack.pop()
    return not stack

