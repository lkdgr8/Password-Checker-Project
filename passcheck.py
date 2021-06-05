import requests 
import hashlib	
import sys 

def request_api_data(query_char):
   url = 'https://api.pwnedpasswords.com/range/' + query_char                        
   ok = requests.get(url)
   return ok

def get_password_leakes_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
	    if h == hash_to_check:
	    	return count
	return 0
   		

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() 
  first5char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5char)
  print(response)	
  return get_password_leakes_count(response, tail)	

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'password {password} was found {count} time. you must change your password')
		else:
			print(f'password {password} was not found. good luck!')
        	

main(sys.argv[1:])