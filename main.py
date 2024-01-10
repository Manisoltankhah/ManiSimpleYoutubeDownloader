import sys
import yt_dlp
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.youtube.com/'))
        self.setWindowIcon(QtGui.QIcon('D:\\YtDl\\YTdownloader.png'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        if os.path.isdir('Mani YDL Downloaded Files'):
            pass
        else:
            os.mkdir("Mani YDL Downloaded Files")

        navbar = QToolBar()
        self.addToolBar(navbar)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.back_home)
        home_btn.setIcon(QtGui.QIcon('D:\\ManiSimpleYoutubeDownloader\\home.png'))
        navbar.addAction(home_btn)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setIcon(QtGui.QIcon('D:\\ManiSimpleYoutubeDownloader\\pngtree-vector-back-icon-png-image_931209.png'))
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setIcon(QtGui.QIcon('D:\\ManiSimpleYoutubeDownloader\\pngtree-vector-forward-icon-png-image_927285.png'))
        navbar.addAction(forward_btn)

        reload_btn = QAction('Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setIcon(QtGui.QIcon('D:\\ManiSimpleYoutubeDownloader\\refresh-1781197-1518571.png'))
        navbar.addAction(reload_btn)

        self.download_btn = QAction('Download', self)
        self.download_btn.triggered.connect(self.download_button)
        self.download_btn.setIcon(QtGui.QIcon('D:\\ManiSimpleYoutubeDownloader\\download.png'))
        navbar.addAction(self.download_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setStyleSheet("""border-style: outset;
                                           border-width: 2px;
                                           border-radius: 10px;
                                           border-color:#3582c4;
                                          padding: 4px;""")

        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def download_button(self):
        self.url_text = self.url_bar.text()
        self.thread = DownloadThread(self.url_text)
        # self.thread.data_downloaded.connect(self.on_data_ready)
        self.thread.start()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Video Has Been Downloaded")
        msg.setWindowTitle("Download Info")
        msg.setStandardButtons(QMessageBox.Ok)

    def back_home(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,url):
       self.url_bar.setText(url.toString())


class DownloadThread(QThread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            print('working')
            url = self.url
            print(f'{url}')
            print('Downloading...')
            yt_opts = {
                'outtmpl': 'Mani YDL Downloaded Files/Downloaded_Videos/%(title)s-%(id)s.%(ext)s'
                       }
            ydl = yt_dlp.YoutubeDL(yt_opts)
            ydl.download(f"{url}")
            print('downloaded')

        except OSError:
            print('can\'download right now')

app = QApplication(sys.argv)
QApplication.setApplicationName('Mani Browser')
window = MainWindow()
app.exec_()