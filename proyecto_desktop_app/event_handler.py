from PyQt6.QtWidgets import QMessageBox


def handle_closeEvent(self, event):
    # Verificar si se han guardado los datos
    if not self.has_saved_data():
        # Mostrar un cuadro de diálogo de confirmación antes de cerrar
        reply = QMessageBox.question(
            self,
            "Guardar",
            "No has guardado los cambios. ¿Deseas guardar antes de cerrar?",
            QMessageBox.StandardButton.Save
            | QMessageBox.StandardButton.Discard
            | QMessageBox.StandardButton.Cancel,
        )

        if reply == QMessageBox.StandardButton.Save:
            self.save_file()
        elif reply == QMessageBox.StandardButton.Cancel:
            event.ignore()
            return

    event.accept()
