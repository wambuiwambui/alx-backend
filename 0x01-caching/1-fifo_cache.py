#!/usr/bin/python3
"""
FIFOCache module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFOCache class
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    return
                print("DISCARD: {}".format(self.queue[0]))
                del self.cache_data[self.queue[0]]
                self.queue.pop(0)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None