nama_pelanggan = input("Masukkan nama pelanggan: ")
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
daftar_barang = []
for i in range(jumlah_barang):
    print(f"\nMasukkan data untuk barang ke-{i+1}")
    print("-" * 30)
nama_barang = input("Masukkan nama barang \t: ")
harga_barang = int(input("Masukkan harga barang \t: "))
jumlah_item = int(input("Masukkan jumlah barang\t: "))
daftar_barang.append([nama_barang, harga_barang, jumlah_item])
subtotal = 0
total_diskon = 0
total_pajak = 0
print("\n" + "="*53)
print(f"{'STRUK PEMBELIAN':^53}")
print("-"*53)
print(f"Nama Pelanggan: {nama_pelanggan}")
print("-"*53)
print(f"{'Barang':<15} {'Harga':<15} {'Jumlah':<8} {'Total':^12}")
print("-"*53)
for barang in daftar_barang:
    nama, harga, jumlah = barang
    total_harga = harga * jumlah
    subtotal += total_harga
    print(f"{nama:<15} {harga:<15,} {jumlah:^8} {total_harga:<15,}")
if harga_barang >= 5000000:
    kategori = "Premium"
    total_diskon = subtotal * 0.08 # Diskon 8%
elif harga_barang >= 1000000:
    kategori = "Menengah"
    total_diskon = subtotal * 0.05 # Diskon 5%
else:
    kategori = "Ekonomis"
    total_diskon = subtotal * 0.03 # Diskon 3%
    total_pajak = (subtotal - total_diskon) * 0.05
    total_pembayaran = subtotal - total_diskon + total_pajak
print(f"Subtotal: {subtotal:>40,}")
print(f"Diskon: {total_diskon:>40,}")
print(f"Pajak: {total_pajak:>40,}")
print("-"*53)
print(f"TOTAL: {total_pembayaran:>40,}")
print("-"*53)
print("Terima kasih atas kunjungan Anda!")
print("-"*53)