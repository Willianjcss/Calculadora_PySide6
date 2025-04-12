from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


# Aqui agente sobre escreve nossa QMainWindow do módulo PySide adicionando
# e configurando funções e métodos para facilitar na hora da utilização
# no main.py
class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
# Layout vertical , que organiza os elementos em uma pilha (um abaixo do outro)
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Última coisa a ser feita
        # Ajusta automaticamente o tamanho da janela com base no conteúdo
        self.adjustSize()
        # Define o tamanho ajustado como fixo, impedindo redimensionamento
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
