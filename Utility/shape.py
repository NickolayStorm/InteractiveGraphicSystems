import math

from Utility.structures import HomogeneousPoint

DEFAULT_PARAMETER = 50
DEFAULT_STEP = 20
DEFAULT_MAX_VALUE = 200


class Shape:
    def __init__(self):
        # Дополнительные параметры фигуры (сжатие, растяжение и тд)
        self._a, self._b, self._c = DEFAULT_PARAMETER, DEFAULT_PARAMETER, DEFAULT_PARAMETER
        # Шаг сетки
        self._u_step, self._v_step = DEFAULT_STEP, DEFAULT_STEP
        # Минимальное и максимальное значения
        self._u_min, self._v_min = 0, 0
        self._u_max, self._v_max = DEFAULT_MAX_VALUE, DEFAULT_MAX_VALUE

        # Параметры фигуры
        self._u = 0
        self._v = 0

    def calculate(self):
        """
        Возвращает новую точку поверхности
        :return: int x, int y, int z
        """
        pass

    def homogeneous_point(self, i, j):
        """
        Формирует и возвращает точку в однородных координатах.
        :return: HomogeneousPoint
        """
        self._u = self._u_min + i/(self._u_step - 1) * (self._u_max - self._u_min)
        self._v = self._v_min + j/(self._v_step - 1) * (self._v_max - self._v_min)
        x, y, z = self.calculate()
        return HomogeneousPoint(x, y, z)

    def set_params(self, a, b, u_max, v_max):
        self._a = a
        self._b = b
        self._u_max = u_max
        self._v_max = v_max

    def set_steps(self, u_step, v_step):
        self._u_step = u_step
        self._v_step = v_step

    def get_limits(self):
        return {'u_max': self._u_max,
                'u_min': self._u_min,
                'v_max': self._v_max,
                'v_min': self._v_min}

    def get_params(self):
        return {'u': self._u,
                'v': self._v,
                'a': self._a,
                'b': self._b}


