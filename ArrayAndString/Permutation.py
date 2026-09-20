class Permutation:
    def __init__(self, data1, data2):
        self.data1=data1
        self.data2=data2
    def check_permutation(self):
        if len(self.data1) != len(self.data2):
            return False
        for i in range(0, len(self.data1), 1): # O(N) in complexity and in place no more memory used
            if self.data1[i]!=self.data2[i]:
                return False
        return True

if __name__== "__main__":
    x=Permutation("ana", "anx")
    print(x.check_permutation())
        