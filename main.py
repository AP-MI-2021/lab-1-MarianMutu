'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    for i in range(n-1,2):
        if n%i==0:
             return False
        return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    p=1
    for x in lst:
      p=p*lst(x)
    return p
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x

    return x
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''

def get_cmmdc_v2(x, y):
    d=x+y
    while d>0:
        if x%d==0 and y%d==0:
            return d
        d-=1
    return 1


def main():

    is_prime(78)
    get_product(4)
    get_cmmdc_v1(2,6)
    get_cmmdc_v2(9,27)


if __name__ == '__main__':
    main()
