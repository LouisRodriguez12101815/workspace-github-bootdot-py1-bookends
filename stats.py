def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	var_count = {}

	for t in text:
		t = t.lower()

		if t in var_count:
			var_count[t]["count"] += 1
		else:
			var_count[t] = {"char": t, "count": 1}

	# Convert dictionary values to a list
	# var_count.values() gives us all the {"char": x, "count": y} dictionaries
	# list() converts it from a dict_values object to an actual list we can sort
	char_list = list(var_count.values())

	# Filter to keep only alphabetical characters
	alpha_list = []
	for item in char_list:
		if item["char"].isalpha():    # .isalpha() returns True for letters only
			alpha_list.append(item)   # add to our filtered list

	# Sort by count, greatest to smallest
	# reverse=True = descending order (biggest first)
	# key=lambda x: x["count"] = "sort by the 'count' value inside each dictionary"
	alpha_list.sort(reverse=True, key=lambda x: x["count"])

	return(alpha_list)  # Now returns a sorted list instead of a dictionary
