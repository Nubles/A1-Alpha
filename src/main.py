import sys
import mss
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Screen Capture App")
        self.setGeometry(100, 100, 800, 600)

        # Main layout and widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Image display label
        self.image_label = QLabel("Click 'Capture Screen' to start.")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # A fixed size for the capture area, can be adjusted
        self.image_label.setFixedSize(640, 480)
        layout.addWidget(self.image_label)

        # Capture button
        self.capture_button = QPushButton("Capture Screen")
        self.capture_button.clicked.connect(self.capture_screen)
        layout.addWidget(self.capture_button)

    def capture_screen(self):
        # Define the capture area (top, left, width, height)
        # This is a hardcoded region for now.
        monitor = {"top": 40, "left": 0, "width": 640, "height": 480}

        with mss.mss() as sct:
            # Grab the data
            sct_img = sct.grab(monitor)

            # Create a QImage from the raw MSS data
            img = QImage(sct_img.rgb, sct_img.width, sct_img.height, QImage.Format.Format_RGB888)

            # Create a QPixmap from the QImage
            pixmap = QPixmap.fromImage(img)

            # Set the pixmap on the label
            self.image_label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
