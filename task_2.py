from prettytable import PrettyTable

def hitung_gaji(golongan):
    """Menghitung gaji berdasarkan golongan karyawan"""
    data_golongan = {
        "1A": {"gaji": 1_200_000, "tunjangan": 600_000, "pajak": 0.02},
        "1B": {"gaji": 1_800_000, "tunjangan": 900_000, "pajak": 0.03},
        "1C": {"gaji": 2_500_000, "tunjangan": 1_200_000, "pajak": 0.04}
    }
    
    if golongan not in data_golongan:
        return None
    
    return data_golongan[golongan]

def main():
    # Tampilkan header
    print("\n" + "="*60)
    print(f"{'PROGRAM PENGHITUNG GAJI KARYAWAN':^60}")
    print("-"*60)

    # Input jumlah karyawan
    while True:
        try:
            jumlah_karyawan = int(input("Masukkan Jumlah Karyawan \t: "))
            if jumlah_karyawan > 0:
                break
            print("Error: Jumlah karyawan harus lebih dari 0")
        except ValueError:
            print("Error: Masukkan angka yang valid")

    # List untuk menyimpan data
    data_karyawan = []

    # Input data setiap karyawan
    for i in range(jumlah_karyawan):
        print(f"\nData Karyawan ke-{i+1}")
        print("-"*30)
        
        nama = input("Nama Karyawan \t\t: ")
        golongan = input("Golongan (1A/1B/1C) \t: ").strip().upper()
        
        # Hitung gaji berdasarkan golongan
        data_gaji = hitung_gaji(golongan)
        
        if not data_gaji:
            print(f"Error: Golongan '{golongan}' tidak valid untuk karyawan {nama}")
            print("Golongan yang tersedia: 1A, 1B, 1C")
            continue
            
        # Hitung komponen gaji
        gaji_pokok = data_gaji["gaji"]
        tunjangan = data_gaji["tunjangan"]
        total_gaji = gaji_pokok + tunjangan
        pajak = total_gaji * data_gaji["pajak"]
        gaji_bersih = total_gaji - pajak
        
        # Simpan data karyawan
        data_karyawan.append([
            nama, 
            golongan, 
            gaji_pokok, 
            tunjangan, 
            pajak, 
            gaji_bersih
        ])
        print("\nData berhasil disimpan!")

    # Buat tabel
    table = PrettyTable()
    table.field_names = [
        "No",
        "Nama",
        "Golongan",
        "Gaji Pokok",
        "Tunjangan",
        "Pajak",
        "Gaji Bersih"
    ]
    
    # Tambahkan data ke tabel
    for idx, karyawan in enumerate(data_karyawan, 1):
        table.add_row([
            idx,
            karyawan[0],
            karyawan[1],
            f"Rp {karyawan[2]:,}",
            f"Rp {karyawan[3]:,}",
            f"Rp {karyawan[4]:,.0f}",
            f"Rp {karyawan[5]:,.0f}"
        ])

    # Tampilkan hasil
    print("\n" + "="*60)
    print(f"{'DAFTAR GAJI KARYAWAN':^60}")
    print("-"*60)
    print(table)
    print("="*60)

if __name__ == "__main__":
    main()