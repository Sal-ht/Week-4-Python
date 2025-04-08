# question 

    # define the function modify_file
def modify_file():
    input_file = input("Enter the name of the file to read: ")
    output_file = "modified_" + input_file

    # Open the file in read mode
    file = open(input_file, 'r')
    content = file.read()
    file.close()

    # Modify content
    modified_content = content.upper()

    # Write the modified content to a new file
    file = open(output_file, 'w')
    file.write(modified_content)
    file.close()

    print(f"Modified content saved to '{output_file}'.")

# Run the function
modify_file()

# With Error Handling
def modify_file():
    input_file = input("Enter the name of the file to read: ")
    output_file = "modified_" + input_file

# Initiate the Try-except Block
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            print(content)
            print("\nFile read successfully.")


        # Modify content to uppercase
        modified_content = content.upper()

        with open(output_file, 'w') as file:
            file.write(modified_content)
            print(f"Modified content saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_file}'.")

modify_file()
