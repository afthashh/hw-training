import re

text = "Contact us at support@example.com or info@example.org."

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

email_addresses = re.findall(email_pattern, text)

for email in email_addresses:
    print("Email:", email)
