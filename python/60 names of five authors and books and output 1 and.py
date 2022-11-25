# program to get names of five authors
# and book
book_author= {}
for i in range(2):
    author = input("Enter name of author: ")
    book_name= input("Enter book name: ")
    book_author[author] = book_name
last_author = (list(book_author.keys()[-1]))
last_book = (list(book_author.values()[-1]))
print(f"Last author is{last_author} and book is {last_book}.")