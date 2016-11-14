import math

from Utility.shape import Shape


class Shell(Shape):
    def __init__(self):
        super().__init__()
        self._u_min = 0
        self._u_max = 1800  # 1440
        self._v_min = 0
        self._v_max = 360

        self._a = 90
        self._b = 30

        self._u = 1800
        self._v = 360

    def calculate(self):
        u = self._u * math.pi / 180
        v = self._v * math.pi / 180

        x = u * math.cos(u) * (math.cos(v) + self._b/10)
        y = u * math.sin(u) * (math.cos(v) + self._b/10)
        z = u * math.sin(v) - (math.pi * (u + 7) / (self._a/10 + 1) ) ** 2 + 100
        return x, y, z

