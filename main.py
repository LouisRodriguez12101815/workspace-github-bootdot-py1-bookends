import sys
from stats import count_words, count_characters

def get_book_text(path):
	with open(path) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]

	# Header
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")

	text = get_book_text(book_path)
	word_count = count_words(text)
	print(f"Found {word_count} total words")

	# Section header
	print("--------- Character Count -------")

	char_count = count_characters(text)

	# Loop through a list of dictionaries instead of a dictionary
	# Before: char_count was {"a": {"char": "a", "count": 5}, ...}
	#         we looped through keys with `for char in char_count`
	# After:  char_count is [{"char": "a", "count": 5}, ...]
	#         we loop through each dictionary directly
	for item in char_count:
		print(f"{item['char']}: {item['count']}")

	# Footer
	print("============= END ===============")

main()


