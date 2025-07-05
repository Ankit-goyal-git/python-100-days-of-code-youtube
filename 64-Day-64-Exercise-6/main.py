class lib:
    def __init__(self,):
        self.nobook=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.nobook+=1
    def rembook(self,book):
        ind=self.books.index(book)
        self.books.pop(ind)
        self.nobook-=1
    def isok(self):
        if(self.nobook==len(self.books)):
            print("yes")
        else:
            print("no")
    def info(self):
        print(f"library have {self.nobook} books:")
        for i in self.books:
            print(i)

a=lib()

a.info()

a.addbook("book1")
a.addbook("book2")
a.info()

a.isok()

a.rembook("book2")

a.isok()
a.info()


