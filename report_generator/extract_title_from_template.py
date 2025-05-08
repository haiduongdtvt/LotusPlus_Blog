from docxtpl import DocxTemplate
from docx import Document
from io import StringIO  
from docx.shared import Pt, Cm, RGBColor
from os.path import join, dirname, abspath 



def extract_title_from_template(file_name):
    
    INPUT_FILE = join(dirname(abspath(__file__)),f'/report_generator/report_templates/{file_name}')
    """
    Extracts the title from a Word document template.
    
    Args:
        template_path (str): The path to the Word document template.
        
    Returns:
        str: The extracted title from the template.
    """
    # Load the Word document
    # doc = Docx(INPUT_FILE)
    # maintenance_table = None
    print(INPUT_FILE)
    
    with open(INPUT_FILE, 'rb') as f:
        source_stream = StringIO(f.read())
        doc = Document(source_stream)
    source_stream.close()
    
    # Xác định bảng VSAT (dựa vào từ khóa trong cột thứ 2, hàng 1)
    for table in doc.tables:
        print(table.cell(0, 1).text.strip())
    
    # if maintenance_table is None:
    #     raise ValueError("Không tìm thấy bảng chứa nội dung VSAT.")
    
    # # Initialize an empty string for the title
    # result_dict = {}
    
    # for i in range(1, len(maintenance_table.rows)): # chạy từ 1 để bỏ qua header
    #     row = maintenance_table.row_cells(i)
    #     try:
    #         step_number = int(maintenance_table.cell(i, 0).text.strip())
    #         description = maintenance_table.cell(i, 1).text.strip()
    #         result = maintenance_table.cell(i, 3).text.strip()
    #         result_dict[step_number] = {description: result}
    #     except Exception:
    #         continue
    #     return result_dict

if __name__ == "__main__":
    # Example usage
    template_dict = extract_title_from_template("report_template_2.docx")
    # print("Extracted Title:", template_dict)
            
