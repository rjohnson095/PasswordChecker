import requests
import hashlib



def request_api_data(query_char):
	# k-anonymity
	url = "https://api.pwnedpasswords.com/range/" + query_char

	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f"Error fetching {res.status_code}, check the API and try again.")
		return res 
	print(res)


def read_res(response):
	print(response.text)

def pwned_api_check(password):
	# check password if it exists in API response
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	return read_res(response)

pwned_api_check('12345')

