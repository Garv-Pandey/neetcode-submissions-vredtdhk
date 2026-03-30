class TimeMap:

    def __init__(self):
        self.d = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key] = self.d.get(key, [])
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        self.d[key] = self.d.get(key, None)
        if self.d[key] == None:
            return ""
        
        arr = self.d[key]
        l = 0
        r = len(arr) -1
        answer = ""
        while l <=r:
            mid = l + (r-l)//2

            if arr[mid][1]> timestamp:
                r = mid-1

            else:
                answer = arr[mid][0]
                l = mid+1

        return answer