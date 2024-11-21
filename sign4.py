import hashlib

# Data yang diberikan
guid = "69890235"
left_num = 1000
name = "GARFITZY"
session = "lSRyBAyPkimrevAZw6TN1Q=="

# Langkah 1: Gabungkan data sesuai urutan tertentu, bisa juga ditambahkan pemisah jika diperlukan
data_string = f"guid={guid}left_num={left_num}name={name}session={session}"

# Langkah 2: Hitung hash MD5 dari string gabungan
sign = hashlib.md5(data_string.encode('utf-8')).hexdigest()

# Output nilai sign
print("Sign:", sign)
