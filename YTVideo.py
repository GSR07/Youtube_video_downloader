from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFileDialog
from pytube import YouTube, Playlist
import os
import sys

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.initUI()

    def initUI(self):
        # Create widgets
        self.url_label = QLabel("YouTube URL:")
        self.url_input = QLineEdit()
        self.save_label = QLabel("Save Location:")
        self.save_input = QLineEdit()
        self.save_button = QPushButton("Choose Location")
        self.single_button = QPushButton("Download Single Video")
        self.playlist_button = QPushButton("Download Playlist")

        # Connect button signals
        self.save_button.clicked.connect(self.choose_save_location)
        self.single_button.clicked.connect(self.download_single_video)
        self.playlist_button.clicked.connect(self.download_playlist)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.save_label)
        layout.addWidget(self.save_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.single_button)
        layout.addWidget(self.playlist_button)
        self.setLayout(layout)

    def choose_save_location(self):
        save_location = QFileDialog.getExistingDirectory(self, "Choose Save Location")
        self.save_input.setText(save_location)

    def download_single_video(self):
        url = self.url_input.text()
        save_path = self.save_input.text()
        download_video(url, save_path)

    def download_playlist(self):
        url = self.url_input.text()
        save_path = self.save_input.text()
        download_playlist(url, save_path)

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_playlist(url, save_path):
    try:
        playlist = Playlist(url)
        for video_url in playlist.video_urls:
            download_video(video_url, save_path)
        print("Playlist downloaded successfully!")
    except Exception as e:
        print(f"Error downloading playlist: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())
