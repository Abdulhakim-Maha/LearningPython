bidders = [int(i) for i in input('Enter All Bid : ').split()]
bidders.sort()
if len(bidders) == 1:
	print('not enough bidder')
elif bidders.count(bidders[-1]) > 1:
	print('error : have more than one highest bid')
else:
	print('winner bid is {} need to pay {}'.format(bidders[-1], bidders[-2]))