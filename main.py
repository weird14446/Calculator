from typing import List, Optional
from math import gamma


def infixToPostfix(expression: str) -> str:
    expression = expression.replace(" ", "")
    s: str = ""

    Operators: set[str] = set(
        ["+", "-", "*", "/", "(", ")", "^", "=", "!", "%", "<", ">"]
    )
    Priority: dict[str, int] = {
        "<": 0,
        ">": 0,
        "=": 0,
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "%": 2,
        "^": 3,
        "!": 0,
    }
    unaryOperators: set[str] = set(["-", "+", "!"])
    stack: List[str] = []
    output: List[str] = []

    cOpers: set[str] = set(["+", "-", "*", "/", "^", "(", "=", "%", "!", "<", ">"])
    c: int = 0
    for i in range(len(expression)):
        if i == 0 and expression[i] in Operators:
            c += 1
            s += " ( 0 " + expression[i] + " "
        elif expression[i] in Operators:
            if expression[i] in unaryOperators and expression[i - 1] in cOpers:
                c += 1
                s += " ( 0 " + expression[i] + " "
            else:
                for _ in range(c):
                    s += " ) "
                c = 0
                s += " " + expression[i] + " "
        else:
            s += expression[i]

    for i in range(c):
        s += " ) "

    expressionArr: List[str] = s.split()

    for character in expressionArr:
        if character == " ":
            continue
        if character not in Operators:
            output.append(character)
        elif character == "(":
            stack.append("(")
        elif character == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            stack.pop()
        else:
            while (
                stack
                and stack[-1] != "("
                and Priority[character] <= Priority[stack[-1]]
            ):
                output.append(stack.pop())

            stack.append(character)

    while stack:
        output += stack.pop()

    return " ".join(output)


def calc(postfix: str) -> Optional[float]:
    arr: List[str] = list(postfix.split())
    stack: List[float] = []
    symbols: set[str] = set(["(", ")"])
    Operators: set[str] = set(["+", "-", "*", "/", "^", "=", "%", "!", "<", ">"])

    for i in arr:
        if i in symbols:
            continue
        elif i in Operators:
            x: float = stack.pop()
            y: float = stack.pop()
            if i == "+":
                stack.append(x + y)
            elif i == "-":
                stack.append(y - x)
            elif i == "*":
                stack.append(x * y)
            elif i == "/":
                if x == 0:
                    return None
                stack.append(y / x)
            elif i == "^":
                stack.append(y**x)
            elif i == "=":
                stack.append(x == y)
            elif i == "%":
                if x == 0:
                    None
                stack.append(y % x)
            elif i == "!":
                if x < 0:
                    return None
                stack.append(gamma(x + 1))
            elif i == "<":
                stack.append(y < x)
            elif i == ">":
                stack.append(y > x)
        else:
            stack.append(float(i))

    return stack.pop()


if __name__ == "__main__":
    s = input()
    print(infixToPostfix(s))
    print(calc(infixToPostfix(s)))
