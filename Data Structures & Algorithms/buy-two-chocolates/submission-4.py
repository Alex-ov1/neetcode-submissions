class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        l = []
        for i in range(2):
            l.append(prices[i])
        res = sum(l)

        if res > money:
            return money
        return money - res