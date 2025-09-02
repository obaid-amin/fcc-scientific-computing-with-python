problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
show_answers = True

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged = ""
    parsed = [p.split() for p in problems]
    widths = [max(len(left), len(right)) + 2 for left, op, right in parsed]

    # First line (left operands)
    for (left, op, right), w in zip(parsed, widths):
        arranged += left.rjust(w) + "    "
    arranged = arranged.rstrip() + "\n"

    # Second line (operator + right operand)
    for (left, op, right), w in zip(parsed, widths):
        arranged += op + right.rjust(w - 1) + "    "
    arranged = arranged.rstrip() + "\n"

    # Dashes line
    for w in widths:
        arranged += "-" * w + "    "
    arranged = arranged.rstrip()

    # Answers (if enabled)
    if show_answers:
        arranged += "\n"
        for (left, op, right), w in zip(parsed, widths):
            result = str(int(left) + int(right)) if op == '+' else str(int(left) - int(right))
            arranged += result.rjust(w) + "    "
        arranged = arranged.rstrip()

    return arranged


print(arithmetic_arranger(problems, show_answers))
