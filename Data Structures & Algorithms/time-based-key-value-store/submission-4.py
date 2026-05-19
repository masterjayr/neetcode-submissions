from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        #{"alice": [[1, "happy"], [3, "sad"]]}
        values = self.hashMap.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:

            mid = (l + r) // 2

            if timestamp >= values[mid][0]:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
