import arcade
import numpy as np
import random
from game_object import Object3D

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Projeccion 3d"


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.cube = Object3D(
            [
                (6, 8, 0),
                (6, 0, 0),
                (0, -5, 0),
                (-6, 0, 0),
                (-6, 8, 0),
                (0, 5, 0),
                (2, 0, 0),
                (3, 0, 0),
                (2, -1, 0),
                (-2, 0, 0),
                (-3, 0, 0),
                (-2, -1, 0),
            ],
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 0),
                (0, 2),
                (4, 2),
                (3, 1),
                (1, 5),
                (5, 3),
                (6, 8),
                (6, 7),
                (8, 7),
                (9, 10),
                (9, 11),
                (10, 11),
            ],
            arcade.color.ORANGE_RED
        )
        self.cube.translate(399, 399, 0)
        self.cube.scale(50, 50, 50)
        #self.cube.rotate(-0.3, "x")
        #self.cube.rotate(0.3, "y")
        # self.cube.rotate(0.7, "z")
    
    def on_update(self, delta_time: float):
        pass
        #self.cube.rotate(delta_time, "y")
        
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        rotation_speed = 0.01  # Factor de escala para la rotación
        self.cube.rotate(dx * rotation_speed, "x")
        self.cube.rotate(dy * rotation_speed, "y")

    def on_draw(self):
        arcade.start_render()
        self.cube.draw()
    
if __name__ == "__main__":
    app = App()
    arcade.run()