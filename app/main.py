PythonFinalizationError
from datetime import datetime

APP_NAME = "ERP Yayasan Platform"
VERSION = "0.1.0"


def main():
    print("=" * 60)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Started : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("=" * 60)
    print("Foundation berhasil dibuat.")
    print("=" * 60)


if __name__ == "__main__":
    main()