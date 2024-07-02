import PyPDF2


class PDF_TO_PODCAST():

    def __init__(self) -> None:
        self.text_to_voicemodel = None
        self.summarizer_model = None
        self.document_text = [] #list of strings

    def parse_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        self.document_text.append(text)
    

pdf = PDF_TO_PODCAST()
file_path = "./How Much House Can I Afford_.pdf"
pdf.parse_pdf(file_path)