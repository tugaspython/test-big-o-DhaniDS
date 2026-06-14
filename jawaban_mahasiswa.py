def cari_pasangan(arr, target):
    angka_ditemukan = set()

    for angka in arr:
        pasangan = target - angka

        if pasangan in angka_ditemukan:
            return True

        angka_ditemukan.add(angka)

    return False
