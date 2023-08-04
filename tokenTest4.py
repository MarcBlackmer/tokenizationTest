import re
import sys

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt).strip())
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

def tokenize_transcript(file_path):
    try:
        # Reading the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Prompting for your company name
        my_company_name = input("Please enter the name of your company (leave blank if not mentioned): ").strip()
        if my_company_name:
            content = content.replace(my_company_name, "[MY_COMPANY]")

        # Prompting for product name
        product_name = get_non_empty_input("Please enter the product name: ")
        content = content.replace(product_name, "[PRODUCT]")

        # Prompting for competitor names
        num_competitors = get_integer_input("Enter the number of competitor names (0 if none): ")
        for i in range(num_competitors):
            competitor_name = get_non_empty_input(f"Enter competitor name {i+1}: ")
            content = content.replace(competitor_name, "[COMPETITOR]")

        # Prompting for customer company name
        customer_company_name = get_non_empty_input("Enter the customer company name: ")
        content = content.replace(customer_company_name, "[CUSTOMER_COMPANY]")

        # Prompting for customer names, nicknames, and titles
        num_customers = get_integer_input("Enter the number of customers: ")
        for i in range(num_customers):
            customer_first_name = get_non_empty_input(f"Enter customer first name {i+1}: ")
            customer_last_name = get_non_empty_input(f"Enter customer last name {i+1}: ")
            customer_nickname = input(f"Enter customer nickname {i+1} (if any): ").strip()
            customer_title = input(f"Enter customer title {i+1} (if any): ").strip()
            content = content.replace(customer_first_name + " " + customer_last_name, "[CUSTOMER]")
            content = content.replace(customer_first_name, "[CUSTOMER]")
            if customer_nickname:
                content = content.replace(customer_nickname, "[CUSTOMER]")
            if customer_title:
                content = content.replace(customer_title, "[TITLE]")

        # Writing the tokenized content to a new file
        output_file_path = file_path.replace('.txt', '_tokenized.txt')
        with open(output_file_path, 'w') as file:
            file.write(content)

        print(f"Tokenized file saved to {output_file_path}")

    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Check if the script received a command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 script.py path/to/transcript.txt")
else:
    # Retrieve the file path from the command-line argument
    file_path = sys.argv[1]
    tokenize_transcript(file_path)
