class StringCompression:
    def __init__(self, data):
        self.data=data

    def compress(self):
        container={} #space needed 
        
        for x in self.data: #O(N)
            if x in container:
                value=container.get(x)
                value+=1
                container.update({x:value})
            else:
                container.update({x:1})
        ok=False
        print(container)
        time=[]
        for x in container.keys(): #O(N)
            if container.get(x)>1 and ok == False:
                ok=True

            time+=[""+x+str(container.get(x))]
        
        if ok == False:
            return self.data
        else:
            return "".join(time)
        
if __name__=="__main__":

    x=StringCompression("aaabcssssssssssssssssssss")

    print(x.compress())