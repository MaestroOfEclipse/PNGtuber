import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import time

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
        
        # Load default image
        #self.load_sprite("default.png")  # Your test image
        
        # Position and size
        self.setFixedSize(300, 300)
        self.move(100, 100)
        
        # Mouse dragging
        self.dragging = False
        self.offset = None

    def load_sprite(self, image_path):
        pixmap = QPixmap(image_path)

        # Scale the pixmap to fit the widget size
        scaled_pixmap = pixmap.scaled(
            self.size(),  # scale to widget size (300x300)
            Qt.KeepAspectRatio,  # maintain aspect ratio
            Qt.SmoothTransformation  # smooth scaling
        )

        self.sprite_label.setPixmap(scaled_pixmap)
        self.sprite_label.resize(self.size())  # match label size to widget


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
    
    SpritePaths = ["a.png"]
    sprites = []
    
    for i, SpritePath in enumerate(SpritePaths):
        overlay = PNGTuberOverlay()
        overlay.load_sprite(SpritePath)
        #overlay.move(100 + i*320, 100)  # Spread out horizontally
        overlay.move(0,0)
        overlay.show()
        sprites.append(overlay)
    spr=sprites[0]

    sys.exit(app.exec_())
    
    