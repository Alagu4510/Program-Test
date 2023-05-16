class Palindrome:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        try:
            self.value = self.value.lower()
            self.value = self.value.replace(" ", "")
            rev_value = self.value[::-1]
        except AttributeError:
            raise ValueError("Please enter a string")
        return self.value == rev_value
def main():
    value = input("Enter a string: ")
    palindrome = Palindrome(value)

    if palindrome.is_palindrome():
        print("Is a palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()


