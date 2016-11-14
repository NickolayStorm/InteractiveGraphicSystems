from PyQt5.QtWidgets import QSlider, QApplication, QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPainter, QPen, QFontMetrics
from PyQt5.QtCore import Qt, QPoint, QRect


class SliderWithValues(QSlider):
    def __init__(self, parent=None):
        super(SliderWithValues, self).__init__(parent)

        print(self.getContentsMargins())

        self.setStyleSheet("""
        QSlider::groove:horizontal {
            border: 1px solid #bbb;
            background: white;
            height: 10px;
            border-radius: 4px;
        }

        QSlider::sub-page:horizontal {
            background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                stop: 0 #66e, stop: 1 #bbf);
            background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                stop: 0 #bbf, stop: 1 #55f);
            border: 1px solid #777;
            height: 10px;
            border-radius: 4px;
        }

        QSlider::add-page:horizontal {
            background: #fff;
            border: 1px solid #777;
            height: 10px;
            border-radius: 4px;
        }

        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #eee, stop:1 #ccc);
            border: 1px solid #777;
            width: 13px;
            margin-top: -2px;
            margin-bottom: -2px;
            border-radius: 4px;
        }

        QSlider::handle:horizontal:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 #fff, stop:1 #ddd);
            border: 1px solid #444;
            border-radius: 4px;
        }

        QSlider::sub-page:horizontal:disabled {
            background: #bbb;
            border-color: #999;
        }

        QSlider::add-page:horizontal:disabled {
            background: #eee;
            border-color: #999;
        }

        QSlider::handle:horizontal:disabled {
            background: #eee;
            border: 1px solid #aaa;
            border-radius: 4px;
        }
        """)

    def paintEvent(self, event):
        QSlider.paintEvent(self, event)

        painter = QPainter(self)
        painter.setPen(QPen(Qt.black))

        font_metrics = QFontMetrics(self.font())
        font_width = font_metrics.boundingRect(str(self.value())).width()
        font_height = font_metrics.boundingRect(str(self.value())).height()

        # self.geometry().setHeight(self.geometry().height()*6)

        rect = self.geometry()

        if self.orientation() == Qt.Horizontal:
            horizontal_x_pos = rect.width() / 2 - font_width/2
            horizontal_y_pos = rect.height() * 0.15 # + font_height/2

            painter.drawText(QPoint(horizontal_x_pos, horizontal_y_pos), str(self.value()))

        painter.drawRect(rect)


if __name__ == '__main__':
    app = QApplication([])

    win = QWidget()
    win.setWindowTitle('Test Slider with Text')
    win.setMinimumSize(600, 400)
    layout = QVBoxLayout()
    win.setLayout(layout)

    sliderWithValue = SliderWithValues(Qt.Horizontal)
    sliderWithValue.setMinimum(0.0)
    sliderWithValue.setMaximum(100)
    sliderWithValue.setTickInterval(1)
    sliderWithValue.setSingleStep(2)
    sliderWithValue.setPageStep(5)
    sliderWithValue.setTickPosition(QSlider.TicksBelow)
    sliderWithValue.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    sliderWithValue.setValue(100)

    layout.addWidget(sliderWithValue)

    win.show()
    app.exec_()




