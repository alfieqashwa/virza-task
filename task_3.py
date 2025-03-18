from prettytable import PrettyTable

def hitung_diskon(subtotal):
    """Menghitung diskon berdasarkan subtotal pembelian"""
    if subtotal >= 5_000_000:
        return subtotal * 0.08, "Premium"    # Diskon 8%
    if subtotal >= 1_000_000:
        return subtotal * 0.05, "Menengah"   # Diskon 5%
    return subtotal * 0.03, "Ekonomis"       # Diskon 3%

def main():
    # Print header
    print("\n" + "="*53)
    print(f"{'PROGRAM KASIR TOKO':^53}")
    print("-"*53)

    # Input data pelanggan
    nama_pelanggan = input("Masukkan Nama Pelanggan \t: ")
    
    # Input jumlah barang
    while True:
        try:
            jumlah_barang = int(input("Masukkan Jumlah Barang \t: "))
            if jumlah_barang > 0:
                break
            print("Error: Jumlah barang harus lebih dari 0")
        except ValueError:
            print("Error: Masukkan angka yang valid")

    # Input data barang
    daftar_barang = []
    subtotal = 0

    for i in range(jumlah_barang):
        print(f"\nData Barang ke-{i+1}")
        print("-"*30)
        
        nama_barang = input("Nama Barang \t\t: ")
        
        while True:
            try:
                harga = int(input("Harga Barang \t\t: "))
                if harga > 0:
                    break
                print("Error: Harga harus lebih dari 0")
            except ValueError:
                print("Error: Masukkan angka yang valid")
        
        while True:
            try:
                jumlah = int(input("Jumlah \t\t\t: "))
                if jumlah > 0:
                    break
                print("Error: Jumlah harus lebih dari 0")
            except ValueError:
                print("Error: Masukkan angka yang valid")
        
        total_harga = harga * jumlah
        subtotal += total_harga
        daftar_barang.append([nama_barang, harga, jumlah, total_harga])

    # Hitung diskon dan pajak
    diskon, kategori = hitung_diskon(subtotal)
    pajak = (subtotal - diskon) * 0.05  # Pajak 5% setelah diskon
    total_pembayaran = subtotal - diskon + pajak

    # Cetak struk
    print("\n" + "="*60)
    print(f"{'STRUK PEMBELIAN':^60}")
    print("-"*60)
    print(f"Nama Pelanggan : {nama_pelanggan}")
    print(f"Kategori       : {kategori}")
    print("-"*60)

    # Buat tabel barang
    table = PrettyTable()
    table.field_names = ["No", "Nama Barang", "Harga", "Jumlah", "Total"]
    
    for idx, barang in enumerate(daftar_barang, 1):
        table.add_row([
            idx,
            barang[0],
            f"Rp {barang[1]:,}",
            barang[2],
            f"Rp {barang[3]:,}"
        ])

    print(table)
    print("-"*60)
    print(f"{'Subtotal':<20}: {'Rp':>25} {subtotal:>13,}")
    print(f"{'Diskon':<20}: {'Rp':>25} {diskon:>13,}")
    print(f"{'Pajak (5%)':<20}: {'Rp':>25} {pajak:>13,}")
    print("-"*60)
    print(f"{'TOTAL PEMBAYARAN':<20}: {'Rp':>25} {total_pembayaran:>13,}")
    print("-"*60)
    print(f"{'Terima Kasih Atas Kunjungan Anda!':^60}")
    print("="*60)

if __name__ == "__main__":
    main() 