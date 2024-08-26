# YouTube Transcript to Detailed Notes Converter

This project is a Streamlit-based application that allows users to convert YouTube video transcripts into detailed notes. The application extracts the transcript from a YouTube video and uses Google's Generative AI to summarize the content into concise points.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Overview

The YouTube Transcript to Detailed Notes Converter helps users by providing a quick and easy way to generate detailed notes from the transcript of a YouTube video. By simply providing the YouTube video link, the app will fetch the transcript, summarize it using Google's Generative AI, and display the summary in a clear, concise format.

## Features

- **Transcript Extraction**: Extracts the transcript text from YouTube videos using the video URL.
- **Content Summarization**: Uses Google's Generative AI (Gemini model) to generate a summary of the video transcript.
- **Interactive Interface**: Provides a user-friendly interface for inputting YouTube links and viewing summaries.

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/youtube-transcript-to-notes.git
    cd youtube-transcript-to-notes
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a `.env` file in the root directory with the following content:

      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

    - Replace `your_google_api_key` with your actual Google API key.

## Usage

To run the application:

```bash
streamlit run app.py
```
## How It Works:

- **Enter YouTube Link**: Input the YouTube video link into the text box.
- **View Thumbnail**: The video thumbnail will be displayed for confirmation.
- **Generate Notes**: Click the "Get Detailed notes" button to extract the transcript and generate a summarized version.

### Example:

- **Enter YouTube Link**: Provide the URL of the YouTube video you want to summarize.
- **Analyze Transcript**: The app will extract the transcript and generate a summary.
- **Review Notes**: The AI-generated response will provide a detailed analysis and summary of the video.

## Project Structure

- `app.py`: Main application file that handles the Streamlit interface and core functionality.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `.env`: Environment variables file (not included in the repository; must be created by the user).

## Dependencies

The project uses the following dependencies:

- `youtube_transcript_api`: For extracting transcripts from YouTube videos.
- `streamlit`: For building the interactive user interface.
- `google-generativeai`: For generating summaries using Google's Generative AI.
- `python-dotenv`: For managing environment variables.
- `pathlib`: For handling file paths.

For a full list of dependencies, please refer to the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
