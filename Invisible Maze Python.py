# Pake Module Time buat cooldown
import time

# Fungsi untuk labirin terlihat / visible
def labirin_terlihat(labirin, posisi_pemain, terlihat):
    for i in range(len(labirin)): # baris labirin
        for j in range(len(labirin[i])): # kolom labirin
            if (i, j) == posisi_pemain:
                print("P", end=" ") # posisi player
            elif terlihat:
                if labirin[i][j] == 0:
                    print(".", end=" ") # jalan
                elif labirin[i][j] == 1:
                    print("#", end=" ") # tembok
                elif labirin[i][j] == 2:
                    print("F", end=" ") # finish
            else:
                print("?", end=" ") # Maze invisible
        print()
    print()
    

# Fungsi perpindahan player
def pindah(posisi_pemain, perintah, labirin):
    i, j = posisi_pemain
    if perintah == "w": # Atas
        if i > 0:
            i -= 1  # posisi pemain berkurang 1 baris
    elif perintah == "s":  # Bawah
        if i < len(labirin) - 1:
            i += 1
    elif perintah == "a":  # Kiri
        if j > 0:
            j -= 1
    elif perintah == "d":  # Kanan
        if j < len(labirin[i]) - 1:
            j += 1
    return (i, j)

# Fungsi Jarak agar user tidak melihat (labirin terlihat)
def pembersih_layar():
    print("\n" *50) # \n kegunaannya untuk membuat baris dan dikali 50
    
# Fungsi menjalankan game
def main():
    while True: # menggunakan infinity loop sampai break program
        print("\n=== Game Invisible Maze ===")
        print("Instruksi:")
        print("1. Gunakan W (atas), S (bawah), A (kiri), D (kanan) untuk bergerak.")
        print("2. Hindari dinding ('#') dan menuju Finish ('F').")
        print("3. Labirin akan terlihat selama beberapa detik, lalu menjadi tak terlihat.\n") 
        
        pilihan = input("Tekan Enter Untuk Memulai...\n")
    
        #labirin bawaan
        labirin = [
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 2],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
        ]
        
        labirin2 = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 1, 2],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        
        # pilihan ingin menggunakan labirin bawaan atau tidak
        print("Pilih Labirin Anda")
        print("1.Labirin 1")
        print("2.Labirin 2")
        print("3.Membuat Labirin Baru")
        pilihan = input("Masukkan Pilihan: ")
        
        if pilihan == "1":
            labirin
            
        elif pilihan == "2":
            labirin2
        
        elif pilihan == "3":
            print("Buat Labirin baru (0 = jalan, 1 = tembok, 2 = Finish):")
            labirin = []
            for i in range(5):
                baris = input(f"Masukkan baris ke-{i + 1} (contoh: 0 1 0 1 2): ").split()
                labirin.append([int(x) for x in baris])
                
        else:
            print("Input Anda Tidak sesuai")
                
        posisi_pemain = (0, 0) # posisi awal pemain
            
        # labirin terlihat
        print("\nLabirin Terlihat:")
        labirin_terlihat(labirin, posisi_pemain, terlihat=True)
        print("(labirin akan menjadi tak terlihat setelah beberapa saat.)")
    
        for i in range(10, 0, -1):
            print(f"Permainan dimulai dalam {i} detik...", end="\r") # \r digunakan untuk menimpa print
            time.sleep(1) # memakai module time selama 1 detik

        # input("Tekan Enter untuk memulai...")
        
        pembersih_layar()
        
        # labirin tidak terlihat
        while True:
            labirin_terlihat(labirin, posisi_pemain, terlihat=False)
            
            # posisi_pemain = (2, 3) posisi_pemain[0] = 2 [posisi_pemain[1] = 3
            # digunakan untuk membedakan baris dan kolom
            # program berjalan terus sampai finish
            if labirin[posisi_pemain[0]][posisi_pemain[1]] == 2:
                print("Selamat! Kamu berhasil mencapai Finish!")
                break # memberhentikan loop while true
            
            # program menjalakan perintah dan perpindahan player
            perintah = input("Gunakan W/A/S/D untuk menjalankan game: ").lower()
            if perintah in ["w", "a", "s", "d"]:
                posisi_pemain = pindah(posisi_pemain, perintah, labirin)
                # Program apabila menabrak tembok
                if labirin[posisi_pemain[0]][posisi_pemain[1]] == 1:
                    print("Kamu menabrak dinding! Game Over!")
                    break
                posisi_pemain
                
            else:
                print("Perintah tidak valid. Gunakan W, A, S, atau D.")
            
        # Menanyakan ingin bermain ulang
        ulang = input("Apakah kamu ingin bermain lagi? (y/n): ").lower()
        if ulang == "n":
            print("Terima kasih telah bermain. Sampai jumpa!")
            break
        
# Mengulang kembali
main()
                