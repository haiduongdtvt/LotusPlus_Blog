from docx import Document
from os.path import join, dirname, abspath 



def convert_docx_to_text(file_name):
    """
    Convert a DOCX file to plain text.

    Args:
        docx_path (str): Path to the DOCX file.

    Returns:
        str: The extracted text from the DOCX file.
    """
    file_path = join(dirname(abspath(__file__)),f'/report_generator/report_templates/{file_name}')
    # Load the DOCX file
    doc = Document(file_path)

    # Initialize an empty string to store the text
    text = ""

    # Iterate through each paragraph in the document and append its text to the string
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text.strip()  # Remove any trailing newline characters

if __name__ == "__main__":
    # Example usage
    text = convert_docx_to_text("report_template_2.docx")
    print("Extracted Text:", text)