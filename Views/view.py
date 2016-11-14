from PyQt5.QtWidgets import QWidget, QMainWindow, QSizePolicy
from Views.shapeview import ShapeView
from PyQt5.uic import loadUi
import sys

from Views.slider import SliderWithValues


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Views/ui/form3.ui", self)

        self.shape_view = ShapeView(self)
        size = self.widget_draw.size()
        self.horizontalLayout.replaceWidget(self.widget_draw, self.shape_view)
        # self.gridLayout.replaceWidget(self.widget, self.shape_view)
        # self.shape_view.resize(size)
        # self.drawing_view = self.shape_view
        self.shape_view.resize(size)
        print(self.shape_view.size())
        self.shape_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)