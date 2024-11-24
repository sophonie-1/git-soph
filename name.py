class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
    
    def calculate_age(self):
        current_year = 2022
        return current_year - self.year
    
    def is_old(self):
        return self.calculate_age() > 50
    
    def update_author(self, new_author):
        self.author = new_author
        print(f"Author updated to {new_author}")
    
    def add_genre(self, genre):
        self.genre = genre
        print(f"Genre added: {genre}")
    
    def remove_genre(self):
        self.genre = None
        print("Genre removed")
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}"


# Example usage
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book1.display_info()
print(f"Age: {book1.calculate_age()}")
print(f"Is old: {book1.is_old()}")

book1.update_author("Harper Lee (Jane Austen)")