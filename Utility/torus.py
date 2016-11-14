import math

from Utility.shape import Shape


class Torus(Shape):
    def __init__(self):
        super().__init__()
        self._u_min = 0
        self._u_max = 360
        self._v_min = 0
        self._v_max = 360

        self._a = 90
        self._b = 30

        self._u = 360
        self._v = 360

    def calculate(self):
        u = self._u * math.pi / 180
        v = self._v * math.pi / 180

        x = math.cos(u) * (self._b * math.cos(v) + self._a)
        y = math.sin(u) * (self._b * math.cos(v) + self._a)
        z = self._b * math.sin(v)
        return x, y, z
