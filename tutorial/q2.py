# Q2-1
# yearから閏年を判定するプログラム

year = 1900

if year%400 == 0:
  print("閏年です")
elif year%100 == 0:
  print("平年です")
elif year%4 == 0:
  print("閏年です")
else:
  print("平年です")


# Q2-2
# FizzBuzz問題
for i in range(1, 101):
  if i%15 == 0:
    print("FizzBuzz")
    continue
  elif i%3 == 0:
    print("Fizz")
    continue
  elif i%5 == 0:
    print("Buzz")
  else:
    print(i)


