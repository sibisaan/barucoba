import hashlib

# Data input
op = "login"
account = "garfitzyescobar@gmail.com"
md5pwd = "c7f058ca599176d400f6ae5826c733d3"
game_token = "AWd2qMYMpd2zWpYvbAymavlH9Y1NFki_sEQiq5BLa6dhTxGpZaTq2DP3UXz_Jhy_ToqALnEOSsA"

# Gabungkan parameter dalam urutan yang benar
data_to_sign = f"{op}{account}{md5pwd}{game_token}"

# Menghitung MD5 dari gabungan data
sign_hash = hashlib.md5(data_to_sign.encode('utf-8')).hexdigest()

# Menampilkan hasil sign (MD5 hash)
print("MD5 Sign:", sign_hash)
