# 🎥 YouTube Downloader with python

A simple YouTube video downloader built with Python, using `tkinter` for the GUI and `pytube` for downloading videos. This application allows you to easily download YouTube videos in the highest resolution available directly to your Downloads folder.

## ✨ Features

- 📺 **Download Videos:** Enter a YouTube URL to download the video in high resolution.
- 📁 **Save to Downloads Folder:** Videos are automatically saved to your system's Downloads folder.
- 📊 **Progress Tracking:** View the download progress percentage and a progress bar.
- 🎨 **Customizable UI:** The application uses `customtkinter` for a modern look.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **pip**: The Python package installer.

## 🚀 Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/erfunit/python-youtube-downloader.git
    cd python-youtube-downloader
    ```

2. **Install the required packages:**

    ```bash
    pip install pytube customtkinter
    ```

3. **Run the application:**

    ```bash
    python app.py
    ```

## 🖥️ Usage

1. **Open the Application:**

    After running the script, the YouTube Downloader window will appear.

2. **Enter a YouTube URL:**

    - Paste the YouTube video link into the input field.
    - Ensure the URL is in the format `https://www.youtube.com/watch?v=...`.

3. **Download the Video:**

    - Click the "Download" button.
    - The download progress will be displayed as a percentage and a progress bar.
    - Once the download is complete, the video will be saved to your Downloads folder.

## 📝 Code Overview

### Main Components

- **`extract_video_id(url)`**: Extracts the video ID from a YouTube URL.
- **`get_downloads_folder()`**: Returns the path to the user's Downloads folder.
- **`startDownload()`**: Initiates the download process and manages the download thread.
- **`download_video(video, download_path)`**: Handles the actual downloading of the video.
- **`on_progress(stream, chunk, bytes_remaining)`**: Updates the progress percentage during the download.

### UI Elements

- **`CTkLabel`**: Labels to display text like titles, messages, and progress.
- **`CTkEntry`**: Entry field for the user to input the YouTube URL.
- **`CTkButton`**: Button to start the download process.
- **`CTkProgressBar`**: Progress bar that visually represents the download progress.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to customize this README as needed!
