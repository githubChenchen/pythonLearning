set1={1,2,3,4,4,3,2,1}  #通过赋值语句创建集合 去重 1,2,3,4
set2=set([1,2,3,4,4]) #set创建可变集合
set3=frozenset([1,2,3,4,4,3,21,1]) #frozenset创建不可变集合

set1.add(10)  #add向集合中添加元素，只能添加一个元素
set1.update(1,6,7,8) #update向集合中添加多个元素

set1.remove(4) #删除集合元素4
set1.discard(3) #用法与remove一致，集合元素不存在不会报错，remove会报错
set1.pop() #随机删除一个元素
set1.clear() #清空所有元素


