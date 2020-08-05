# ----------------------------------------------------------------------
# Takes password input of the user and returns the amount of times that
# password has been used. Number of times used is based on a database of 
# breached info.
#
# Ryley Johnson
# ----------------------------------------------------------------------

import requests
import hashlib



def request_api_data(query_char):
	"""Performs a GET request on URL to obtain status code. 

	Status code should be 200.
	"""
	url = "https://api.pwnedpasswords.com/range/" + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f"Error fetching {res.status_code}, check the API and try again.")
	return res


def get_password_leaks_count(hashes, hashes_to_check):

	hashes = (line.split(":") for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hashes_to_check:
			return count
	return 0


def pwned_api_check(password):
	"""Formats the password in the SHA-1 hash method and creates variables

	for the partial hash sent to the API.
	"""
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char) # sends partial hash to API
	return get_password_leaks_count(response,tail) # full password count

	
def main(password):
	"""Provides information about number of times the password appeared.

	Provides recommendation on whether to change password
	"""
	count = pwned_api_check(password)
	if count:
		print(f"{password} was found {count} times. You should probably change your password!")
	else:
		print(f"{password} was not found. Carry on!")
	
			
			


if __name__ == '__main__':
	"""Main program execution. Asks user for desired password lookup

	and whether the user wants to continue looking up passwords.
	"""
	while True:
		main(input("Enter password to check: "))
		x = input("Search another password? (y/n) ") 
		if x[0].lower() == 'y':
			continue
		else:	
			break