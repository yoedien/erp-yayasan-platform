from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models.permission import Permission

PERMISSIONS = [
    # =====================================================
    # USER
    # =====================================================
    ("user.view", "Lihat User", "User"),
    ("user.create", "Tambah User", "User"),
    ("user.update", "Ubah User", "User"),
    ("user.delete", "Hapus User", "User"),
    # =====================================================
    # ROLE
    # =====================================================
    ("role.view", "Lihat Role", "Role"),
    ("role.create", "Tambah Role", "Role"),
    ("role.update", "Ubah Role", "Role"),
    ("role.delete", "Hapus Role", "Role"),
    # =====================================================
    # UNIT
    # =====================================================
    ("unit.view", "Lihat Unit", "Unit"),
    ("unit.create", "Tambah Unit", "Unit"),
    ("unit.update", "Ubah Unit", "Unit"),
    ("unit.delete", "Hapus Unit", "Unit"),
    # =====================================================
    # PARTNER
    # =====================================================
    ("partner.view", "Lihat Partner", "Partner"),
    ("partner.create", "Tambah Partner", "Partner"),
    ("partner.update", "Ubah Partner", "Partner"),
    ("partner.delete", "Hapus Partner", "Partner"),
    # =====================================================
    # KATEGORI BELANJA
    # =====================================================
    ("category.view", "Lihat Kategori", "Kategori"),
    ("category.create", "Tambah Kategori", "Kategori"),
    ("category.update", "Ubah Kategori", "Kategori"),
    ("category.delete", "Hapus Kategori", "Kategori"),
    # =====================================================
    # TAHUN PELAJARAN
    # =====================================================
    ("academic_year.view", "Lihat Tahun Pelajaran", "Master Keuangan"),
    ("academic_year.create", "Tambah Tahun Pelajaran", "Master Keuangan"),
    ("academic_year.update", "Ubah Tahun Pelajaran", "Master Keuangan"),
    ("academic_year.delete", "Hapus Tahun Pelajaran", "Master Keuangan"),
    # =====================================================
    # SUMBER DANA
    # =====================================================
    ("fund_source.view", "Lihat Sumber Dana", "Master Keuangan"),
    ("fund_source.create", "Tambah Sumber Dana", "Master Keuangan"),
    ("fund_source.update", "Ubah Sumber Dana", "Master Keuangan"),
    ("fund_source.delete", "Hapus Sumber Dana", "Master Keuangan"),
    # =====================================================
    # POS DANA
    # =====================================================
    ("fund_position.view", "Lihat Pos Dana", "Master Keuangan"),
    ("fund_position.create", "Tambah Pos Dana", "Master Keuangan"),
    ("fund_position.update", "Ubah Pos Dana", "Master Keuangan"),
    ("fund_position.delete", "Hapus Pos Dana", "Master Keuangan"),
    # =====================================================
    # PROPOSAL
    # =====================================================
    ("proposal.view", "Lihat Pengajuan", "Proposal"),
    ("proposal.create", "Buat Pengajuan", "Proposal"),
    ("proposal.update", "Ubah Pengajuan", "Proposal"),
    ("proposal.approve", "Setujui Pengajuan", "Proposal"),
    # =====================================================
    # PAYMENT
    # =====================================================
    ("payment.view", "Lihat Pembayaran", "Payment"),
    ("payment.create", "Buat Pembayaran", "Payment"),
    ("payment.approve", "Setujui Pembayaran", "Payment"),
    # =====================================================
    # REPORT
    # =====================================================
    ("report.view", "Lihat Laporan", "Report"),
    # =====================================================
    # SETTING
    # =====================================================
    ("setting.manage", "Kelola Pengaturan", "Setting"),
]

def seed_permissions():
    session = SessionLocal()

    try:
        for code, name, module in PERMISSIONS:

            exists = session.scalar(select(Permission).where(Permission.code == code))

            if exists:
                continue

            session.add(
                Permission(
                    code=code,
                    name=name,
                    module=module,
                    description=None,
                )
            )

        session.commit()

    finally:
        session.close()
