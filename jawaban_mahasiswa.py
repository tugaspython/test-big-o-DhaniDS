# File: jawaban_mahasiswa.py (Solusi Profesional)
def cari_pasangan(arr, target):
    # Menggunakan Set (Kompleksitas O(N))
    angka_dilihat = set()
    for angka in arr:
        pasangan_dibutuhkan = target - angka
        if pasangan_dibutuhkan in angka_dilihat:
            return True
        angka_dilihat.add(angka)
    return False
