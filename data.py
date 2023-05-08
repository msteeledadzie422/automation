import re


def extract_data(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Extract phone numbers and email addresses using regular expressions
    phone_numbers = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', data)
    email_addresses = re.findall(r'[\w\.-]+@[\w\.-]+', data)

    # Convert phone numbers to xxx-yyy-zzzz format
    for i in range(len(phone_numbers)):
        phone_number = re.sub(r'\D', '', phone_numbers[i])
        if len(phone_number) == 10:
            phone_numbers[i] = f'{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}'
        else:
            phone_numbers[i] = f'206-{phone_number[:3]}-{phone_number[3:]}'

    return phone_numbers, email_addresses


def write_to_files(phone_numbers, email_addresses):
    # Create phone_numbers.txt and write phone numbers to it
    with open('phone_numbers.txt', 'w') as file:
        for phone_number in phone_numbers:
            file.write(f'{phone_number}\n')
    print(f'Phone numbers saved to phone_numbers.txt')

    # Create email_addresses.txt and write email addresses to it
    with open('email_addresses.txt', 'w') as file:
        for email_address in email_addresses:
            file.write(f'{email_address}\n')
    print(f'Email addresses saved to email_addresses.txt')


def main():
    file_path1 = 'assets/existing_contacts.txt'
    phone_numbers, email_addresses = extract_data(file_path1)
    write_to_files(phone_numbers, email_addresses)

    # Print the contents of the phone_numbers.txt file
    with open('phone_numbers.txt', 'r') as file:
        phone_numbers_content = file.read()
        print('phone_numbers.txt contents:')
        print(phone_numbers_content)

    # Print the contents of the email_addresses.txt file
    with open('email_addresses.txt', 'r') as file:
        email_addresses_content = file.read()
        print('email_addresses.txt contents:')
        print(email_addresses_content)

    file_path2 = 'assets/potential_contacts.txt'
    phone_numbers, email_addresses = extract_data(file_path2)
    write_to_files(phone_numbers, email_addresses)

    # Print the contents of the phone_numbers.txt file
    with open('phone_numbers.txt', 'r') as file:
        phone_numbers_content = file.read()
        print('phone_numbers.txt contents:')
        print(phone_numbers_content)

    # Print the contents of the email_addresses.txt file
    with open('email_addresses.txt', 'r') as file:
        email_addresses_content = file.read()
        print('email_addresses.txt contents:')
        print(email_addresses_content)


if __name__ == '__main__':
    main()
