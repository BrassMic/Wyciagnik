import sys
import os
import shutil
import random
from pathlib import Path

from PySide6.QtCore import Qt, QFile
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidgetItem
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Ustalanie ścieżki do pliku .ui w zależności od trybu uruchamiania
        if hasattr(sys, '_MEIPASS'):
            # Uruchamiane z pliku wykonywalnego
            base_path = Path(sys._MEIPASS)
        else:
            # Uruchamiane ze źródła
            base_path = Path(__file__).resolve().parent

        ui_file_path = QFile(base_path / "wyciagnik/form.ui")
        if not ui_file_path.exists():
            QMessageBox.critical(self, "Error", f"UI file not found: {ui_file_path.fileName()}")
            sys.exit(1)

        ui_file_path.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file_path)
        ui_file_path.close()

        if self.ui is None:
            QMessageBox.critical(self, "Error", f"Could not load UI file from {ui_file_path}")
            sys.exit(1)

        self.setCentralWidget(self.ui)

        # Ustawienie ikony okna
        icon_path = base_path / "resources/icon.ico"
        if not icon_path.exists():
            QMessageBox.critical(self, "Error", f"Icon file not found: {icon_path}")
            sys.exit(1)

        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle("Wyciągnik")
        self.setFixedSize(850, 800)

        # Przyciski do metod
        self.ui.mkat_button.clicked.connect(self.select_main_directory)
        self.ui.dkat_button.clicked.connect(self.select_destination_directory)
        self.ui.start_button.clicked.connect(self.start_action)

        # Inicjalizacja listy katalogów
        self.load_directory_list()

    def select_main_directory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Main Directory")
        if dir_path:
            self.ui.mkatline.setText(dir_path)
            self.load_directory_list()

    def select_destination_directory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Destination Directory")
        if dir_path:
            self.ui.dkatline.setText(dir_path)

    def load_directory_list(self):
        self.ui.kat_widget.clear()
        main_dir = self.ui.mkatline.text()

        if os.path.isdir(main_dir):
            for folder_name in os.listdir(main_dir):
                folder_path = os.path.join(main_dir, folder_name)
                if os.path.isdir(folder_path):
                    item = QListWidgetItem(folder_name)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.ui.kat_widget.addItem(item)

    def start_action(self):
        min_files = self.ui.min_line.text()
        max_files = self.ui.max_line.text()
        try:
            min_files = int(min_files)
            max_files = int(max_files)
        except ValueError:
            QMessageBox.warning(self, "Invalid input", "Min and Max files must be integers.")
            return

        selected_folders = [self.ui.kat_widget.item(i).text() for i in range(self.ui.kat_widget.count())
                            if self.ui.kat_widget.item(i).checkState() == Qt.CheckState.Checked]

        if not selected_folders:
            QMessageBox.warning(self, "No Folders Selected", "Please select at least one folder.")
            return

        destination_dir = Path(self.ui.dkatline.text())
        if not destination_dir.is_dir():
            QMessageBox.warning(self, "Invalid Destination", "Please select a valid destination directory.")
            return

        main_dir = Path(self.ui.mkatline.text())

        try:
            for folder in selected_folders:
                folder_path = main_dir / folder
                if folder_path.is_dir():
                    # Pobieranie tylko plików .wav
                    files = list(folder_path.glob('*.wav'))
                    if not files:
                        continue

                    num_files_to_move = random.randint(min_files, min(max_files, len(files)))
                    files_to_move = random.sample(files, num_files_to_move)

                    for file in files_to_move:
                        destination_file = destination_dir / file.name

                        # Sprawdzenie, czy plik już istnieje i dodanie numeracji
                        counter = 1
                        while destination_file.exists():
                            destination_file = destination_dir / f"{file.stem}_{counter}{file.suffix}"
                            counter += 1

                        shutil.move(file, destination_file)

            QMessageBox.information(self, "Operation Complete", "WAV files have been successfully moved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
