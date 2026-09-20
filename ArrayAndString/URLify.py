class URLify:
    def __init__(self, data):
        self.data=data
    def URLify_converter(self): #it is not in place we need an additional space
        time=[]

        for i in range(0, len(self.data), 1): #O(N)

            if self.data[i]==" ":
                time+=["%20"]
            else:
                time+=[ self.data[i] ]
        self.data="".join(time)
        return len(self.data), self.data #O(N)
    
if __name__=="__main__":
    x=URLify("hello how are you man")

    s, data=x.URLify_converter()

    print(s)
    print(data)