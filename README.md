Created a secure password checker which allows the user to search his/her passwords and see how many times their password showed up within the breached information. This program uses the SHA-1 hashing method and only sends a partial code to the website. Once the API returns all of the hashed codes (using the partial code as a 'match' critieria), the program then matches our remaining hash to the full password received. By only sending a partial hash to the API, it is impossible for an individual to intercept the code and translate our password. 

The program's final output shows the amount of times the password has been used as well as a recommendation on whether or not to change the password. 

Download the 'checkmypass.py' file and give it a try!
