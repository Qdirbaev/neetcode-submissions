class MyStack:

    def __init__(self):
        self.q1 = [] #  out <- a, b, c  <- in
        self.q2 = [] #

    def push(self, x: int) -> None:
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.pop(0))
        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:
        return self.q2.pop(0)

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        print(self.q2)
        return self.q2 == []

