import shadab_a1

old=input('enter original currency:').upper()
new=input('enter desired currency:').upper()
amt=input('enter original amount:')

# DO NOT modify the following code
# if the source currency is not valid, quit
if(not(shadab_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
# if the target currency is not valid, quit
if(not(shadab_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()
print('You can exchange {0} {1} for {2} {3}'.format(amt,old,shadab_a1.exchange(old,new,amt),new))