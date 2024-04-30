import sys  # Sistema
from PyQt5 import QtWidgets  # PyQt


class MainForm(QtWidgets.QMainWindow):  # Classe de tela principal que herda uma classe do Qt.
    def __init__(self, parent=None):  # Construtor.
        # parent=None quer dizer que a classe não está dentro de nenhuma outra tela.
        super().__init__(parent=parent)  # O super quer dizer que vai rodar o método da classe pai.
        # Para aplicações com widgets, rodar o método init da classe pai é necessário.
        # Se não rodar, o computador não irá entender o que deve ser feito, a classe pai que sabe.

        self.label_name = QtWidgets.QLabel('Name:')  # Cria uma label.
        self.line_edit_name = QtWidgets.QLineEdit()  # Cria uma linha de texto.

        self.button_save = QtWidgets.QPushButton('Save')  # Cria um botão.
        self.button_save.clicked.connect(self.on_click_save)  # Conecta o botão com a função.

        self.message = QtWidgets.QLabel()  # Cria uma label.
        self.message.setStyleSheet('color: blue')  # Seta o style do label.
        self.message.setVisible(False)  # Diz que o label fica invisível.

        space = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        # Um item que terá 0 e 0 nos eixos
        # Mas suas 'polices' serão fixas e expandidas. Isso irá empurrar todos os Widgets para cima.

        self.vertical_layout = QtWidgets.QVBoxLayout()
        # Criando uma caixa vertical. Fará todos os itens ficarem um abaixo do outro.
        self.vertical_layout.addWidget(self.label_name)  # Adiciona o label
        self.vertical_layout.addWidget(self.line_edit_name)  # ...
        self.vertical_layout.addWidget(self.button_save)  # ...
        self.vertical_layout.addWidget(self.message)
        self.vertical_layout.addItem(space)  # Adicionando o item space como último.

        self.components = QtWidgets.QWidget()  # Cria um widget.
        self.components.setLayout(self.vertical_layout)  # Adiciona os layouts ao widget.

        self.setCentralWidget(self.components)  # Adiciona na tela o widget components.

        self.setWindowTitle('Hello, World!.')  # Método da classe pai que diz o nome que a tela terá.
        self.setGeometry(100, 100, 800, 400)  # Método da classe pai que diz o tamanho da tela.
        # X, Y, Largura, Altura

    def on_click_save(self):  # Função para mostrar algo no terminal.
        print(f'{self.line_edit_name.text()} clicked on save.')  # A variável é a que o usuário escreve.
        self.message.setText(f'Hello {self.line_edit_name.text()}')  # Coloca um texto no label.
        self.message.setVisible(True)  # Diz que o label fica visível.


app = QtWidgets.QApplication(sys.argv)  # Vai iniciar a aplicação com argumentos do sistema. Vai configurar certinho.

window = MainForm()  # Criamos a tela, com uma variável recebendo a classe.
window.show()  # Mostramos a tela.

sys.exit(app.exec_())  # Quando a tela fechar, o sistema vai fechar também.
