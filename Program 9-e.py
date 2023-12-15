class publisher:
    def __init__(self,name):
        self.name=name
class book:
    def __init__(self,name,title,author):
        publisher.__init__(self,name)
        self.title=title
        self.author=author
class python:
    def __init__(self,name,title,author,price,no_of_pages):
        book.__init__(self,name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Publisher:",self.name)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print("Bo.of Pages:",self.no_of_pages)
book1=python("Franklin","Python Programming","John M.Zelle",1200,560)
book1.display()
