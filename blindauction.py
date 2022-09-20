from replit import clear
from art import logo
print(logo)
bids={}
name= input("What is your name?\n")
price= int(input("What is your bid?\n"))
bids[name]=price
x= input("Are there any other users who want to bid? yes or no\n")
while x=="yes":
  clear()
  name= input("What is your name?\n")
  price= int(input("What is your bid?\n"))
  bids[name]=price
  x= input("Are there any other users who want to bid? yes or no\n")
if x=="no":
  highest_bid=0
  for bid in bids:
    if bids[bid]>highest_bid:
      highest_bid=bids[bid]
      print(highest_bid)
