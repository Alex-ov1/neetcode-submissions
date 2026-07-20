class LRUCache:
    def __init__(self, capacity: int):
        assert type(capacity) == int, "la valer doit être un entier"
        self.capacity = capacity
        self.freq = {}
        self.l = []

    def get(self, key: int) -> int:
        if key in self.freq:
            self.l.remove(key)
            self.l.append(key)

            return self.freq[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.freq:
            self.freq[key] = value

            self.l.remove(key)
            self.l.append(key)
        else:
            if len(self.l) == self.capacity:
                ancien = self.l.pop(0)
                self.freq.pop(ancien)
            
            self.l.append(key)
            self.freq[key] = value
