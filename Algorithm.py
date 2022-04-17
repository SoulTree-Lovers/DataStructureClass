class Count:
    def __init__(self):
        self.count = 0

    def sample(self, list_A, n):
        if n == 1:
            return 1
        sum = 0
        for i in range(n):
            sum += list_A[i]
            self.count += 1

        tmp = sum + self.sample(list_A, n-1)
        self.count += 1

        print("count:", self.count)
        return tmp

list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_B = list_A * 10


a = Count()

print(a.sample(list_B, 100))


# 시간 복잡도 : O(n**2)