import requests
import PyPDF2
import tempfile

def download_pdf(url):
    response = requests.get(url)
    response.raise_for_status()
    
    # Save to temporary file
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
        tmp_file.write(response.content)
        return tmp_file.name

def merge_pdfs_from_urls(urls, output_path):
    merger = PyPDF2.PdfMerger()
    
    try:
        # Download and merge each PDF
        for url in urls:
            pdf_path = download_pdf(url)
            merger.append(pdf_path)
            
        # Write merged PDF to output path
        merger.write(output_path)
        
    finally:
        merger.close()
