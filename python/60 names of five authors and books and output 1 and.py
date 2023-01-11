# program to get names of five authors
# and book
book_author= {}
for i,j in book_author(2):
    author = input("Enter name of author: ")
    book_name= input("Enter book name: ")
    book_author.update({"{author}": "{book}"})
    # book_author[author] = book_name
# last_author = (list(book_author.keys()[-1]))
# last_book = (list(book_author.values()[-1]))
# print(f"Last author is{last_author} and book is {last_book}.")
print(book_author)