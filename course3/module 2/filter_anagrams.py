def filter_anagrams(word, words):

    word_lower = word.lower()
    word_count = {char: word_lower.count(char) for char in word_lower if char.isalpha()}


    anagrams = [w for w in words if len(w) == len(word) and w != word and
                {char: w.lower().count(char) for char in w.lower() if char.isalpha()} == word_count]

    return anagrams
