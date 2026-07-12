from sqlalchemy import select

from erp.database.session import SessionLocal
from erp.models import Permission, Role, RolePermission


ROLE_PERMISSIONS = {
    "Super Admin": [
        # =====================================================
        # USER
        # =====================================================
        "user.view",
        "user.create",
        "user.update",
        "user.delete",
        # =====================================================
        # ROLE
        # =====================================================
        "role.view",
        "role.create",
        "role.update",
        "role.delete",
        # =====================================================
        # UNIT
        # =====================================================
        "unit.view",
        "unit.create",
        "unit.update",
        "unit.delete",
        # =====================================================
        # PARTNER
        # =====================================================
        "partner.view",
        "partner.create",
        "partner.update",
        "partner.delete",
        # =====================================================
        # KATEGORI BELANJA
        # =====================================================
        "category.view",
        "category.create",
        "category.update",
        "category.delete",
        # =====================================================
        # TAHUN PELAJARAN
        # =====================================================
        "academic_year.view",
        "academic_year.create",
        "academic_year.update",
        "academic_year.delete",
        # =====================================================
        # SUMBER DANA
        # =====================================================
        "fund_source.view",
        "fund_source.create",
        "fund_source.update",
        "fund_source.delete",
        # =====================================================
        # POS DANA
        # =====================================================
        "fund_position.view",
        "fund_position.create",
        "fund_position.update",
        "fund_position.delete",
        # =====================================================
        # PROPOSAL BELANJA
        # =====================================================
        "proposal.view",
        "proposal.create",
        "proposal.update",
        "proposal.approve",
        # =====================================================
        # PEMBAYARAN
        # =====================================================
        "payment.view",
        "payment.create",
        "payment.approve",
        # =====================================================
        # LAPORAN
        # =====================================================
        "report.view",
        # =====================================================
        # PENGATURAN
        # =====================================================
        "setting.manage",
    ],
}

def seed_role_permissions():

    session = SessionLocal()

    try:

        for role_name, permission_codes in ROLE_PERMISSIONS.items():

            role = session.scalar(
                select(Role).where(Role.name == role_name)
            )

            if role is None:
                continue

            for code in permission_codes:

                permission = session.scalar(
                    select(Permission).where(
                        Permission.code == code
                    )
                )

                if permission is None:
                    continue

                exists = session.scalar(
                    select(RolePermission).where(
                        RolePermission.role_id == role.id,
                        RolePermission.permission_id == permission.id,
                    )
                )

                if exists:
                    continue

                session.add(
                    RolePermission(
                        role_id=role.id,
                        permission_id=permission.id,
                    )
                )

        session.commit()

    finally:
        session.close()
