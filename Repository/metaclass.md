# metaclass



不多bb，先上代码
```
#!/usr/bin/env python3


class TestMetaClass(type):

    def __new__(cls, name, bases, attr):

        change_attr = {}
        for x in attr:
            if not x.startswith('__'):
                change_attr[x.upper()] = attr[x]
            else:
                change_attr[x] = attr[x]
        return super().__new__(cls, name, bases, change_attr)


class TestClass(object, metaclass=TestMetaClass):

    author = 'Crush'


if __name__ == '__main__':

    print(dir(TestClass))

// ['AUTHOR', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
通过控制台的print，可以看出明明是小写的author变成了大写的AUTHOR，这点可以说明，是\_\_new\_\_ 方法中的代码起了作用，将所有内置属性意外的属性全变成了大写，所以根据现阶段对于元类的理解，元类是通过在生成类的过程中，改变类的一些行为模式，相当于`类工厂`，对于用户创建的类，做一些私人化的定制
