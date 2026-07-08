from erp.database.seeders.role_seeder import (
    seed_roles,
)
from erp.database.seeders.unit_seeder import (
    seed_units,
)
from erp.database.seeders.permission_seeder import (
    seed_permissions,
)
from erp.database.seeders.user_seeder import (
    seed_super_admin,
)
from erp.database.seeders.role_permission_seeder import (
    seed_role_permissions,
)
from erp.database.seeders.category_seeder import (
    seed_categories,
)


def main():

    print("=" * 50)
    print("ERP Yayasan Database Seeder")
    print("=" * 50)

    print("\nSeeding Roles...")
    seed_roles()

    print("\nSeeding Units...")
    seed_units()

    print("\nSeeding Categories...")
    seed_categories()

    print("\nSeeding Permissions...")
    seed_permissions()

    print("\nSeeding Super Admin...")
    seed_super_admin()

    print("\nSeeding Role Permissions...")
    seed_role_permissions()

    print("\n" + "=" * 50)
    print("Semua Seeder berhasil dijalankan.")
    print("=" * 50)


if __name__ == "__main__":
    main()