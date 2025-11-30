# This function takes a filepath (like "books/frankenstein.txt") as input
# and returns all the text inside that file as one big string
def get_book_text(filepath):
    # open() opens the file so we can read it
    # "with" automatically closes the file when we're done (good practice!)
    with open(filepath) as f:
        # f.read() reads the ENTIRE file content as a single string
        # return sends that string back to whoever called this function
        return f.read()


# This function takes a string of text and counts how many words are in it
# It returns an integer (a number) representing the word count
def count_words(text):
    # .split() is a string method that breaks a string into a LIST of words
    # By default, it splits on whitespace (spaces, tabs, newlines)
    #
    # Example: "hello world foo".split() returns ['hello', 'world', 'foo']
    #
    # We store this list in a variable called "words"
    words = text.split()

    # len() counts how many items are in a list
    # Since each item in our list is one word, len(words) = number of words
    #
    # Example: len(['hello', 'world', 'foo']) returns 3
    #
    # return sends this number back to whoever called the function
    return len(words)


# This is our main function - it's like the "control center" of our program
# It coordinates calling the other functions and printing results
def main():
    # Step 1: Call get_book_text() and store the result in "text"
    # After this line, "text" contains the entire book as a string
    text = get_book_text("books/frankenstein.txt")

    # Step 2: Call count_words() and pass it our text
    # The function will split the text and count the words
    # We store the result (a number) in "word_count"
    word_count = count_words(text)

    # Step 3: Print the result so we can see it
    print(word_count)


# This line actually RUNS our main() function
# Without this, we'd just be defining functions but never calling them
#
# IMPORTANT: Everything above this line is just DEFINING functions
# Nothing actually happens until we call main() here
main()
