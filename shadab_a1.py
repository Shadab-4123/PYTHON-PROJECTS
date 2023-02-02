"""
Module for currency exchange
This module provides several string parsing functions to
implement a
simple currency exchange routine using an online currency
service.
The primary function in this module is exchange.
Author: Shadab Raza
Date: 30/11/2022
"""
def before_space(s):
	'''
	Returns a copy of s up to, but not including, the first space

	Parameter s: the string to slice
	Precondition: s is a string with at least one space

	# we are testing space and slice of string before first part of whole string
	>>> before_space("8.786 USD")
	'8.786'
	>>> before_space("25.76  INR")
	'25.76'
	>>> before_space("11.345  USD")
	'11.345'
	'''
	end_first = s.find(' ')
	first = s[:end_first].strip()
	return first

# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()

def after_space(s):
	'''
	Returns a copy of s after the first space

	Parameter s: the string to slice
	Precondition: s is a string with at least one space

	# we are testing space and slice of string after first part of whole string 
	>>> after_space("8.786 USD")
	'USD'
	>>> after_space("25.76  INR")
	'INR'
	'''
	
	end_first = s.find(' ')
	last = s[end_first+1:].strip()
	return last
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()
	

def first_inside_quotes(s):
	'''
	Returns the first substring of s between two (double) quotes
	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of
	it.

	Examples:
	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C',
	because it only picks the first such substring.

	Parameter s: a string to search
	Precondition: s is a string containing at least two double
	quotes

	# testing first double quote substring

	>>> first_inside_quotes('A "B C" D')
	'B C'

	>>> first_inside_quotes('A "GoOD" N "BYE" K')
	'GoOD'
	'''
	s1 = s.index('"')
	s2 = s.index('"',s1+1)
	string = s[s1+1:s2]
	return string
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()

def get_lhs(json):
	'''
	Returns the lhs value in the response to a currency query

	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the keyword
	"lhs".
	 For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if the JSON response
	contains an error message.

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query	
	
	# test of lhs value in json
	>>> get_lhs('{ "lhs" : "2 Namibian Dollars", "rhs" : "2 Lesotho Maloti","err" : "" }')
	'2 Namibian Dollars'

	>>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
	'1 Bitcoin'
	''' 
	start=json.index(':')
	end_first = json.find(',')
	first1 = json[start+3:end_first-1]
	return first1
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()

def get_rhs(json):
    '''
    Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the
    keyword "rhs". 
    For example, if the JSON is
    '{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
    then this function returns '19995.85429186 Euros' (not
    '"38781.518240835 Euros"').
    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    
    # test of rhs value in json.
    >>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
    '19995.85429186 Euros'
    
    >>> get_lhs('{ "lhs":"2 Namibian Dollars", "rhs":"2 Lesotho Maloti","err":"" }')
	'2 Lesotho Maloti'
	'''
    
    start=json.index(':',json.index(':')+3)
    end_second = json.index(',',json.index(',')+4)
    first2 = json[start+3:end_second-1]
    return first2    

def has_error(json):
	'''
	Returns True if the query has an error; False otherwise.

	Given a JSON response to a currency query, this returns True if
	there is an error message. 
	For example, if the JSON is
	'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True (It
	does NOT return the message 'Currency amount is invalid.').

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	
	 #checks for empty substring
	>>> has_error('{ "lhs" : "USD", "rhs" : "INR", "err" : "" }')                                         
    False   
    >>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid" }')
    True
	'''
	h1=json.index('err')
	h2=json.index('"',h1+5)
	h3=json.index('"',h2+1)
	return h3>=h2+2

def query_website(old,new,amt):
    '''
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency old to the
    currency new. The response should be a string of the form
    '{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
    where the values old-amount and new-amount contain the value
    and name for the old and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "err" will have an error message.

    Parameter old: the currency on hand
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to
    Precondition: new is a string with no spaces or non-letters
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float

    >>> query_website('USD','CUP',2.5)
    '{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'

    '''
    import requests
    json=(requests.get('http://cs1110.cs.cornell.edu/2022fa/a1?old={0}&new={1}&amt={2}'.format(old,new,amt))).text
    # print(json)     
    return json
# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()
#print(query_website('USD','INR',1.2))


def is_currency(code):
	'''
	Returns: True if code is a valid (3 letter code for a) currency
	It returns False otherwise.

	Parameter code: the currency code to verify
	Precondition: code is a string with no spaces or non-letters.
	
	# test of correct currency code.
	>>> is_currency('ugh') 
	Fasle
	>>> is_currency('USD')
	True
	'''
	return not(has_error(query_website(code,code,5.6))==True)

def exchange(old,new,amt):
	'''
	Returns the amount of currency received in the given exchange.

	In this exchange, the user is changing amt money in currency
	old to the currency new. The value returned represents the
	amount in currency new.
	The value returned has type float.

	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code

	Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code
	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	'''
	# x=get_rhs(query_website(old,new,amt))
	# print(x)
	# y=before_space(x)
	# print(before_space(get_rhs(query_website(old,new,amt))))
	return before_space(get_rhs(query_website(old,new,amt)))
