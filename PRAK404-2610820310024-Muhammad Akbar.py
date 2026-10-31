while True:
    print("Pilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    
    pilihan = int(input("Masukkan Pilihan : "))
    
    if pilihan == 5:
        print("Terimakasih, telah menggunakan kalkulator Muhammad Akbar")
        break
    elif pilihan in [1, 2, 3, 4]:
        nil1 = float(input("Masukkan nilai pertama : "))
        nil2 = float(input("Masukkan nilai kedua : "))
        
        if pilihan == 1:
            nama_op = "penjumlahan"
            hasil = nil1 + nil2
        elif pilihan == 2:
            nama_op = "pengurangan"
            hasil = nil1 - nil2
        elif pilihan == 3:
            nama_op = "perkalian"
            hasil = nil1 * nil2
        elif pilihan == 4:
            nama_op = "pembagian"
            hasil = nil1 / nil2
            
        print(f"Hasil {nama_op} antara {nil1:.2f} dengan {nil2:.2f} adalah {hasil:.2f}")
    else:
        print("Input anda salah, silahkan coba lagi")
    print()