class book:
    def __init__(self,book_id,title):
        self.book_id=book_id
        self.title,members=[]

    def  add_book(self,book):
        self.books.append(book)
        print(f"book'{book.title}'added.")

    def  register_member(self,member):
        self.members.append(member)
        print(f"member'{member.name}' registered.")

    def issue_book(self,book_id,member):
        for book in self .books:
            if book.book_id==book_id:
                if book.available:
                    book.available==False
                    print(f"'{book.titlie}' issused to {member.name}")
                else:
                    print("book is not available.")
                return
            print("book not found.")

    def return_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id : 

                book,available=True
                print(f"'{book.title}'return succesfully.")
                return
        library=library()
        book1=book(101,"python programming")
        member1=Member(1,"Arun")

        library.add_book(book1)
        library.register_member(member1)
        library.issue_book(101.member1)
        library.return_book(101)