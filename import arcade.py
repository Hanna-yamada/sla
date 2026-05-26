import arcade
ALTURA=600
LARGURA=800
TITULO=" P"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("pngegg.png", scale=0.3)
        self.textuta_direita = arcade.load_texture("pngegg.png")
        self.textuta_esquerda = arcade.load_texture("pngeggg.png")
    def update(self):
        pass


class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(800,600," p")
        arcade.set_background_color(arcade.color.AMAZON)

        self.personagem = Player()
        self.personagem.center_x= 400
        self.personagem.center_y= 300

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.personagem)

    def on_update(self, delta_time):
        pass

def sla():
    tela = JanelaJogo()
    arcade.run()

if __name__=="__main__":                       
    sla()