# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    with open(filename) as file:
        content = file.read().replace("\n", "")
    return content


def count_words():
    text = read_file_content("./story.txt").replace(".", "").replace(",", "").replace("?", "")

    split_text = text.split(" ")
    while "" in split_text:
        split_text.remove("")

    word_count = {}
    for word in split_text:
        word_count[word] = split_text.count(word)

    return word_count
