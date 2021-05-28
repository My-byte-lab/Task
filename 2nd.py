amount=int(input("enter the number"))
count=0
if(amount>500):
  count=amount//500
  amount=amount%500
print( "The number of 500 note is", count )
if(amount>200):
  count=amount//200
  amount=amount%200
print( "The number of 200 note is", count)
if(amount>100):
  count=amount//100
  amount=amount%100
print( "The number of 100 note is", count)
if(amount>50):
  count=amount//50
  amount=amount%50
print( "The number of 50 note is", count)
if(amount>20):
  count=amount//20
  amount=amount%20
print( "The number of 20 note is", count)
if(amount>10):
  count=amount//10
  amount=amount%10
print( "The number of 10 note is", count)
if(amount>5):
  count=amount//5
  amount=amount%5
print( "The number of 5 note is", count)
