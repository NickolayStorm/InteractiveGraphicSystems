from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPainterPath, QPolygonF
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPoint


class ShapeView(QWidget):
    def __init__(self, parent=None):
        super(ShapeView, self).__init__(parent)
        self.polygons = []

    def paintEvent(self, event):
        if self.polygons:
            painter = QPainter(self)

            # painter.drawEllipse(0, 0, self.width()/2, self.width()/2)
            for (pa, pb, pc), color in self.polygons:
                a = QPoint(pa.x, pa.y)
                b = QPoint(pb.x, pb.y)
                c = QPoint(pc.x, pc.y)

                pen = QPen()

                if color:
                    pen.setColor(color)
                else:
                    pen.setColor(QColor(0, 0, 0))

                painter.setPen(pen)

                polygon = QPolygonF([a, b, c])

                painter.drawPolygon(polygon)

                if color:
                    path = QPainterPath()
                    path.addPolygon(polygon)

                    # painter.setBrush(QBrush(color))
                    painter.fillPath(path, QBrush(color))
                # print(pa, pb, pc)


    def set_polygons(self, polygons):
        self.polygons = polygons