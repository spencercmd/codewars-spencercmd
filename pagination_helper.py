import math

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection #list of items
        self.items_per_page = items_per_page #max items per page
    
    def item_count(self):
        # return total number of items in collection
        return len(self.collection)
    
    def page_count(self):
        # return total number of pages
        return math.ceil(len(self.collection) / self.items_per_page)
    def page_item_count(self, page_index):
        # return number of items on the given page index
        if page_index < 0 or page_index >= self.page_count():
            return -1 #invalid page index
        #if its the last page, return the remaining items.
        if page_index == self.page_count() - 1:
            return len(self.collection) % self.items_per_page or self.items_per_page
        return self.items_per_page # full page
    def page_index(self, item_index):
        # return the page number that contains the item index
        if item_index < 0 or item_index >= len(self.collection):
            return -1 #invalid item index
        return item_index // self.items_per_page #integer division
    
# math.ceil() is used to round up to the nearest whole number.
# item_count() returns the length of the collection.
# page_count() uses math.ceil() to determine how many full pages are needed.
# page_item_count(page_index) handles out of bounds cases by returning -1
# if its the last page, it returns the remainder of items using modulo
# otherwise, it returns the standard items_per_page.

# page_index(item_index) handles oob by returning -1
# uses integer division to find the page number.


# diving into the python syntax used here:
# class PaginationHelper: defines a new class
# a class here is a blueprint for creating objects.

# __init__ method constructor
# self refers to the instance of the class (the object being created)
# collection is a list of items (like 'a','b','c')
# items_per_page is the number of items allowed per page.

# item_count() method
# defines a method inside a class
# returns the length of the collection (number of items).

# import math imports python's math module.
# page_count() method uses math.ceil() to round up to the nearest whole number.
# len(self.collection) / self.items_per_page returns the number of items in the collection divided by the number of items per page.
# math.ceil() ensures partial pages still count.

# page_item_count(page_index) method
# conditional check, if the page number is negative, return -1
# if the page number does not exist, return -1

# self.page_count() - 1 returns the last page number
# len(self.collection) % self.items_per_page returns the remainder of items
# or self.items_per_page returns the standard number of items per page.
# if not the last page, return full page size.

# page_index(item_index) method
# checks if item is out of range 
# // integer division, returns the whole number part of division operation
# this tellsus which page the item belongs to.

