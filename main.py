import sys
import json
import os
from PyQt6.QtWidgets import QInputDialog, QMessageBox, QApplication, QMainWindow
from ui import Ui_MainWindow  

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # потрібно викликати конструктор батьківського класу
        self.setupUi(self)

        self.notes =  # створити пустий словник для збереження заміток

        self.load_notes()

        # Підключення функцій до кнопок
        # кнопка для додавання замітки
        # кнопка для видалення замітки
        # кнопка для збереження замітки
        
        self.listWidget.itemClicked.connect(self.show_note) 

    # виправити помилку в створенні функції
    def load_notes(self)
        if os.path.exists("notes_data.json"):
            # замість ? підставити атрибут доступу для читання
            with open("notes_data.json", "?", encoding="utf-8") as file: 
                self.notes = json.load(file)  
            self.listWidget.addItems(self.notes.keys())  
        else:
            # створити вспливаюче вікно про відсутність файлу notes_data.json

    def add_note(self):
        note_name, ok = QInputDialog.getText(self, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            if note_name not in self.notes:
                self.notes[note_name] = {"текст": "", "теги": []}
                self.listWidget.addItem(note_name)  
            else:
                # створити вспливаюче вікно про повідомлення, що замітка вже існує
        else:
            # створити вспливаюче вікно про те, що замітка не може бути порожньою

    # виправити помилку в створенні функції
    def show_note():
        if self.listWidget.selectedItems():
            key = self.listWidget.selectedItems()[0].text()
            self.textEdit.setText(self.notes[key]["текст"])  
            # створити очищення спискового віджета
            self.listWidget_2.addItems(self.notes[key]["теги"])  
        else:
            # створити вспливаюче вікно про те, що вибраної замітки немає

    def save_note(self):
        # виправити помилку в умовному операторі
        if self.listWidget.selectedItems()
            key = self.listWidget.selectedItems()[0].text()
            self.notes[key]["текст"] = self.textEdit.toPlainText() 
            # замість ? підставити атрибут доступу для перезапису
            with open("notes_data.json", "?", encoding="utf-8") as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        else:
            # створити вспливаюче вікно про те, що замітка для збереження не обрана

    # виправити помилку в створенні функції
    del del_note(self):
        # написати перевірку чи обрані елементи в списковому віджеті
            key = self.listWidget.selectedItems()[0].text()
            del self.notes[key] 
            # очистити віджет зі списком заміток
            # очистити віджет текстового поля
            self.listWidget.addItems(self.notes.keys())  
            # замість ? підставити атрибут доступу для перезапису
            with open("notes_data.json", "?", encoding="utf-8") as file:
                # замість ! написати назву словника, який використовується в програмі
                json.dump("!", file)

        else:
            # створити вспливаюче вікно про те, що замітка для видалення не обрана

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = # вказати назву класу
    # "показати" вікно
    sys.exit(app.exec())
