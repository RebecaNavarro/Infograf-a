import arcade
import arcade.color

from bresenham import get_line

# definicion de constantes
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Figuras Geométricas con Bresenham"


class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 5
        #Puntos para el rectangulo
        self.xr = 8
        self.yr = 8
        self.wr = 12
        self.hr = 20
        
        # Puntos para el triángulo
        self.xt = 10
        self.yt = 10
        self.base_t = 20
        self.height_t = 15

        # Puntos para el pentágono
        self.xp = 15
        self.yp = 25
        self.rp = 10
    

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        #self.draw_rectangle(self.xr, self.yr, self.wr, self.hr, arcade.color.AFRICAN_VIOLET)
        #self.draw_triangle_isosceles(self.xt, self.yt, self.base_t, self.height_t, arcade.color.ALIZARIN_CRIMSON)
        #self.draw_pentagon(self.xp, self.yp, self.rp, arcade.color.BLUE)
        self.draw_house()

    def draw_house(self):
        self.draw_rectangle(10, 10, 40, 30, arcade.color.BRICK_RED)
        self.draw_triangle_isosceles(10, 40, 40, 5, arcade.color.DARK_BROWN)
        self.draw_rectangle(25, 10, 10, 15, arcade.color.BROWN)
        self.draw_rectangle(15, 25, 10, 10, arcade.color.SKY_BLUE)


    def draw_grid(self):
        # lineas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [50, 50, 50]
            )
        #lineas horizontales
        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [50, 50, 50]
            )

    def draw_line_points(self, points,  color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)  

    def draw_rectangle(self, x, y, w, h, color):
        points0 = get_line(x,y,x+w,y) 
        self.draw_line_points(points0,color) 
        points1 = get_line(x+w,y,x+w,y+h)  
        self.draw_line_points(points1,color)
        points2 = get_line(x+w,y+h,x,y+h)  
        self.draw_line_points(points2,color)
        points3 = get_line(x,y+h,x,y)  
        self.draw_line_points(points3,color)

    def draw_triangle_isosceles(self, x, y, b, h, color):
        points0 = get_line(x, y, x+b, y)
        self.draw_line_points(points0, color)
        points1 = get_line(x, y, x + b // 2, y+h)
        self.draw_line_points(points1, color)
        points2 = get_line(x+b, y, x + b // 2, y+h)
        self.draw_line_points(points2, color)
    
    def draw_pentagon(self, x, y, r, color):
        import math
        points = []
        for i in range(5):
            angle = 2 * math.pi * i / 5
            x_i = x + int(r * math.cos(angle))
            y_i = y + int(r * math.sin(angle))
            points.append((x_i, y_i))

        for i in range(5):
            points_line = get_line(points[i][0], points[i][1], points[(i + 1) % 5][0], points[(i + 1) % 5][1])
            self.draw_line_points(points_line, color)

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()