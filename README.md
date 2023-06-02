# Palindrome Checker
The Palindrome Checker is a Python class that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization.

#Usage
To use the Palindrome Checker, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the Palindrome Checker code.
3. Open a terminal or command prompt and navigate to the directory where the code is located.

Run the following command to execute the program:
python palindrome_checker.py

You will be prompted to enter a string. Type the string you want to check and press Enter.
The program will output whether the entered string is a palindrome or not.

Example:
Enter a Value: madam
Is a Palindrome

Test:-
The Palindrome Checker includes unit tests using the pytest framework. To run the tests, follow these steps:

1.Ensure you have pytest installed. If not, you can install it using the following command:
2.Copy code
3.pip install pytest
4.Open a terminal or command prompt and navigate to the directory where the code is located.
5.Run the following command to execute the tests:
6.Copy code
7.pytest -v
The tests will be executed, and the test results will be displayed in the console.

Additional Notes:-
The Palindrome Checker class uses regular expressions to remove non-alphanumeric characters from the input string.
The class raises a ValueError if a non-string value is provided as input.

