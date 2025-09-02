import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class ExemploIPA(toga.App):
    def startup(self):
        # Janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Conteúdo
        self.label = toga.Label("Olá, iOS 👋", style=Pack(padding=10))
        self.input = toga.TextInput(placeholder="Digite algo...", style=Pack(padding=10, flex=1))
        self.button = toga.Button("Mostrar alerta", on_press=self.on_press, style=Pack(padding=10))

        box = toga.Box(
            children=[
                self.label,
                toga.Box(children=[self.input, self.button], style=Pack(direction=ROW)),
            ],
            style=Pack(direction=COLUMN, padding=20),
        )

        self.main_window.content = box
        self.main_window.show()

    def on_press(self, widget):
        texto = self.input.value or "Nada digitado"
        self.main_window.info_dialog("Você clicou!", f"Texto: {texto}")

def main():
    return ExemploIPA("Exemplo IPA", "com.seu.bundle.exemplo-ipa")
