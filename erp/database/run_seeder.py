from erp.database.session import SessionLocal

from erp.database.seeders.role_seeder import seed_roles
from erp.database.seeders.unit_seeder import seed_units
from erp.database.seeders.category_seeder import seed_categories
from erp.database.seeders.permission_seeder import seed_permissions
from erp.database.seeders.user_seeder import seed_users
from erp.database.seeders.role_permission_seeder import seed_role_permissions

from erp.database.seeders.partner_seeder import seed as seed_partners
from erp.database.seeders.academic_year_seeder import (
    seed_academic_years,
)

def main():

    session = SessionLocal()

    try:

        print("=" * 50)
        print("ERP Yayasan Seeder")
        print("=" * 50)

        print("Seed Role...")
        seed_roles()

        print("Seed Unit...")
        seed_units()

        print("\nSeeding Academic Years...")
        session = SessionLocal()

        try:
            seed_academic_years(session)
        finally:
            session.close()

        print("Seed Category...")
        seed_categories()

        print("Seed Permission...")
        seed_permissions()

        print("Seed Super Admin...")
        seed_users()

        print("Seed Role Permission...")
        seed_role_permissions()

        print("Seed Partner...")
        seed_partners(session)

        print("=" * 50)
        print("SELESAI")
        print("=" * 50)

    finally:
        session.close()


if __name__ == "__main__":
    main()
