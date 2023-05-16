import re


class PalindromeChecker:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        try:
            self.value = self.value.lower()
            self.value = re.sub(r"[^a-zA-Z0-9]", "", self.value)
            rev_value = self.value[::-1]
        except AttributeError:
            raise ValueError("Please enter a string")

        return self.value == rev_value


def main():

    value = input("Enter a Value: ")
    checker = PalindromeChecker(value)

    if checker.is_palindrome():
        print("palindrome")

    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()
