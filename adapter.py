import copy

class ownError(Exception):
    def __init__(self,text):
        ownError.txt = text

class myList(list):
    pass

class adapter(object):
    def __init__(self,obj=0):
        if obj:
            try:
                self.obj=myList(obj)
            except:
                self.obj=myList()
            return
        self.obj=myList()

class stack(adapter):
    def __eq__(self,other):
        try:
            return (self.obj==other.obj)
        except:
            return False         


    def __len__(self):
        return len(self.obj)

    def __str__(self):
        return str(self.obj)

    def pop(self):
        if not len(self.obj):
            raise ownError("No elements")
        return self.obj.pop()

    def top(self):
        if not len(self.obj):
            raise ownError("No elements")
        return self.obj[-1]

    def push(self, obj):
        self.obj.append(obj)

def show(obj:stack):
    if type(obj)!=type(stack()):
        obj=stack(obj)
    obj_new=copy.deepcopy(obj)
    l=len(obj_new)
    for i in range(l):
        print(obj_new.pop(), end=' ')
    print()



a=stack([1,2,3])
a.push(1)
a.push(2)
show(a)
print(a)
