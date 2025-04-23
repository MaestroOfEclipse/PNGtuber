import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class PNGTuberOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint |
            Qt.X11BypassWindowManagerHint  # Remove or change if not on Linux
        )
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create label for the sprite
        self.sprite_label = QLabel(self)
        self.sprite_label.setAlignment(Qt.AlignCenter)

        # Position and size
        self.setFixedSize(300, 300)
        self.move(100, 100)

        # Mouse dragging
        self.dragging = False
        self.offset = None

    def loadSprite(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.sprite_label.setPixmap(scaled_pixmap)
        self.sprite_label.resize(self.size())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging and self.offset:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.dragging = False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    overlay = PNGTuberOverlay()
    overlay.move(0, 0)
    overlay.show()

    # Load the first sprite manually
    overlay.loadSprite("a.png")

    counter = 0
    # Example: change sprite after 2 seconds (for demo purposes)
    def update_sprite():
        global counter
        print(counter)
        if counter % 10 == 0:
            overlay.loadSprite("b.png")
        else:
            overlay.loadSprite("a.png")
        counter += 1

    # Run every 100 ms
    timer = QTimer()
    timer.timeout.connect(update_sprite)
    timer.start(1)
    sys.exit(app.exec_())
