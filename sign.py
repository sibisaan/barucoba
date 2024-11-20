import hashlib

# Define the data as a string (concatenating all values)
data_string = '{"op":"login","params":{"account":"garfitzyescobar@gmail.com","md5pwd":"c7f058ca599176d400f6ae5826c733d3","game_token":"AWd2qMYMpd2zWpYvbAymavlH9Y1NFki_sEQiq5BLa6dhTxGpZaTq2DP3UXz_Jhy_ToqALnEOSsA","recaptcha_token":"","country":""},"lang":"id"}'

# Calculate the MD5 hash of the data string
md5_hash = hashlib.md5(data_string.encode()).hexdigest()
md5_hash
