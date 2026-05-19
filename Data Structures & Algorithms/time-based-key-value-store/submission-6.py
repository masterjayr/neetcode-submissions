from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timeMap:
            return ""

        values = self.timeMap.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            elif values[mid][0] > timestamp:
                r = mid - 1
        return res 