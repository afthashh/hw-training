import ast

code_snippet = """
def greet(name):
    return f"Hello, {name}!"
"""

parsed_ast = ast.parse(code_snippet)

for node in ast.walk(parsed_ast):
    print(node)
