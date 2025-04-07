import lazyllm

test1 = lambda a: a + 1
test2 = lambda a: a * 4
test3 = lambda a: a / 2

with lazyllm.parallel() as prl1:
    prl1.func1 = test1
    prl1.func2 = test2
    prl1.func3 = test3

with lazyllm.parallel().asdict as prl2:
    prl2.path1 = test1
    prl2.path2 = test2
    prl2.path3 = test3

with lazyllm.parallel().astuple as prl3:
    prl3.func1 = test1
    prl3.func2 = test2
    prl3.func3 = test3

with lazyllm.parallel().aslist as prl4:
    prl4.func1 = test1
    prl4.func2 = test2
    prl4.func3 = test3

with lazyllm.parallel().join('，') as prl5:
    prl5.func1 = test1
    prl5.func2 = test2
    prl5.func3 = test3

print("默认输出：prl1(1) -> ", prl1(1), type(prl1(1)))
print("输出字典：prl2(1) -> ", prl2(1), type(prl2(1)))
print("输出元组：prl3(1) -> ", prl3(1), type(prl3(1)))
print("输出列表：prl4(1) -> ", prl4(1), type(prl4(1)))
print("输出字符串：prl5(1) -> ", prl5(1), type(prl5(1)))