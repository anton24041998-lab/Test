#First Question
"""
This program collects grades from the user and performs basic statistics.
How it works:
 The user is prompted to enter integer grades.
 Valid grades must be between 0 and 100 (inclusive).
 Invalid inputs (non-integers or out-of-range values) are ignored.
 Entering -999 will terminate input ONLY if at least 10 valid grades were entered.

After termination:
 The program calculates and prints:
   The average grade
   The maximum grade
   The number of valid grades entered
 If no valid grades were entered, a message is displayed.
"""
_sum = 0
grades = []
while True:
    try:
        grade = int(input('write grade: '))
    except ValueError as e:
        print('Invalid input, please enter a number', e)
        continue
    if grade == -999:
        if len(grades) >= 10:
            break
        else:
            print('need at least 10 grades')
            continue
    if grade > 100 or grade < 0:
        print('grades not in range')
        continue
    grades.append(grade)
    _sum += grade
if len(grades) == 0:
    print('no grades')
else:
    max_grade = max(grades)
    _avg = _sum / len(grades)
    print("average:", _avg)
    print('max grade:', max_grade)
    print("valid grade written:", len(grades))

#Second Question
def find_median(numbers: list) -> float:
    """
      Calculate the median of a list of values.

      The function attempts to convert all elements to floats.
      Non-numeric values are skipped, and a warning is printed
      showing their indices and values.

      Args:
          numbers (list): A list of values (numbers or numeric strings).

      Returns:
          float: The median of the valid numeric values.

      Raises:
          ValueError: If the input list is empty or contains no valid numeric values.
      """

    if not numbers:
        raise ValueError("The list must not be empty")
    converted = []
    skipped = []
    for i, x in enumerate(numbers):
        try:
            converted.append(float(x))
        except (ValueError, TypeError):
            skipped.append((i, x))
    if not converted:
        raise ValueError("No valid numeric values found")
    if skipped:
        print("Skipped non-numeric values:")
        for i, x in skipped:
            print(f"  index {i}: '{x}'")
    sorted_numbers = sorted(converted)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
print(find_median(["11",2,3,4,'gdgs']))

#Third Question
def snake_to_camel(text: str) -> str:
    """
    Convert a snake_case string to camelCase.
    Args:
        text (str): A string in snake_case format.
    Returns:
        str: The string converted to camelCase.
    Raises:
        ValueError: If the input is empty.
    """
    if not text:
        raise ValueError("Input string must not be empty")
    parts = text.split("_")
    return parts[0].lower() + "".join(word.capitalize() for word in parts[1:])
print(snake_to_camel("a_b_c_d_eeew"))

#Fourth Question
"""
    The program:
    Continuously asks the user to enter words
    Stops when the user types 'quit' 
    Converts all inputs to lowercase
    Checks if any duplicate words were entered

    Behavior:
    Prints "you didn't type anything" if no words were entered
    Prints "there was duplicates" if duplicates are found
    Prints "there was no duplicates" if all words are unique
"""
items = []
while True:
    value = input("Enter words, or type 'quit' to stop: ")
    if value.lower() == "quit":
        break
    items.append(value.lower())
if not items:
    print("you didn't type anything")
elif len(items) != len(set(items)):
    print("there was duplicates")
else:
    print("there was no duplicates")

#Fifth Question
def most_common_word(story: tuple[str, ...]) -> str:
    """
        Find the most common word in a tuple of sentences.

        The function:
         Removes punctuation by keeping only letters and spaces
         Converts all text to lowercase
         Splits sentences into individual words
         Counts how many times each word appears
         Prints the most common word and its count

        Args:
            story (tuple[str, ...]): A tuple containing sentences (strings).

        Returns:
            str: The word that appears most frequently.

        Raises:
            ValueError: If no valid words are found.

        """
    words = []
    for sentence in story:
        cleaned = ""
        for char in sentence:
            if char.isalpha() or char == " ":
                cleaned += char
        words.extend(cleaned.lower().split())
    if not words:
        raise ValueError("No words found")
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    max_word = None
    max_count = 0
    for word, count in counts.items():
        if count > max_count:
            max_word = word
            max_count = count
    print(f"Most common word: {max_word}")
    print(f"Count: {max_count}")
    return max_word
story = (
    "Once upon a time, there was a little sponge who lived in the ocean.",
    "The sponge loved to run, jump, and laugh every single day.",
    "The sponge also loved to eat crabby patty, because crabby patty was the best food.",
    "Every day, the sponge met a star and a crab, and the sponge played with the star and the crab.",
    "The crab liked money, and the star liked to be silly, but the sponge liked both the crab and the star.",
    "Sometimes the sponge said, I am a goofy goober, and the star laughed a lot.",
    "In the end, the sponge, the star, and the crab were happy friends in the ocean."
)
most_common_word(story)