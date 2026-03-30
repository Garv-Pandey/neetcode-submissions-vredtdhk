class TimeMap:
    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.time_map:
            key_value = self.time_map[key]
            key_value.append((value, timestamp))
            return

        self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        key_value = self.time_map[key]

        ans = key_value[0]
        l = 0
        r = len(key_value) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if key_value[mid][1] == timestamp:
                return key_value[mid][0]

            elif key_value[mid][1] < timestamp:
                ans = key_value[mid] if key_value[mid][1] > ans[1] else ans
                l = mid + 1

            else:
                r = mid - 1

        return ans[0] if ans[1] <= timestamp else ""
