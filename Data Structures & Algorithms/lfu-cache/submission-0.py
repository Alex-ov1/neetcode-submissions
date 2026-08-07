class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq = {}
        self.count = {}
        self.l = []

    def get(self, key: int) -> int:
        if key in self.freq:
            self.count[key] += 1

            self.l.remove(key)
            self.l = [key] + self.l[:]

            return self.freq[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.freq:
            self.count[key] += 1
            self.freq[key] = value

            self.l.remove(key)
            self.l = [key] + self.l[:]
        else:
            if len(self.l) < self.capacity:
                self.l = [key] + self.l[:]

                if key in self.freq:
                    self.count[key] += 1
                else:
                    self.count[key] = 1
                    self.freq[key] = value
            else:
                f = sorted(self.count, key=self.count.get)
                if self.count[f[0]] == self.count[f[-1]]:
                    least = self.l[-1]
                else:
                    least = f[0]

                self.l.remove(least)
                self.freq.pop(least)
                self.count.pop(least)

                self.l = [key] + self.l[:]
                self.count[key] = 1
                self.freq[key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)