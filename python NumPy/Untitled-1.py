import numpy as np 


number = np.array([12, 18, 15, 20, 14, 16, 10, 19, 17, 13, 20, 15, 18, 14, 16])

#reshape 
x =number.reshape(3,5)
print(x)

#min
minn = number.mean()
print(minn)


#max

print(number.max())

#min
print(number.min())


# sum
mm = number.sum()
print(mm)


#flatten

bb =number.flatten()
print(bb)


#reshap 

k =number.reshape(5,3)
print(x)

# 
num =np.argmax(k)
print(num)


mn =np.argmin(k)
print(mn)


ekta =np.unique(k)
print(ekta)


mingin =k.mean()
if mingin >= 15:
  print("کلاس عملکرد خوبی داشته")
else:
  print("نیاز به تلاش بیشتری هست")