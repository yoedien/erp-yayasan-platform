import sys

from PySide6.QtWidgets import QApplication

from erp.gui.windows.login_window import LoginWindow

import erp.gui.windows.main_window

print("MainWindow file :", erp.gui.windows.main_window.__file__)


def main():

    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
