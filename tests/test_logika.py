import pytest

from app.logika import bersihkan_judul, hitung_progres


def test_bersihkan_judul_merapikan_spasi():
    assert bersihkan_judul("  belajar   CI/CD ") == "belajar CI/CD"


@pytest.mark.parametrize("masukan", [None, "", "   ", "x" * 101])
def test_bersihkan_judul_tidak_valid(masukan):
    assert bersihkan_judul(masukan) is None


def test_hitung_progres_kosong():
    assert hitung_progres([]) == 0


def test_hitung_progres_sebagian():
    tugas = [{"selesai": 1}, {"selesai": 0}, {"selesai": 0}]
    assert hitung_progres(tugas) == 33
