import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QLabel, QStackedWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Planner App")
        self.setMinimumSize(700, 400)

        # ----- Sidebar -----
        self.sidebar = QVBoxLayout()

        self.btn_tasks = QPushButton("Tasks")
        self.btn_pomodoro = QPushButton("Pomodoro")
        self.btn_spotify = QPushButton("Spotify")

        for btn in (self.btn_tasks, self.btn_pomodoro, self.btn_spotify):
            btn.setFixedHeight(40)
            self.sidebar.addWidget(btn)

        self.sidebar.addStretch()

        # ----- Pages -----
        self.pages = QStackedWidget()

        # Tasks Page
        self.page_tasks = QLabel("Tasks Page")
        self.page_tasks.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Pomodoro Page
        self.page_pomodoro = QLabel("Pomodoro Timer Page")
        self.page_pomodoro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Spotify Page
        self.page_spotify = QLabel("Spotify Integration Page")
        self.page_spotify.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add pages
        self.pages.addWidget(self.page_tasks)
        self.pages.addWidget(self.page_pomodoro)
        self.pages.addWidget(self.page_spotify)

        # Button signals
        self.btn_tasks.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        self.btn_pomodoro.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.btn_spotify.clicked.connect(lambda: self.pages.setCurrentIndex(2))

        # ----- Layout -----
        layout = QHBoxLayout()
        layout.addLayout(self.sidebar)
        layout.addWidget(self.pages)

        self.setLayout(layout)
class WeeklyPlanner(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title label
        self.week_label = QLabel()
        layout.addWidget(self.week_label)

        # List of days
        self.days_list = QListWidget()
        layout.addWidget(self.days_list)

        self.update_week()

    def get_week(self):
        today = datetime.date.today()
        start = today - datetime.timedelta(days=today.weekday())
        end = start + datetime.timedelta(days=6)
        week_days = [(start + datetime.timedelta(days=i)) for i in range(7)]
        return start, end, week_days

    def update_week(self):
        start, end, days = self.get_week()

        self.week_label.setText(f"This Week: {start} → {end}")

        for day in days:
            self.days_list.addItem(day.strftime("%A — %B %d"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
