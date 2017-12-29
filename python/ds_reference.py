print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist只是指向同一对象的另一名称
mylist = shoplist

# 购买了apple删除
del shoplist[0] #和在mylist中删除效果一样

print('shoplist is', shoplist)
print('my list is', mylist)
#注意打印结果
#二者指向同一对象，则会一致

print('Copy by making a full slice')
mylist = shoplist[:] #复制完整切片
#删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('my list is', mylist)
#此时已经不同