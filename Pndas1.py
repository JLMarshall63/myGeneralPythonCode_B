import pandas
df1 = pandas.DataFrame([[23, 54, 76],[43, 765, 98]])
df2 = pandas.DataFrame([[23, 54, 76],[43, 765, 98]], columns=["Num A","Num B","Num C"])
df3 = pandas.DataFrame([[23, 54, 76],[43, 765, 98]], columns=["Num A","Num B","Num C"], index=["1st","2nd"])
df4 = pandas.DataFrame([{"FirstName":"Bob", "Surname":"Jackson"},{"FirstName":"Marge","Surname":"Singleton"}])
df5 = pandas.DataFrame([[23, 54, 76],[43, 765, 98]], columns=["Price","Age","Value"], index=["1st","2nd"])
print df1
print df1.mean()
print df2
print df2.mean()
print df3
print df3.mean()
print df4
print df5
print df5.Price
print df5.Price.mean()
print df5.Price.max()
print df5.Price.min()

print df5.Age
print df5.Age.mean()
print df5.Age.max()
print df5.Age.min()

print df5.Value
print df5.Value.mean()
print df5.Value.max()
print df5.Value.min()