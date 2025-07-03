# movies_module.py
# Este módulo define la clase MovieListPage, que implementa un listado de películas
# usando un QTableWidget con data de prueba. La grilla está configurada para que
# no permita ordenar, editar ni autoajustar sus columnas. Además, se aplica un estilo dark.

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QFrame, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize


class MovieListPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        # Se crea un layout vertical para contener la grilla.
        layout = QVBoxLayout(self)

        # Search Bar
        # En la parte superior se agrega un QFrame que actúa como contenedor de la Search Bar.
        self.searchBarFrame = QFrame()
        self.searchBarFrame.setStyleSheet(""" 
        QFrame {
            background-color: rgb(39, 44, 54);
            border: 1px solid rgb(52, 59, 72);
            border-radius: 5px;}
        QLabel {
            color: rgb(210, 210, 210);
            }""")

        # Dentro del QFrame se coloca un QHBoxLayout que contiene el QLineEdit (con placeholder "Title") y el QPushButton (con el ícono search).

        # Parametros layout barra
        searchBarLayout = QHBoxLayout(self.searchBarFrame)
        searchBarLayout.setContentsMargins(100, 100, 10, 10)
        searchBarLayout.setSpacing(10)

        # Parametros texto barra y estilos
        # El QLineEdit permite ingresar el texto a buscar.
        self.titleEdit = QLineEdit()
        self.titleEdit.setPlaceholderText("Title")
        self.titleEdit.setStyleSheet("""
        QLineEdit {
            background-color: rgb(0, 0, 0);
            border-radius: 5px;
            border: 2px solid rgb(27, 29, 35);
            padding-left: 10px;
            color: rgb(210, 210, 210);
            height: 30px;
            }
        QLineEdit:hover {
            border: 2px solid rgb(64, 71, 88);
            }
        QLineEdit:focus {
            border: 2px solid rgb(91, 101, 124);
            }""")

        self.searchButton = QPushButton("Search")
        self.searchButton.setIcon(QIcon("icons/16x16/cil-zoom-in.png"))
        self.searchButton.setStyleSheet("""
        QPushButton {
            border: 2px solid rgb(52, 59, 72);
            border-radius: 5px;
            background-color: rgb(52, 59, 72);
            color: rgb(210, 210, 210);
            padding: 5px 10px;
            }
        QPushButton:hover {
            background-color: rgb(57, 65, 80);
            border: 2px solid rgb(61, 70, 86);
            }
        QPushButton:pressed {
            background-color: rgb(35, 40, 49);
            border: 2px solid rgb(43, 50, 61);
            }""")

        self.searchButton.clicked.connect(self.onSearchBasic)

        searchBarLayout.addWidget(self.titleEdit)
        searchBarLayout.addWidget(self.searchButton)
        layout.addWidget(self.searchBarFrame)

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
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        # Deshabilitar el autoajuste de las columnas: usar un modo Fixed y establecer ancho manualmente.
        # Se configura cada columna con un ancho fijo.
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeMode.Fixed)
        self.table.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(0, 300)  # Columna Title
        self.table.setColumnWidth(1, 100)  # Columna Year
        self.table.setColumnWidth(2, 100)  # Columna Duration

        # Aplicar estilo dark a la grilla
        self.table.setStyleSheet("""
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
            }""")

        # Agregar la grilla al layout
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Cargar datos de prueba hardcode
        self.loadMovies()

    def getMoviesFromDB(self):
        data = [
            {"title": "The Shawshank Redemption",
                "year": 1994, "duration": 142},
            {"title": "The Godfather", "year": 1972, "duration": 175},
            {"title": "The Dark Knight", "year": 2008, "duration": 152},
            {"title": "Pulp Fiction", "year": 1994, "duration": 154}
            ]
        return data

    def loadMovies(self, movies=None):
        if movies is None:
            movies = self.getMoviesFromDB()

        # Establecer el número de filas según la cantidad de registros
        self.table.setRowCount(len(movies))

        # Iterar sobre cada registro y crear items en la grilla
        for row, movie in enumerate(movies):
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

    def onSearchBasic(self):
        title_text = self.titleEdit.text().lower()
        if not title_text:
            self.loadMovies()   #Si esta vacio, devuelve todas las peliculas
            return
        
        movies = self.getMoviesFromDB()
        filtered = [movies for movie]
        self.loadMovies(filtered)


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
