import pytest
from mazeDFS import Maze



@pytest.mark.parametrize("file,Goal",[('maze1.txt',(0,5)),
                        ('maze2.txt',(8,13)),('maze3.txt',(2,1)),
                        ('maze4.txt',(2,18)),('maze5.txt',(4,23))])
def test_method1(file,Goal):
    m = Maze(file)
    m.solve()
    assert m.goal == Goal
    

@pytest.mark.parametrize("file,numExpLored,",[('maze1.txt',11),
                          ('maze2.txt',194),('maze3.txt',17),
                          ('maze4.txt',49),('maze5.txt',90)])
def test_method2(file,numExpLored):
    m = Maze(file)
    m.solve()
    assert m.num_explored == numExpLored
