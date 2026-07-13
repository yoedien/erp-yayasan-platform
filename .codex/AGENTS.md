# ERP Yayasan Platform

## Tujuan

Membangun aplikasi ERP Yayasan berbasis Python + PySide6 + SQLAlchemy
dengan arsitektur bersih, mudah dipelihara, dan konsisten.

---

# Aturan Utama

JANGAN PERNAH:

- menghapus fitur yang sudah berjalan
- mengganti struktur folder tanpa diminta
- mengubah nama class
- mengubah API service
- mengubah repository yang sudah stabil

Jika perlu perubahan besar,
selalu jelaskan dahulu.

---

# Standar Pengerjaan

Semua fitur baru WAJIB memiliki:

- Model
- Repository
- Service
- Dialog
- Page
- TableModel
- Permission
- Seeder bila diperlukan

Tidak boleh langsung query database dari GUI.

GUI hanya boleh memanggil Service.

Service hanya boleh memanggil Repository.

Repository saja yang mengakses database.

---

# Cara Mengedit

Saat memberi jawaban:

Gunakan format:

🆕 BUAT FILE BARU

➕ TAMBAHKAN

✏️ GANTI

❌ HAPUS

Jangan hanya menjelaskan.

Selalu tampilkan kode lengkap jika file berubah.

---

# Database

Menggunakan:

- SQLAlchemy ORM
- Alembic Migration

Jangan membuat database manual.

Semua perubahan schema harus melalui migration.

---

# Coding Style

Gunakan:

PEP8

Type hint bila memungkinkan.

Method dipisahkan menggunakan komentar:

# ==========================================
# CREATE
# ==========================================

# ==========================================
# UPDATE
# ==========================================

dst.

---

# GUI

Framework:

PySide6

Semua halaman CRUD mengikuti:

BaseCrudPage

Semua dialog mengikuti pola project.

---

# Repository

Tidak boleh ada business logic.

Repository hanya CRUD.

Business logic berada di Service.

---

# Error

Gunakan ValueError bila validasi gagal.

GUI menampilkan QMessageBox.

---

# Sebelum selesai

Selalu lakukan:

- cek import
- cek relasi
- cek compile
- cek migration
- cek permission
- cek menu

Jangan meninggalkan kode setengah jadi.

---

# Git

Jangan melakukan commit.

Jangan melakukan push.

Biarkan developer yang melakukan commit.

---

# Target

Kode harus production ready.

Tidak boleh demo quality.
