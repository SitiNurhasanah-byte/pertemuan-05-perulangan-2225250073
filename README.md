# Pertemuan 05 Perulangan Python
Nama: Siti Nurhasanah  
NIM: 2225250073  
Kelas: 3B  

---

## 🎯 Tujuan
Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif.

---

## 🚀 Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

---

## 📂 Algoritma Kuis 2
1. Baca suku pertama `a` dan beda `d`.  
2. Baca banyak suku `n`. Jika `n <= 0`, minta ulang sampai valid.  
3. Set `total = 0`.  
4. Ulangi `i` dari 0 sampai `n-1`.  
5. Hitung suku ke-`i` dengan rumus `a + i * d`.  
6. Tambahkan suku ke `total` dan tampilkan nilai suku.  
7. Setelah loop selesai, tampilkan jumlah akhir dengan format dua angka di belakang koma.  

---

## 📊 Hasil Pengujian

### Latihan 1 – Tabel Perkalian
| Input | Output Aktual | Status |
|-------|---------------|--------|
| n = 4 | 10 baris: 4×1 … 4×10 | ✅ |
| n = -3 | 10 baris: -3×1 … -3×10 | ✅ |

### Latihan 2 – Jumlah 1 sampai n
| Input | Output Aktual | Status |
|-------|---------------|--------|
| n = 1 | Jumlah = 1 | ✅ |
| n = 5 | Jumlah = 15 | ✅ |
| n = 10 | Jumlah = 55 | ✅ |

### Latihan 3 – Validasi Input
| Input Berurutan | Output Aktual | Status |
|-----------------|---------------|--------|
| 120, -5, 75 | Menolak 120 & -5, menerima 75 | ✅ |

### Latihan 4 – Hitung Bilangan Genap
| Input | Output Aktual | Status |
|-------|---------------|--------|
| n = 1 | Banyak bilangan genap = 0 | ✅ |
| n = 5 | Banyak bilangan genap = 2 | ✅ |
| n = 10 | Banyak bilangan genap = 5 | ✅ |

### Kuis 2 – Deret Aritmetika
| a   | d   | n | Suku yang Dihasilkan       | Jumlah | Status |
|-----|-----|---|----------------------------|--------|--------|
| 2   | 3   | 5 | 2, 5, 8, 11, 14            | 40.00  | ✅ |
| 10  | -2  | 4 | 10, 8, 6, 4                | 28.00  | ✅ |
| 1.5 | 0.5 | 3 | 1.5, 2.0, 2.5              | 6.00   | ✅ |

---

## 🪞 Refleksi
Kesalahan perulangan yang pernah ditemukan adalah **lupa menuliskan batas loop dengan benar**.  
Contoh: menggunakan `range(n)` tetapi salah menafsirkan bahwa akan menghasilkan sampai `n` (padahal hanya sampai `n-1`).  
Perbaikan dilakukan dengan menyesuaikan logika perulangan:  
- Jika ingin mencetak 10 baris, gunakan `range(1, 11)`.  
- Jika ingin menghasilkan `n` suku, gunakan `range(n)` dengan indeks mulai dari 0.  

Dengan perbaikan ini, jumlah iterasi sesuai kebutuhan dan hasil program konsisten dengan spesifikasi.
