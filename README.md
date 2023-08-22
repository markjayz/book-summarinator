# book-summarinator
# Book Summarization API

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This is a simple Python script that creates an API endpoint for summarizing books using the OpenAI API. It allows you to input the title of a book and its author, and it returns a concise summary of the book's content.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed.
- An OpenAI API key. You can obtain one by signing up on the OpenAI website.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/book-summarinator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd book-summarinator
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the script, you need to set your OpenAI API key. You can do this by creating a `.env` file in the project directory and adding your API key like this:

```env
OPENAI_API_KEY=your_api_key_here


