import requests
import hashlib



def request_api_data(query_char):
	# k-anonymity
	url = "https://api.pwnedpasswords.com/range/" + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f"Error fetching {res.status_code}, check the API and try again.")
	return res


def get_password_leaks_count(hashes, hashes_to_check):
	hashes = (line.split(":") for line in hashes.text)

def pwned_api_check(password):
	# check password if it exists in API response
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	print(response)
	return get_password_leaks_count(response,tail)

	
pwned_api_check('1234')

