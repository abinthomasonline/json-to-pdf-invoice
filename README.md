# json-to-pdf-invoice

Programatically generate pdf invoices using python.

## Installation

```bash
pip install -r requirements.txt
```
Follow the steps here to install [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit?tab=readme-ov-file#installation)

## Usage

```bash
python main.py --input_json_path <path_to_json_file> --output_pdf_path <path_to_output_pdf>
```

## Implementation

The invoice template is first written in html and css. The data is then read from the json file and the html template is populated with the data. The populated html template is then converted to pdf using [pdfkit](https://github.com/JazzCore/python-pdfkit)
