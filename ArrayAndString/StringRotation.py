class StringRotation:
    def __init__(self, data1, data2):
        self.data1=data1
        self.data2=data2
    def check(self):
        #wat erbottlewat erbottle
        if len(self.data2)!= len(self.data1):
            return False
        
        concatenation=self.data1+self.data1
        try:
            start=concatenation.index(self.data2)
        except ValueError:
            print("it is not present")
            return False
        time=""
        for i in range(0,start, 1):
            time+=concatenation[i]
        for i in range(start+len(self.data2), len(concatenation), 1):
            time+=concatenation[i]
        
        return time== self.data1
    

 # s1 "waterbottle" and s2 "erbottlewat", is s2 a rotation of s1?
if __name__=="__main__":
    x=StringRotation( "erbottlewat","waterbottle")
    print(x.check())