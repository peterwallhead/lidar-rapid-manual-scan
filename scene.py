from ast import Try
import math

from PIL import Image, ImageDraw


class Frame:
    def __init__(self, data, scale):
        self._data = data
        self._frame_coordinates = []
        self._scale = scale

    def plot(self):
        self._minimum_relative_x = 0
        self._maximum_relative_x = 0
        self._minimum_relative_y = 0
        self._maximum_relative_y = 0
        
        for angle_str, distance_float in self._data:
            try:
                angle = int(float(angle_str))
                distance = int(distance_float)

                if distance != 0:
                    relative_x = distance * math.sin(math.radians(angle))
                    relative_y = distance * math.cos(math.radians(angle))

                    self._frame_coordinates.append((relative_x, relative_y))

                    if relative_x < self._minimum_relative_x:
                        self._minimum_relative_x = int(relative_x)
                    elif relative_x > self._maximum_relative_x:
                        self._maximum_relative_x = int(relative_x)

                    if relative_y < self._minimum_relative_y:
                        self._minimum_relative_y = int(relative_y)
                    elif relative_y > self._maximum_relative_y:
                        self._maximum_relative_y = int(relative_y)
            except:
                continue

    def _draw_dot(self, drawing, dot_position, dot_colour = 'green'):
        dot_size = 30 * self._scale
        drawing.ellipse((dot_position[0] - dot_size, dot_position[1] - dot_size,
            dot_position[0] + dot_size, dot_position[1] + dot_size), fill=dot_colour)
    
    def draw(self, data = None, filepath = 'output/', filename = 'frame', dot_colour = 'green'):
        filename = str(filename)

        if data is None:
            data = self._frame_coordinates

        self._img_width = 12000
        self._img_height = 12000

        self._img_width_scaled = int(12000 * self._scale)
        self._img_height_scaled = int(12000 * self._scale)
        
        image = Image.new('RGBA', (self._img_width_scaled, self._img_height_scaled), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        for frame_coordinate in data:
            self._draw_dot(draw, ((frame_coordinate[0] + (self._img_width // 2)) * self._scale, ((self._img_height // 2) - frame_coordinate[1]) * self._scale), dot_colour)            

        image.save(f'{filepath}{filename}.png', 'PNG')
        #image.show()

    @property
    def frame_coordinates(self):
        return self._frame_coordinates
