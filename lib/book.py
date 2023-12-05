#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def get_book(self):
        return self._page_count

    def set_book(self, new_count):
        if type(new_count) != int:
            print("page_count must be an integer")
        else:
            self._page_count = new_count

    page_count = property(get_book, set_book,)    
        

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")