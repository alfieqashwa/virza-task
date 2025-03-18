from prettytable import PrettyTable

def main():
    # Print header
    print("\n" + "="*53)
    print(f"{'INPUT DATA GAJI KARYAWAN':^53}")
    print("-"*53)

    # Get number of employees
    jumlah_karyawan = int(input("Masukkan jumlah karyawan: "))
    data_karyawan = []

    # Input data for each employee
    for i in range(jumlah_karyawan):
        print("-" * 30)
        nama = input("Masukkan Nama Karyawan \t: ")
        golongan = input("Masukkan golongan karyawan (1A/1B/1C): ").strip().upper()

        # Determine salary and benefits based on grade
        if golongan == "1A":
            gaji_pokok = 1200000
            tunjangan = 600000
            pajak_persen = 0.02
        elif golongan == "1B":
            gaji_pokok = 1800000
            tunjangan = 900000
            pajak_persen = 0.03
        elif golongan == "1C":
            gaji_pokok = 2500000
            tunjangan = 1200000
            pajak_persen = 0.04
        else:
            print(f"Golongan tidak valid untuk karyawan {nama}. Mohon masukkan golongan yang benar (1A, 1B, atau 1C).")
            continue

        # Calculate salary details
        total_gaji = gaji_pokok + tunjangan
        pajak = total_gaji * pajak_persen
        gaji_bersih = total_gaji - pajak
        
        # Store employee data
        data_karyawan.append([
            nama, 
            golongan, 
            gaji_pokok, 
            tunjangan, 
            pajak, 
            gaji_bersih
        ])

    # Create and configure table
    table = PrettyTable()
    table.field_names = [
        "No",
        "Karyawan",
        "Golongan",
        "Gaji Pokok",
        "Tunjangan",
        "Pajak",
        "Gaji Bersih"
    ]

    # Add data to table
    for id, karyawan in enumerate(data_karyawan, start=1):
        table.add_row([
            id,
            karyawan[0],
            karyawan[1],
            f"{karyawan[2]:,}",
            f"{karyawan[3]:,}",
            f"{karyawan[4]:,.0f}",
            f"{karyawan[5]:,.0f}"
        ])

    # Display final table
    print("\nData Gaji Karyawan")
    print(table)

if __name__ == "__main__":
    main()