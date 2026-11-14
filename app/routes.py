from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from .db import get_db
from .logika import bersihkan_judul, hitung_progres

bp = Blueprint("main", __name__)


@bp.get("/health")
def health():
    return jsonify(status="ok")


@bp.get("/")
def index():
    tugas = get_db().execute("SELECT * FROM tugas ORDER BY id").fetchall()
    return render_template("index.html", tugas=tugas, progres=hitung_progres(tugas))


@bp.post("/tambah")
def tambah():
    judul = bersihkan_judul(request.form.get("judul"))
    if judul is None:
        return "Judul tidak valid", 400
    db = get_db()
    db.execute("INSERT INTO tugas (judul) VALUES (?)", (judul,))
    db.commit()
    return redirect(url_for("main.index"))


@bp.post("/selesai/<int:id>")
def selesai(id):
    db = get_db()
    db.execute("UPDATE tugas SET selesai = 1 - selesai WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("main.index"))


@bp.post("/hapus/<int:id>")
def hapus(id):
    db = get_db()
    db.execute("DELETE FROM tugas WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("main.index"))
