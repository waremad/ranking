from ranking import *
import random

def test_two_ch():
    assert two_ch([0],1) == 0
    assert two_ch([0],2) == 0
    assert two_ch([1,0,1],4) == 10
    assert two_ch([1,0,1,0],4) == 10

def test_max_two():
    assert max_two([1]) == 1
    assert max_two([0,0,0]) == 2
    assert max_two([0,1,2,3,4,5,6,7,8,9]) == 4

def test_randomls():
    ls = [0,1,2,3,4,5,6,7,8,9]
    outls = randomls(ls)
    for i in outls:
        ls.remove(i)
    assert ls == []

"""
def test_add_ls():
    assert add_ls(0,[]) == [0]
    assert add_ls(1,[0]) == [0,1]
    assert add_ls(0,[1]) == [0,1]
    assert add_ls(0,[0,2,4,6,8]) == [0,0,2,4,6,8]
    assert add_ls(1,[0,2,4,6,8]) == [0,1,2,4,6,8]
    assert add_ls(3,[0,2,4,6,8]) == [0,2,3,4,6,8]
    assert add_ls(7,[0,2,4,6,8]) == [0,2,4,6,7,8]
    assert add_ls(9,[0,2,4,6,8]) == [0,2,4,6,8,9]
"""

def test_txt2ls():
    assert txt2ls("test.txt") == ["1","ni","3san!"]

"""
ls = []
for i in range(10):
    ls.append(random.randint(0,99))
out = []
print(ls)
for i in ls:
    out = add_ls(i,out)
    print(out)
"""