# ERP Yayasan Platform - Codex Guidelines

## Project Overview

Aplikasi ERP Yayasan berbasis:

- Python
- PySide6
- SQLAlchemy ORM
- Alembic Migration
- SQLite/PostgreSQL


# Arsitektur

Gunakan pola:

GUI
 ↓
Service
 ↓
Repository
 ↓
Database


Jangan melakukan query database langsung dari GUI.


# Struktur Modul

Setiap modul CRUD harus memiliki:

- Model
- Repository
- Service
- Page
- Dialog
- TableModel
- Permission
- Seeder


# Database

Semua perubahan database wajib menggunakan Alembic.

Jangan mengubah database secara manual.


# Coding Rules

Gunakan:

- Python PEP8
- Type hint
- SQLAlchemy ORM


Gunakan format komentar:

# ==========================================
# CREATE
# ==========================================


# Perubahan File

Sebelum mengubah kode:

Jelaskan:
1. File yang akan diubah
2. Tujuan perubahan
3. Dampak perubahan


# Jangan

- Jangan menghapus fitur yang sudah berjalan.
- Jangan mengubah struktur folder tanpa alasan.
- Jangan membuat query database di GUI.
- Jangan melakukan commit atau push tanpa perintah.


# Git Workflow

Developer yang melakukan:

git add
git commit
git push


# Testing

Sebelum menyatakan selesai:

- cek import
- jalankan aplikasi
- cek migration
- cek permission