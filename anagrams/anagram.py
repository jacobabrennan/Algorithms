

# = Anagram Dictionary Search =================================================
"""
When executed, this script will compile a dictionary of English words, and then
present the user with a prompt. The program will attempt to find all anagrams
for any string entered into the prompt, and then output the resulting list to
the user, along with the number of calls to search_tree used to build the list.

The project consists of two major components:
 * The dictionary building process,
 * And the searching function.

The dictionary is built from a list of English words stored in a text file. The
dictionary consists of a nested tree structure. Each node on the tree is a
Python dictionary, whose keys are a subset of the letters of the alphabet, plus
the special value PATH_WORD. Every final node also contains a key PATH_WORD,
the value of which is an English word. Thus, traversing the tree downward, one
letter at a time, will always lead to a valid English word. Non-final nodes can
also contain the key PATH_WORD; for an example, the very first node at the key
"a" contains a PATH_WORD value of "a", as this is a valid English word. Any
other language or arbitrary list of words can be specified by changing the
value of DICTIONARY_DEFAULT.

The search function operates by traversing the dictionary tree recursively. For
each unique letter in the search word, the tree node corresponding to that
letter (if any) is searched using the remaining letters. If a node is found
after all letters have been used for traversal, the PATH_WORD value on that
node is checked. If it exists, it is added to the list of words found for that
sub tree, and returned.

For a conceptual explanation of how this works, consider that strings can be
modelled as paths through a 26 dimensional grid, where each dimension
corresponds with a letter of the alphabet. A dictionary is then the set of all
such paths that correspond with valid words in a given language. A set of
letters, such as those contained in our search words, defines a surface within
that space. The set of all anagrams for any given word is thus the intersection
of the dictionary with the surface defined by that word.
"""


# - Project Constants ----------------------------
PATH_WORD = "@"
DICTIONARY_FILE_ENGLISH = 'words.txt'
DICTIONARY_DEFAULT = DICTIONARY_FILE_ENGLISH
n_count = 0


# - Dictionary Building --------------------------
def build_dictionary(file_name):
    """Constructs a tree containing single letter paths to every valid word."""
    print(F'Building Dictionary')
    print(F' - Reading File')
    with open(file_name) as word_file:
        file_string = word_file.read()
        words = file_string.split('\n')
    print(F' - Building word tree')
    dictionary = {}
    count = 0
    for word in [W.lower() for W in words]:
        count += 1
        current_path = dictionary
        for character in word:
            if(not (character in current_path)):
                sub_path = {}
                current_path[character] = sub_path
            else:
                sub_path = current_path[character]
            current_path = sub_path
        current_path[PATH_WORD] = word
    print(F' - Dictionary Constructed ({count} words)')
    return dictionary


# - Tree traversal and Searching -----------------
def letter_dimensions(word):
    """
    Constructs a dictionary where each letter present in a given word is mapped
    to the number of occurances of that letter within the word.
    """
    letters = {}
    for letter in word.lower():
        if(ord(letter) > ord('z') or ord(letter) < ord('a')):
            continue
        if(not (letter in letters)):
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters


def search_tree(letters, tree):
    """Searches a tree for paths that exhaust all supplied letters."""
    global n_count
    n_count += 1
    words = []
    # If we've reached the end of the letter path
    if(not len(letters)):
        if(PATH_WORD in tree):
            words.append(tree[PATH_WORD])
        return words
    # Add all sub-words on the tree
    for letter in letters:
        # Skip any paths that don't lead to real words
        if(not (letter in tree)):
            continue
        # Get the next portion of the tree
        sub_tree = tree[letter]
        # Subtract letter from next possible steps
        sub_letters = dict(letters)
        sub_letters[letter] -= 1
        if(not sub_letters[letter]):
            del sub_letters[letter]
        # Add all words on sub-tree, recursively
        words_on_path = search_tree(sub_letters, sub_tree)
        words.extend(words_on_path)
    # Return all anagrams
    return words


# - Public Interface -----------------------------
def anagrams(word, dictionary):
    """Finds all anagrams of a given word in a given dictionary."""
    global n_count
    n_count = 0
    letters = letter_dimensions(word)
    possible_words = search_tree(letters, dictionary)
    if(word in possible_words):
        possible_words.remove(word)
    return possible_words


# - Start User Interface -------------------------
english = build_dictionary(DICTIONARY_DEFAULT)
while(True):
    word = input('Find Anagrams for word: ')
    print('Starting Search')
    results = anagrams(word, english)
    print('')
    print(F'Results({n_count}):')
    print(results)
    print('')
