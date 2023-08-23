# base64

# import base64

# binary_data = b"Hello, Base64!"

# encoded_data = base64.b64encode(binary_data)

# print("Encoded Data:", encoded_data.decode("utf-8"))



import base64

encoded_data = b"SGVsbG8sIEJhc2U2NCE="

decoded_data = base64.b64decode(encoded_data)

print("Decoded Data:", decoded_data.decode("utf-8"))
