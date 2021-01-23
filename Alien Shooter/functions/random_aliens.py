import random

def random_aliens(n):
    lst=[]
    for i in range(n):
        lst.append([random.randrange(100,700,30),random.randrange(100,150)])
    return lst

if __name__=="__main__":
    x=random_aliens(8)
    print(x)
