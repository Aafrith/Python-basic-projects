def main():  # Define the main function that will execute the email slicer logic
    print("Welcome to the email slicer")  # Print a welcome message
    print("")  # Print an empty line for spacing

    email_input = input("Input your email address : ")  # Prompt the user to input their email address

    (username, domain) = email_input.split("@")  # Split the email into username and domain at the '@' symbol
    (domain, extension) = domain.split(".")  # Further split the domain into the domain name and extension at the '.' symbol

    print("Username: ", username)  # Print the extracted username
    print("Domain: ", domain)  # Print the extracted domain
    print("Extension: ", extension)  # Print the extracted extension

main()  # Call the main function to execute the code
