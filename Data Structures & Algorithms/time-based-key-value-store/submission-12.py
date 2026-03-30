class TimeMap:

    def __init__(self):
        self.dicti = dict()       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dicti:
            self.dicti[key] = [(value, timestamp)]
            return

        self.dicti[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dicti:
            return ""
        
        values = self.dicti[key]

        l = 0
        r = len(values)-1
        answer = None
        while l<=r:
            mid = l + (r-l)//2

            if values[mid][1] > timestamp:
                r = mid-1

            else: 
                answer = values[mid][0]
                l = mid+1
        
        if answer == None:
            return ""
        
        return answer