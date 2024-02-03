import re

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Compile the regex
    regex = re.compile(email_regex)
    
    # Check if the email matches the pattern
    if regex.match(email):
        return True
    else:
        return False

def validate_email_file(file_path):
    emails = []

    try:
        with open(file_path, 'r') as file:
            email_list = file.read().splitlines()
            k="VALID -- "
            l="INVALID -- "

        for email in email_list:
            if is_valid_email(email):
                emails.append(k+email)
            else:
                emails.append(l+email)

        return emails

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    # Example usage
file_path = "input.txt"  # Replace with your file path

emails = validate_email_file(file_path)
file=open("output.txt","w")
for item in emails:
    file.write(item+"\n")
for item in emails:
    print(item)
file.close()