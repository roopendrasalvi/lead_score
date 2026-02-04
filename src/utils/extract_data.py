from pypdf import PdfReader

def file_to_text(file_path):
    reader = PdfReader(file_path)
    text_content = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            text_content.append(f"--- Page {page_num} ---\n{text}")
        else:
            text_content.append(f"--- Page {page_num} ---\n[No extractable text]")

    full_text = "\n".join(text_content)
    return full_text