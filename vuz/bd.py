import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout

class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджет таблицы
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Name", "Items", "Points", "City"])

        # Создаем виджеты для ввода значения "Points"
        self.points_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.load_data_from_database)

        # Создаем макет для ввода значения "Points"
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLineEdit(self.tr("Enter Points value: ")))
        input_layout.addWidget(self.points_input)
        input_layout.addWidget(self.search_button)

        # Создаем основной макет и добавляем в него таблицу и панель ввода
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.table_widget)

        # Создаем главный виджет и устанавливаем макет
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def load_data_from_database(self):
        points_value = self.points_input.text()
        with sqlite3.connect("main.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Universities WHERE Points = ?", (points_value,))
            rows = cursor.fetchall()

            self.table_widget.setRowCount(len(rows))

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table_widget.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication([])
    viewer = DatabaseViewer()
    viewer.show()
    app.exec()