def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_tambah_tugas_muncul_di_halaman(client):
    client.post("/tambah", data={"judul": "Belajar pytest"})
    r = client.get("/")
    assert "Belajar pytest" in r.get_data(as_text=True)


def test_tambah_judul_kosong_ditolak(client):
    r = client.post("/tambah", data={"judul": "   "})
    assert r.status_code == 400


def test_toggle_selesai_mengubah_progres(client):
    client.post("/tambah", data={"judul": "A"})
    client.post("/selesai/1")
    assert "Progres: 100%" in client.get("/").get_data(as_text=True)


def test_hapus_tugas(client):
    client.post("/tambah", data={"judul": "Sementara"})
    client.post("/hapus/1")
    assert "Sementara" not in client.get("/").get_data(as_text=True)
