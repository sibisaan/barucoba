import hashlib
import json

# Fungsi untuk membuat sign
def generate_sign(guid, game_token, op, country):
    # Gabungkan parameter sebagai string (sesuai aturan sistem, jika diketahui)
    raw_data = f"{guid}{game_token}{op}{country}"
    # Hash menggunakan MD5
    sign = hashlib.md5(raw_data.encode()).hexdigest()
    return sign

# Parameter yang digunakan
guid = "84984384"
game_token = "Ackhm09dYxqYDFWyeI8KfWB4YDcndrqlN8VD5YDn_EffcesNQ8Ua7Yta0WFjRmnCF43lMS5ogc_rC0XJ3t-LsvsGzi6qCuRr"
op = "email_rebind_email_code"
country = ""

# Generate sign
sign = generate_sign(guid, game_token, op, country)
print("Generated Sign:", sign)

# Body request dengan sign yang dihasilkan
data = {
    "op": op,
    "sign": sign,
    "params": {
        "email": "",
        "guid": guid,
        "game_token": game_token,
        "country": country
    },
    "lang": "id"
}

# Print request body
print("Request Body:", json.dumps(data, indent=4))
