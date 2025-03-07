import re
def extract_equation(operand1, operator, operand2):

    equation = f"{operand1} {operator} {operand2}"
    match = re.match(r'(\d+)([+\-*/])(\d+)=(\d+)', equation)




print(extract_equation(1, "+", 2))
