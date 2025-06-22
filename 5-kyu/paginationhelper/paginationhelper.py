class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self._item_count = len(collection)
        self._page_count = (
            self._item_count + items_per_page - 1
        ) // items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return self._page_count

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self._page_count:
            return -1
        return (
            self._item_count % self.items_per_page or self.items_per_page
            if page_index == self._page_count - 1
            else self.items_per_page
        )

    def page_index(self, item_index):
        if item_index < 0 or item_index >= self._item_count:
            return -1
        return item_index // self.items_per_page
