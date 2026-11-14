"""Logika murni (tanpa Flask/DB) -> paling mudah dites unit."""

MAKS_PANJANG = 100


def bersihkan_judul(judul):
    """Rapikan judul tugas. Return string bersih atau None jika tidak valid."""
    if judul is None:
        return None
    judul = " ".join(judul.split())  # rapikan spasi berlebih
    if not judul or len(judul) > MAKS_PANJANG:
        return None
    return judul


def hitung_progres(tugas):
    """Persentase tugas selesai (0-100, dibulatkan). Daftar kosong -> 0."""
    if not tugas:
        return 0
    selesai = sum(1 for t in tugas if t["selesai"])
    return round(selesai / len(tugas) * 100)
