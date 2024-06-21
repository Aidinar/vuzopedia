import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QGroupBox, QScrollArea

class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_data_from_database()

    def initUI(self):
        self.setWindowTitle("Database Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Виджеты
        self.label = QLabel("Введите балл:")
        self.points_input = QLineEdit()
        self.search_button = QPushButton("Поиск")
        self.search_button.clicked.connect(self.load_data_from_database)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.points_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.scroll_area)

        # Главный виджет
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def load_data_from_database(self):
        points_value = self.points_input.text()
        with sqlite3.connect("main.db") as db:
            cursor = db.cursor()

            # Фильтрация данных по баллам
            if points_value:
                cursor.execute("SELECT * FROM Universities WHERE Points >= ?", (points_value,))
            else:
                cursor.execute("SELECT * FROM Universities")
            rows = cursor.fetchall()

            # Очищаем предыдущее содержимое
            for i in reversed(range(self.content_layout.count())):
                self.content_layout.itemAt(i).widget().deleteLater()

            # Добавляем новые блоки с данными
            for row in rows:
                group_box = QGroupBox(f"ID: {row[0]} | Univer: {row[1]}")
                group_box_layout = QVBoxLayout(group_box)
                group_box_layout.addWidget(QLabel(f"Items: {row[2]}"))
                group_box_layout.addWidget(QLabel(f"Points: {row[3]}"))
                group_box_layout.addWidget(QLabel(f"City: {row[4]}"))
                group_box.setStyleSheet("background-color: #f0f0f0; border: 2px solid #e0e0e0; border-radius: 5px; padding: 10px;")
                group_box_layout.setSpacing(10)
                self.content_layout.addWidget(group_box)

            self.scroll_area.setWidget(self.content_widget)

if __name__ == "__main__":
    app = QApplication([])
    viewer = DatabaseViewer()
    viewer.show()
    app.exec()