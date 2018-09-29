# Since the module is not in the same layer, we need to add the related path in examples
import sys
sys.path.append('../')

from GriiidPyCliMenu import CliMenuList

words_items = [
    "good", "goodbye", "hello", "morning", "afternoon", "night", "book", "book bag", "chair", "desk", "erase", "pen", "pencil", "pencil box", "ruler", "computer", "father", "mother", "grandfather", "grandmother", "brother", "sister", "girl", "boy", "student", "friend", "ear", "eye", "foot", "hair", "hand", "leg", "mouth", "nose", "apple", "banana", "case", "egg", "juice", "milk", "pizza", "tea", "water", "cat", "dog", "fish", "lion", "pig", "tiger", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "home", "park", "school", "black", "blue", "brown", "green", "orange", "red", "white", "yellow", "hat", "jacket", "shoes", "big", "cold", "fat", "hot", "new", "old", "short", "small", "tall", "am", "are", "cook", "eat", "go", "has", "have", "is", "like", "play", "read", "run", "see", "sing", "sleep", "bus", "car", "he", "her", "his", "it", "me", "my", "she", "they", "we", "you", "your", "teacher", "in", "on", "happy", "sad", "name", "no", "yes"
]

cli_list = CliMenuList(title="CLI LIST DEMO", items_per_page=5)
cli_list.add_item(words_items)

word = cli_list.prompt()
print("Choose: " + word)

# Clear items and add new list
number_items = [str(x) for x in range(0, 12)]
cli_list.set_title('CHOOSE NUMBER')
cli_list.set_items_per_page(len(number_items))
cli_list.clear()
cli_list.add_item(number_items)
number = cli_list.prompt()
print("Choose: " + number)