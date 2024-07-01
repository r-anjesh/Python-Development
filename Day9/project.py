from art import logo
print(logo,"\n\n")

print("Welcome to secret auction program")
auction = {}
name = input("What is your name? : ")
bid = int(input("What's Your bid? : $"))
auction[name] = bid
bidder = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

def max_bids(auction):
    max_bid = 0
    for bids in auction:
        if auction[bids] > max_bid:
            max_bid = auction[bids]
            bidder_name = bids
    
    print(f'{bidder_name} has the maximum bid of {max_bid} congrajulations to him/her')

while bidder == "yes":
    
    name = input("What is your name? : ")
    bid = int(input("What's Your bid? $: "))

    auction[name] = bid

    bidder = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

max_bids(auction)