from PyQt5.QtWidgets import QApplication, QColorDialog

from Views.view import View
from Models.model import Model
from Utility.structures import HomogeneousPoint
from Utility.torus import Torus
from Utility.shell import Shell
from Controllers.controller import Controller

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()

    u_step = 20
    v_step = 20

    observer = HomogeneousPoint(view.slider_observer_x.value(),
                                view.slider_observer_y.value(),
                                view.slider_observer_z.value())
    shape = Torus()
    # shape = Shell()

    model = Model(height=view.widget_draw.height(),
                  width=view.widget_draw.width(),
                  u_step=u_step,
                  v_step=v_step,
                  shape=shape,
                  observer=observer)

    controller = Controller(model=model, view=view)

    app.exec_()
