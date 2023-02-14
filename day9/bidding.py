bids={}

#print(bids)
def find_highest_bidder(bid_record):
  highest_bid=0
  for bidder in bid_record:
    bid_amt=int(bid_record[bidder])
    if bid_amt>highest_bid:
      highest_bid=bid_amt
      winner=bidder
  print(f"Congrats {winner}, you won the item with bid of {highest_bid}")
extra_bidders=True
while extra_bidders:
  name=input("Enter your name:")
  price=input("Enter your bid:")
  bids[name]=price
  repeat=input("Are there any more bidders? If yes, say 'y' else say 'n':")
  if(repeat=='n'):
    extra_bidders=False
find_highest_bidder(bids)
    
