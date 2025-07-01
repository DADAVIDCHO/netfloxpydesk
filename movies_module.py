# movies_module.py
# Este módulo define la clase MovieListPage, que implementa un listado de películas
# usando un QTableWidget con data de prueba. La grilla está configurada para que
# no permita ordenar, editar ni autoajustar sus columnas. Además, se aplica un estilo dark.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt, QSize


class MovieListPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
        
    def setupUI(self):
        # Se crea un layout vertical para contener la grilla.
        layout = QVBoxLayout(self)
        
        # Crear el QTableWidget con 3 columnas
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Title", "Year", "Duration"])
        
        # Configurar la grilla:
        # - Deshabilitar edición (NoEditTriggers)
        # - Deshabilitar ordenamiento
        # - Selección de filas única
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSortingEnabled(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        
        # Deshabilitar el autoajuste de las columnas: usar un modo Fixed y establecer ancho manualmente.
        # Se configura cada columna con un ancho fijo.
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(0, 300)  # Columna Title
        self.table.setColumnWidth(1, 100)  # Columna Year
        self.table.setColumnWidth(2, 100)  # Columna Duration
        
        # Aplicar estilo dark a la grilla
        style = """ 
        QTableWidget {
            background-color: rgb(39, 44, 54);
            padding: 10px;
            border-radius: 5px;
            gridline-color: rgb(44, 49, 60);
            border-bottom: 1px solid rgb(44, 49, 60);
            color: rgb(210, 210, 210);
            }
        QTableWidget::item:selected {
            background-color: rgb(85, 170, 255);
            }
        QHeaderView::section {
            background-color: rgb(27, 29, 35);
            border: 1px solid rgb(44, 49, 60);
            color: rgb(210, 210, 210);
            padding: 4px;
            }"""
        self.table.setStyleSheet(style)
        
        # Agregar la grilla al layout
        layout.addWidget(self.table)
        #self.setLayout(layout)
        
        # Cargar datos de prueba hardcode
        self.loadData()
    
    def loadData(self):
        # Lista de diccionarios con datos de prueba
        data = [
            {"title": "The Shawshank Redemption", "year": 1994, "duration": 152},
            {"title": "The Shawshank Redemption 2", "year": 1993, "duration": 132},
            {"title": "The Shawshank Redemption 3", "year": 1992, "duration": 142},
            {"title": "The Shawshank Redemption 4", "year": 1991, "duration": 122},
        ]
        
        # Establecer el número de filas según la cantidad de registros
        self.table.setRowCount(len(data))
        
        # Iterar sobre cada registro y crear items en la grilla
        for row, movie in enumerate(data):
            # Crear items para cada columna
            itemTitle = QTableWidgetItem(movie["title"])
            itemYear = QTableWidgetItem(str(movie["year"]))
            itemDuration = QTableWidgetItem(f'{movie["duration"]} min')
            
            # Opcional: alinear el texto de Year y Duration al centro
            itemYear.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            itemDuration.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # Insertar los items en la grilla
            self.table.setItem(row, 0, itemTitle)
            self.table.setItem(row, 1, itemYear)
            self.table.setItem(row, 2, itemDuration)

# Si se desea probar este módulo de forma independiente:
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    # Crear una instancia de MovieListPage
    window = MovieListPage()
    window.resize(QSize(600, 400))
    window.show()
    sys.exit(app.exec())