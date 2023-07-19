from PyQt6.QtWidgets import QMessageBox


def show_about_dialog():
    about_text = """
        <h1>Acerca de la aplicación</h1>
        <p>Esta es una aplicación de edición de Markdown.</p>
        <p>Desarrollado por: Blaggdaros</p>
    """
    QMessageBox.about(None, "Acerca de", about_text)
