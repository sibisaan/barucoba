import requests

# URL API
url = "https://accountmtapi.mobilelegends.com/"

# Header permintaan
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "251",
    "Content-Type": "application/json",
    "Host": "accountmtapi.mobilelegends.com",
    "Origin": "https://mtacc.mobilelegends.com",
    "Referer": "https://mtacc.mobilelegends.com/",
    "sec-ch-ua": '"Chromium";v="130", "Android WebView";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; 220333QAG Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.107 Mobile Safari/537.36",
    "X-Requested-With": "com.mobile.legends",
}

# Body permintaan
data = {
    "op": "email_rebind_email_code",
    "sign": "8b647ae17d5123ed7f6d28eece951804",
    "params": {
        "email": "",
        "guid": "84984384",
        "game_token": "Ackhm09dYxqYDFWyeI8KfWB4YDcndrqlN8VD5YDn_EffcesNQ8Ua7Yta0WFjRmnCF43lMS5ogc_rC0XJ3t-LsvsGzi6qCuRr",
        "country": ""
    },
    "lang": "id"
}

# Melakukan permintaan POST
response = requests.post(url, headers=headers, json=data)

# Menampilkan hasil respons
print("Status Code:", response.status_code)
print("Response Body:", response.text)
