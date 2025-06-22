class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.length = len(collection)
        self.whole_pages = self.length // items_per_page
        self.partial_page = self.length % items_per_page
    
    def item_count(self):
        return self.length
​
    def page_count(self):
        return self.whole_pages + 1 if self.partial_page else self.whole_pages
    
    def page_item_count(self, page_index):
        if (self.page_count() - 1) < page_index or page_index < 0:
            return -1
        return self.items_per_page if page_index <= self.whole_pages - 1 else self.partial_page
    
    def page_index(self, item_index):
        if self.length - 1 < item_index or item_index < 0:
            return -1
        return item_index // self.items_per_page