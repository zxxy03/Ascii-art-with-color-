from PIL import Image
from colorama import Fore, Style, init

# Inisialisasi colorama agar berfungsi di semua OS
init(autoreset=True)

def pixel_ke_warna(pixel_value):
    """Mengembalikan warna berdasarkan tingkat kecerahan piksel."""
    if pixel_value > 230:
        return Fore.WHITE
    elif pixel_value > 200:
        return Fore.LIGHTWHITE_EX
    elif pixel_value > 170:
        return Fore.LIGHTCYAN_EX
    elif pixel_value > 140:
        return Fore.CYAN
    elif pixel_value > 110:
        return Fore.LIGHTGREEN_EX
    elif pixel_value > 80:
        return Fore.GREEN
    elif pixel_value > 50:
        return Fore.MAGENTA
    else:
        return Fore.BLUE

def gambar_ke_ascii_detail(path_gambar, lebar_baru=100):
    """Mengubah gambar menjadi ASCII art berwarna menggunakan colorama."""
    try:
        gambar = Image.open(path_gambar).convert('L')  # grayscale
    except FileNotFoundError:
        return "Error: File gambar tidak ditemukan."

    lebar, tinggi = gambar.size
    rasio_aspek = tinggi / lebar
    tinggi_baru = int(lebar_baru * rasio_aspek * 0.55)
    gambar_resized = gambar.resize((lebar_baru, tinggi_baru))
    piksel = gambar_resized.getdata()

    karakter = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/;:,\"^`'. "
    panjang_karakter = len(karakter)

    ascii_art = []
    baris = ""
    for i, pixel_value in enumerate(piksel):
        index = pixel_value * panjang_karakter // 255
        char = karakter[panjang_karakter - 1 - index]
        warna = pixel_ke_warna(pixel_value)
        baris += warna + char
        if (i + 1) % lebar_baru == 0:
            ascii_art.append(baris)
            baris = ""
    return ascii_art

if __name__ == "__main__":
    path_gambar = input("Path lengkap gambar: ")
    lebar_hasil = int(input("Ukuran Ascii: "))

    hasil_ascii = gambar_ke_ascii_detail(path_gambar, lebar_hasil)

    if isinstance(hasil_ascii, str) and hasil_ascii.startswith("Error"):
        print(hasil_ascii)
    else:
        for baris in hasil_ascii:
            print(baris)
