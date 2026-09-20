class OneAway:
    def __init__(self, data1, data2):
        self.data1=data1
        self.data2=data2

    def check(self):
        # all the check operation are in place no more extra space needed
        if abs( len(self.data1) - len(self.data2) ) > 1: #cloud be 0 or 1
            print("first check failed")
            return False
        
        if len(self.data1) == len(self.data2):# can be a replcae only
            replace=0
            for i in range(0, len(self.data1), 1): # O(N) in time
                if self.data1[i] != self.data2[i]:
                    replace+=1
                    if replace >1:
                        return False
                
            return True
        # [pale] [ple] or [ale]
        elif len(self.data1)>len(self.data2): #replace is no possible, only remove or add 
            j=0
            count=0

            for i in range(0, len(self.data2), 1): #O(N) in time
                if self.data1[i] != self.data2[j]:
                    count+=1
                    if count > 1:
                        return False
                else:
                    j+=1

            return True
        else:
            j=0
            count=0

            for i in range(0, len(self.data1), 1): #O(N) in time
                if self.data1[i] != self.data2[j]:
                    count+=1
                    if count > 1:
                        return False
                else:
                    j+=1
            return True


if __name__=="__main__":
    x=OneAway("pale", "bake")
    print(x.check())