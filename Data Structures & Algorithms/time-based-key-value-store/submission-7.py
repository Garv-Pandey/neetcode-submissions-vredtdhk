class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key] = self.timeMap.get(key, [])
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap.get(key, [])
        if len(arr) == 0:
            return ""
       
        l = 0
        r = len(arr) -1
        result = ""
        while l <= r:
            print(l,r)
            mid = l + (r-l)//2
            
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            
            elif arr[mid][0] > timestamp:
                r = mid-1

            else:
                
                result = arr[mid][1]

                l = mid+1

        return result