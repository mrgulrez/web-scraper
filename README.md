
# Web Data Extractor

This project extracts various types of data from a given URL, including titles, headings, paragraphs, lists, images, links, and tables. The extracted data is then displayed on a modern web interface using Tailwind CSS for styling.

## Features

- Extracts titles, headings, paragraphs, lists, images, links, and tables from any given URL.
- Saves the extracted data to a database.
- Displays the extracted data in a modern, user-friendly interface.
- Utilizes Tailwind CSS for responsive and aesthetically pleasing design.

## Technologies Used

- **Python**: For server-side logic.
- **Django**: As the web framework.
- **BeautifulSoup**: For parsing HTML and extracting data.
- **Tailwind CSS**: For styling the web pages.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/web-data-extractor.git
   cd web-data-extractor
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Extracting Data

1. Navigate to the home page where you'll find a form to enter the URL of the web page you want to extract data from.
2. Enter the URL and submit the form.
3. The server will process the URL, extract the data, and save it to the database.
4. You will be redirected to a page displaying the extracted data.

### Viewing Extracted Data

1. After the extraction process is complete, the extracted data will be displayed in a structured format.
2. The data includes titles, headings, paragraphs, lists, images, links, and tables, each in its respective section.

## Project Structure

- `extractor/`: Main Django application folder.
- `extractor/models.py`: Defines the data models.
- `extractor/views.py`: Contains the logic for data extraction and rendering views.
- `templates/`: HTML templates for rendering web pages.
  - `form.html`: Form for entering URL.
  - `view_data.html`: Page for displaying extracted data.
- `static/`: Static files including Tailwind CSS.
- `requirements.txt`: List of Python dependencies.

## Code Overview

### Views

- **extract_data**: Handles the extraction process, saves data to the database, and redirects to the view data page.
- **view_data**: Retrieves the extracted data from the database and renders it on the page.
