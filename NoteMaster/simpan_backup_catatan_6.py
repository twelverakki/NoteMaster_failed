# simpan_muat_catatan.py  

import json  
import csv  

# Daftar catatan yang akan digunakan dalam modul ini  
catatan_list = []  

def simpan_catatan_json(file_path: str) -> None:  
    """  
    Menyimpan catatan ke file dalam format JSON.  

    Args:  
        file_path (str): Jalur file tempat catatan akan disimpan.  

    Returns:  
        None: Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan konfirmasi.  
    """  
    with open(file_path, 'w', encoding='utf-8') as file:  
        json.dump(catatan_list, file, ensure_ascii=False, indent=4)  
    print(f"Catatan berhasil disimpan ke {file_path}.")  

def simpan_catatan_txt(file_path: str) -> None:  
    """  
    Menyimpan catatan ke file dalam format TXT.  

    Args:  
        file_path (str): Jalur file tempat catatan akan disimpan.  

    Returns:  
        None: Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan konfirmasi.  
    """  
    with open(file_path, 'w', encoding='utf-8') as file:  
        for catatan in catatan_list:  
            file.write(f"{catatan['judul']}\n{catatan['isi']}\n\n")  
    print(f"Catatan berhasil disimpan ke {file_path}.")  

def simpan_catatan_csv(file_path: str) -> None:  
    """  
    Menyimpan catatan ke file dalam format CSV.  

    Args:  
        file_path (str): Jalur file tempat catatan akan disimpan.  

    Returns:  
        None: Fungsi ini tidak mengembalikan nilai, tetapi mencetak pesan konfirmasi.  
    """  
    with open(file_path, 'w', newline='', encoding='utf-8') as file:  
        writer = csv.DictWriter(file, fieldnames=["judul", "isi"])  
        writer.writeheader()  
        writer.writerows(catatan_list)  
    print(f"Catatan berhasil disimpan ke {file_path}.")  

def muat_catatan_json(file_path: str) -> list:  
    """  
    Memuat catatan dari file JSON.  

    Args:  
        file_path (str): Jalur file dari mana catatan akan dimuat.  

    Returns:  
        list: Daftar catatan yang dimuat dari file. Jika terjadi kesalahan, mengembalikan daftar kosong.  
    """  
    global catatan_list  
    try:  
        with open(file_path, 'r', encoding='utf-8') as file:  
            catatan_list = json.load(file)  
        print(f"Catatan berhasil dimuat dari {file_path}.")  
        return catatan_list  
    except FileNotFoundError:  
        print(f"File {file_path} tidak ditemukan.")  
        return []  
    except json.JSONDecodeError:  
        print(f"File {file_path} tidak dapat dibaca. Pastikan formatnya benar.")  
        return []  

def muat_catatan_txt(file_path: str) -> list:  
    """  
    Memuat catatan dari file TXT.  

    Args:  
        file_path (str): Jalur file dari mana catatan akan dimuat.  

    Returns:  
        list: Daftar catatan yang dimuat dari file. Jika terjadi kesalahan, mengembalikan daftar kosong.  
    """  
    global catatan_list  
    catatan_list = []  
    try:  
        with open(file_path, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
            for i in range(0, len(lines), 3):  
                judul = lines[i].strip()  
                isi = lines[i + 1].strip()  
                catatan_list.append({"judul": judul, "isi": isi})  
        print(f"Catatan berhasil dimuat dari {file_path}.")  
        return catatan_list  
    except FileNotFoundError:  
        print(f"File {file_path} tidak ditemukan.")  
        return []  

def muat_catatan_csv(file_path: str) -> list:  
    """  
    Memuat catatan dari file CSV.  

    Args:  
        file_path (str): Jalur file dari mana catatan akan dimuat.  

    Returns:  
        list: Daftar catatan yang dimuat dari file. Jika terjadi kesalahan, mengembalikan daftar kosong.  
    """  
    global catatan_list  
    catatan_list = []  
    try:  
        with open(file_path, 'r', encoding='utf-8') as file:  
            reader = csv.DictReader(file)  
            for row in reader:  
                catatan_list.append(row)  
        print(f"Catatan berhasil dimuat dari {file_path}.")  
        return catatan_list  
    except FileNotFoundError:  
        print(f"File {file_path} tidak ditemukan.")  
        return []
    
