import js2py

# Define a JavaScript function
js_code = """
function add(a, b) {
    return a + b;
}
"""

# Execute the JavaScript code
js_context = js2py.EvalJs()
js_context.execute(js_code)

# Call the JavaScript function
result = js_context.add(5, 3)
print("Result:", result)
