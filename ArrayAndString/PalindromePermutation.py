class PalindromePermutation:
    def __init__(self, data):
        self.data=data
    def check_is_a_permutation_of_a_palindrom(self):
        time=self.data.replace(" ", "") #O(N)
        print(time)
        j=len(time)-1
        for i in range(0, len(time), 1): #O(N)
            if time[i] != time[j]:
                return False
            j-=1
        return True
if __name__=="__main__":
    x=PalindromePermutation("atco cta")
    print(x.check_is_a_permutation_of_a_palindrom())