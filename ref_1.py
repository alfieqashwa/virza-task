from prettytable import PrettyTable

def main():
    # Initialize table
    table = PrettyTable()

    # Print header
    print("\n" + "="*53)
    print(f"{'INPUT DATA NILAI SISWA':^53}")
    print("-"*53)

    # Initialize data storage
    data_mhs = []

    # Get number of students
    jml_mhs = int(input("Masukan Jumlah Mahasiswa : "))

    # Input data for each student
    for i in range(jml_mhs):
        print(f"\nData Siswa ke {i+1}")
        print("-"*30)

        # Get student details
        nama = input("Masukan Nama Mahasiswa \t: ")
        kls = input("Masukan Kelas \t\t: ")
        kehadiran = int(input("Jumlah Kehadiran (0-12) : "))
        nilai1 = int(input("Masukan Nilai Tugas \t: "))
        nilai2 = int(input("Masukan Nilai UTS \t: "))
        nilai3 = int(input("Masukan Nilai UAS \t: "))

        # Calculate attendance percentage
        persen_kehadiran = (kehadiran / 12) * 100

        # Calculate final grade
        rata2 = float(f"{(persen_kehadiran * 0.2) + (nilai1 * 0.1) + (nilai2 * 0.3) + (nilai3 * 0.4):.1f}")

        # Determine grade
        if rata2 >= 85: 
            grade = "A"
        elif rata2 >= 75: 
            grade = "B"
        elif rata2 >= 65: 
            grade = "C"
        elif rata2 >= 50: 
            grade = "D"
        else: 
            grade = "E"

        # Add separator
        print("_"*30)

        # Store student data
        data_mhs.append([nama, kls, kehadiran, nilai1, nilai2, nilai3, rata2, grade])
        print("\nData Berhasil Di tambahkan\n")

    # Set up table headers
    table.field_names = [
        "No",
        "Nama",
        "Kelas",
        "Kehadiran",
        "Nilai 1",
        "Nilai 2",
        "Nilai 3",
        "Rata-Rata",
        "Grade"
    ]

    # Add data to table
    for index, mhs in enumerate(data_mhs, start=1):
        table.add_row([index] + mhs)

    # Display final table
    print(table)

if __name__ == "__main__":
    main()