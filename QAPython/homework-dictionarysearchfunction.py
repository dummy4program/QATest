import re

def titlecase(t): #this is to replace the use of .title because of 'S errors in "The Handmaid's Tale" title
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),
        t)

books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}

def search(searchtitle):
  #print(searchtitle) #debugging
  for author, titles in books.items():
    #print(author) #debugging
    #print(titles) #debugging
    for title in titles:
      #print(title) #debugging
      if str(title) == searchtitle:
        return f"{author} wrote {title}."
  else:
    return "Book not found"
print(search(titlecase(str(input("Enter the book title to search for: ")))))
