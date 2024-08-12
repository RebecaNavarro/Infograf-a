import arcade
import arcade.color

# globales
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_TITLE = "hola arcade"

class HelloWindow(arcade.Window):
    def __init__(self, width, height, title):
        # iniciar el padre
        super().__init__(width, height, title)
        # fondo:
        arcade.set_background_color(arcade.color.AMETHYST)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_ellipse_outline(200,200,100,70, arcade.color.AERO_BLUE,3)

window = HelloWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

arcade.run()
