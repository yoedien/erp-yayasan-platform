from erp.database.seeders.permission_seeder import seed_permissions
from erp.database.seeders.role_seeder import seed_roles
from erp.database.seeders.unit_seeder import seed_units


def main():

    print("Seeding Roles...")
    seed_roles()

    print("Seeding Units...")
    seed_units()

    print("Seeding Permissions...")
    seed_permissions()

    print("Done.")


if __name__ == "__main__":
    main()