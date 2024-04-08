def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    num_words=count_words(text)
    word_counts={}
    word_counts=count_nums(text)
    print(f"{num_words} words found in this book")
    print(word_counts)
    sorted_count=dict(sorted(word_counts.items()))
    print (sorted_count)


def get_book(path):
    with open(path) as f:
        return f.read()

def count_nums(text):
    word_count ={}
    lowered_string = text.lower()
    for char in lowered_string:
        l = char.lower()
        if char.isalpha():
            if char in word_count:
                word_count[l] +=1
            else:
                word_count[l] = 1
    return word_count



     
def count_words(text):
      words =text.split()
      return len(words)

main()
