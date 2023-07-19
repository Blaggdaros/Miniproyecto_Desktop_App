import sys

from about_dialog import show_about_dialog
from event_handler import handle_closeEvent

# from confirm_dialog import show_confirm_dialog
from file_manager import create_new_file, open_file, save_file
from PyQt6.QtCore import QCoreApplication, Qt, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from render import render_markdown


class MarkdownEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Markdown Editor")

        # Editor de texto
        self.text_edit = QPlainTextEdit()
        self.text_edit.setPlaceholderText("Introduce tu Markdown")
        self.text_edit.textChanged.connect(self.set_unsaved_changes)

        # Botón para renderizar
        self.render_button = QPushButton("Render Markdown")
        self.render_button.clicked.connect(self.render_markdown)

        # Widget QWebEngineView para mostrar el contenido renderizado
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("about:blank"))

        # Variable para controlar los cambios sin guardar
        self.unsaved_changes = False

        # Organización ventanas
        layout = QHBoxLayout()
        layout.addWidget(self.text_edit)

        layout.addWidget(self.render_button)
        side_panel = QVBoxLayout()
        layout.addLayout(side_panel)
        layout.addWidget(self.web_view)

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)

        self.setCentralWidget(self.central_widget)
        # Barra de menú
        self.menu_bar = self.menuBar()

        # Menú "File"
        self.file_menu = self.menu_bar.addMenu("File")

        # Acciones del menú "File"
        self.new_action = self.file_menu.addAction("New")
        self.new_action.triggered.connect(self.new_file)

        self.open_action = self.file_menu.addAction("Open")
        self.open_action.triggered.connect(self.open_file)

        self.save_action = self.file_menu.addAction("Save")
        self.save_action.triggered.connect(self.save_file)

        self.close_action = self.file_menu.addAction("Close")
        self.close_action.triggered.connect(self.close_app)

        # Menú "Help"
        self.help_menu = self.menu_bar.addMenu("Help")

        # Acción "About"
        self.about_action = self.help_menu.addAction("About")
        self.about_action.triggered.connect(show_about_dialog)

        # Acción "Close"
        self.close_action = self.file_menu.addAction("Close")
        self.close_action.triggered.connect(self.close)

    def set_unsaved_changes(self):
        self.unsaved_changes = True

    def render_markdown(self):
        markdown_text = self.text_edit.toPlainText()
        try:
            html = render_markdown(markdown_text)
            # Cargar el contenido HTML en el QWebEngineView
            self.web_view.setHtml(html)
        except Exception as e:
            # Manejar el error y proporcionar una respuesta al usuario
            error_message = f"Error al renderizar el Markdown: {str(e)}"
            self.web_view.setHtml(f"<p>{error_message}</p>")

    def new_file(self):
        if self.unsaved_changes:
            result = show_confirm_dialog()
            if result == QMessageBox.StandardButton.Save:
                self.save_file()
            elif result == QMessageBox.StandardButton.Cancel:
                return
        create_new_file()
        self.text_edit.clear()
        self.unsaved_changes = False

    def open_file(self):
        if self.unsaved_changes:
            result = show_confirm_dialog()
            if result == QMessageBox.StandardButton.Save:
                self.save_file()
            elif result == QMessageBox.StandardButton.Cancel:
                return
        content = open_file()
        if content is not None:
            self.text_edit.setPlainText(content)
            self.unsaved_changes = False

    def save_file(self):
        content = self.text_edit.toPlainText()
        save_file(content)
        self.unsaved_changes = False

    def close_app(self):
        if self.unsaved_changes:
            result = show_confirm_dialog()
            if result == QMessageBox.StandardButton.Save:
                self.save_file()
            elif result == QMessageBox.StandardButton.Discard:
                self.unsaved_changes = False
            else:
                return
        QCoreApplication.quit()

    def closeEvent(self, event):
        handle_closeEvent(self, event)

    def has_saved_data(self):
        # Verificar si el contenido actual coincide con el contenido guardado previamente
        current_content = self.text_edit.toPlainText()

        # Por ahora, se asume que no se ha guardado si el contenido está vacío
        return len(current_content.strip()) == 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("./css/style.css", "r") as file:
        style_sheet = file.read()
        # Aplicar estilo de archivo CSS a la aplicación
        app.setStyleSheet(style_sheet)
    window = MarkdownEditor()
    window.show()
    sys.exit(app.exec())
