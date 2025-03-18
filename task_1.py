#!/usr/bin/env python3
from prettytable import PrettyTable

def hitung_rata_kehadiran(kehadiran):
    """Menghitung rata-rata kehadiran dari 12 pertemuan"""
    return sum(kehadiran) / len(kehadiran) * 100

def hitung_nilai_akhir(nilai_kehadiran, nilai_tugas, nilai_uts, nilai_uas):
    """Menghitung nilai akhir berdasarkan bobot yang ditentukan"""
    return (
        (nilai_kehadiran * 0.2) +  # Kehadiran 20%
        (nilai_tugas * 0.1) +      # Tugas 10%
        (nilai_uts * 0.3) +        # UTS 30%
        (nilai_uas * 0.4)          # UAS 40%
    )

def tentukan_grade(nilai_rata):
    """Menentukan grade berdasarkan nilai rata-rata"""
    if nilai_rata >= 85:
        return "A"
    if nilai_rata >= 75:
        return "B"
    if nilai_rata >= 65:
        return "C"
    if nilai_rata >= 50:
        return "D"
    return "E"

def main():
    # Print header
    print("\n" + "="*53)
    print(f"{'INPUT DATA NILAI SISWA':^53}")
    print("-"*53)

    # Input jumlah siswa
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    
    # List untuk menyimpan data siswa
    data_siswa = []
    
    # Input data untuk setiap siswa
    for i in range(jumlah_siswa):
        print(f"\nData Siswa ke {i + 1}")
        print("-"*30)
        
        nama = input("Masukkan Nama Siswa \t: ")
        kelas = input("Masukkan Kelas \t\t: ")
        
        # Simplified attendance input
        while True:
            try:
                kehadiran = int(input("Jumlah Kehadiran (0-12)\t: "))
                if 0 <= kehadiran <= 12:
                    break
                print("Error: Jumlah kehadiran harus antara 0-12")
            except ValueError:
                print("Error: Masukkan angka yang valid")
        
        # Hitung persentase kehadiran langsung
        nilai_kehadiran = (kehadiran / 12) * 100
        
        # Input nilai tugas, UTS, dan UAS
        while True:
            try:
                nilai_tugas = float(input("\nNilai tugas (0-100): "))
                if 0 <= nilai_tugas <= 100:
                    break
                print("Error: Nilai harus antara 0-100")
            except ValueError:
                print("Error: Masukkan nilai yang valid")
        
        while True:
            try:
                nilai_uts = float(input("Nilai UTS (0-100): "))
                if 0 <= nilai_uts <= 100:
                    break
                print("Error: Nilai harus antara 0-100")
            except ValueError:
                print("Error: Masukkan nilai yang valid")
        
        while True:
            try:
                nilai_uas = float(input("Nilai UAS (0-100): "))
                if 0 <= nilai_uas <= 100:
                    break
                print("Error: Nilai harus antara 0-100")
            except ValueError:
                print("Error: Masukkan nilai yang valid")
        
        # Hitung nilai akhir
        nilai_akhir = hitung_nilai_akhir(nilai_kehadiran, nilai_tugas, nilai_uts, nilai_uas)
        grade = tentukan_grade(nilai_akhir)
        
        # Simpan data siswa
        data_siswa.append({
            "nama": nama,
            "kelas": kelas,
            "kehadiran": nilai_kehadiran,
            "tugas": nilai_tugas,
            "uts": nilai_uts,
            "uas": nilai_uas,
            "nilai_akhir": nilai_akhir,
            "grade": grade
        })
    
    # Buat tabel menggunakan PrettyTable
    table = PrettyTable()
    table.field_names = ["No", "Nama", "Kelas", "Kehadiran", "Tugas", "UTS", "UAS", "Rata-rata", "Grade"]
    
    # Atur perataan kolom
    table.align["No"] = "r"  # rata kanan
    table.align["Nama"] = "l"  # rata kiri
    table.align["Kelas"] = "l"  # rata kiri
    table.align["Kehadiran"] = "r"  # rata kanan
    table.align["Tugas"] = "r"  # rata kanan
    table.align["UTS"] = "r"  # rata kanan
    table.align["UAS"] = "r"  # rata kanan
    table.align["Rata-rata"] = "r"  # rata kanan
    table.align["Grade"] = "c"  # rata tengah
    
    # Tambahkan data ke tabel
    for i, siswa in enumerate(data_siswa, 1):
        table.add_row([
            i,
            siswa["nama"],
            siswa["kelas"],
            f"{siswa['kehadiran']:.2f}",
            f"{siswa['tugas']:.1f}",
            f"{siswa['uts']:.1f}",
            f"{siswa['uas']:.1f}",
            f"{siswa['nilai_akhir']:.2f}",
            siswa["grade"]
        ])
    
    # Tampilkan tabel
    print("\nDaftar Nilai Siswa")
    print(table)

if __name__ == "__main__":
    main() 