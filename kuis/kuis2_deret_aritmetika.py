print("Deret Aritmetika")

# 1. Baca a dan d
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# 2. Baca n dan lakukan validasi berulang jika n <= 0
n = int(input("Banyak suku n: "))
while n <= 0:
    print("n harus positif.")
    n = int(input("Banyak suku n: "))

# 3. Set total = 0
total = 0

# 4. Ulangi i dari 0 sampai n - 1
for i in range(n):
    # 5. Hitung suku = a + i * d
    suku = a + i * d
    # 6. Tambahkan suku ke total dan tampilkan suku
    total += suku
    print(f"Suku ke-{i+1}: {suku}")

# 7. Setelah loop selesai, tampilkan total
print(f"Jumlah deret = {total:.2f}")
