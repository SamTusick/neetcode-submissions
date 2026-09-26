class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_val = float('inf')
        self.min_track = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if len(self.min_track) == 0:
            self.min_track.append(val)
            self.min_val = val
        else:
            self.min_val = min(val, self.min_track[len(self.min_track) - 1])
            self.min_track.append(self.min_val)

    def pop(self) -> None:
        self.min_track.pop()        
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]
        
    def getMin(self) -> int:
        return self.min_track[len(self.min_track) - 1]