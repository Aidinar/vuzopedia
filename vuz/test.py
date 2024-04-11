# import sys ВСПЛЫВАЮШИЕ СТРОКИ
# from PyQt6.QtWidgets import QApplication, QWidget, QComboBox

# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Combo box')

#         combo = QComboBox(self)
#         combo.addItem('Python')
#         combo.addItem('Java')
#         combo.addItem('C++')
#         combo.move(50, 50)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     ex.show()
#     sys.exit(app.exec())




# import sys ТАБЛИЦА
# from PyQt6.QtGui import QStandardItem, QStandardItemModel
# from PyQt6.QtWidgets import QApplication, QTreeView, QWidget, QVBoxLayout
 
# class TreeViewExample(QWidget):
#     def __init__(self):
#         super().__init__()
 
#         # Set up the window
#         self.setWindowTitle("QTreeView Example")
#         self.setGeometry(100, 100, 400, 400)
 
#         # Create the model and set up some data
#         self.model = QStandardItemModel()
#         self.model.setHorizontalHeaderLabels(["Name", "Age"])
#         self.root_node = self.model.invisibleRootItem()
#         for name, age in [("Geekscoders", 25), ("Bob", 30), ("John", 35)]:
#             parent = QStandardItem(name)
#             parent.appendRow([QStandardItem(name), QStandardItem(str(age))])
#             self.root_node.appendRow(parent)
 
#         # Create the tree view and set the model
#         self.tree_view = QTreeView()
#         self.tree_view.setModel(self.model)
#         self.tree_view.setEditTriggers(QTreeView.EditTrigger.NoEditTriggers)  # Prevent editing of items
 
#         # Set up the layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.tree_view)
#         self.setLayout(layout)
 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = TreeViewExample()
#     window.show()
#     sys.exit(app.exec())






# import sys  ВЫВОД ДАННЫХ ИЗ INPUT
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout
# from PyQt6.QtGui import QFont
 
# class SpinExample(QWidget):
#     def __init__(self):
#         super().__init__()
 
#         # Set window properties
#         self.setWindowTitle('QSpinBox - Geekscoders.com')
#         self.setGeometry(100, 100, 400, 200)
 
#         # Create QSpinBox widget
#         self.spin_box = QSpinBox()
#         self.spin_box.setMinimum(1)
#         self.spin_box.setMaximum(10)
#         self.spin_box.setSingleStep(1)
#         self.spin_box.setValue(5)
 
#         # Create QLabel widget
#         self.label = QLabel()
 
#         # Create layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.spin_box)
#         layout.addWidget(self.label)
 
#         # Set layout
#         self.setLayout(layout)
 
#         # Connect signals to slots
#         self.spin_box.valueChanged.connect(self.on_spin_box_value_changed)
 
#     def on_spin_box_value_changed(self, value):
#         self.label.setText(f'Value selected: {value}')
#         self.label.setFont(QFont("Times", 15))
 
# if __name__ == '__main__':
#     # Create application object
#     app = QApplication(sys.argv)
 
#     # Create window object
#     window = SpinExample()
 
#     # Show window
#     window.show()
 
#     # Run event loop
#     sys.exit(app.exec())

from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 500, 400)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
 
 
    # method for components
    def UiComponents(self):
 
        # creating a QListWidget
        list_widget = QListWidget(self)
 
        # setting geometry to it
        list_widget.setGeometry(50, 70, 150, 80)
 
        # list widget items
        item1 = QListWidgetItem("PyQt5 Geeks for Geeks")
        item2 = QListWidgetItem("B")
        item3 = QListWidgetItem("C")
        item4 = QListWidgetItem("D")
 
        # adding items to the list widget
        list_widget.addItem(item1)
        list_widget.addItem(item2)
        list_widget.addItem(item3)
        list_widget.addItem(item4)
 
        # scroll bar
        scroll_bar = QScrollBar(self)
 
        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet("background : lightgreen;")
 
        # setting vertical scroll bar to it
        list_widget.setVerticalScrollBar(scroll_bar)
 
        # creating a label
        label = QLabel("GeeksforGeeks", self)
 
        # setting geometry to the label
        label.setGeometry(230, 80, 280, 80)
 
        # making label multi line
        label.setWordWrap(True)
 
 
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())