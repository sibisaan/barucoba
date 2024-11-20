import hashlib
import json

# Data input sebagai dictionary
data = {
    "op": "login",
    "params": {
        "account": "garfitzyescobar@gmail.com",
        "md5pwd": "c7f058ca599176d400f6ae5826c733d3",
        "game_token": "AWd2qMYMpd2zWpYvbAymavlH9Y1NFki_sEQiq5BLa6dhTxGpZaTq2DP3UXz_Jhy_ToqALnEOSsA",
        "recaptcha_token": "",
        "country": ""
    },
    "lang": "id"
}

# Menyiapkan data untuk dihitung MD5-nya
params_str = json.dumps(data["params"], separators=(',', ':'))  # Menggabungkan params ke dalam format JSON tanpa spasi ekstra
sign_data = f'{data["op"]}{params_str}{data["lang"]}'

# Menghitung MD5 dari gabungan data
sign_hash = hashlib.md5(sign_data.encode('utf-8')).hexdigest()

# Menampilkan hasil sign (MD5 hash)
print("MD5 Sign:", sign_hash)
