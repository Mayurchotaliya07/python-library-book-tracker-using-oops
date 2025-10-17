class Book:
    Total_books = 0

    def __init__(self,title,author,copies):
        self.title = title
        self.author = author
        self.copies = copies
        Book.Total_books += 1

    @property
    def copies(self):
        return self._copies
    
    @copies.setter
    def copies(self,value):
        if value < 0:
            raise ValueError("copies must be greater than 0")
        self._copies = value

    def borrow(self, value):
        if value < 0:
            raise ValueError("value should be in positive")
        elif self.copies < value:
            raise ValueError("Don't have that much copies")
        self.copies -= value
        print("you succesfully withdraw a copie")

    def return_book(self, value):
        if value < 0:
            raise ValueError("you can't deposite copies in minus")
        self.copies += value
        print("you succesfully deposit a copie")

    @classmethod
    def get_total_books(cls):
        return cls.Total_books
    
    @classmethod
    def show_total_books(cls):
        print(f" Total {cls.Total_books} books are created")

    @staticmethod
    def library_hours():
        print("Library is open 9am - 5pm")

    


    
