from flask import Blueprint, request, jsonify, send_file
from app.pdf_utils import merge_pdfs_from_urls
import tempfile

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/merge', methods=['POST'])
def merge_pdfs():
    try:
        data = request.get_json()
        if not data or 'urls' not in data:
            return jsonify({'error': 'No URLs provided'}), 400
        
        pdf_urls = data['urls']
        if not isinstance(pdf_urls, list) or not pdf_urls:
            return jsonify({'error': 'URLs must be provided as a non-empty list'}), 400

        # Create temporary file for merged PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            output_path = tmp_file.name
            
        # Merge PDFs
        merge_pdfs_from_urls(pdf_urls, output_path)
        
        # Send merged file
        return send_file(output_path, as_attachment=True, download_name='merged.pdf')

    except Exception as e:
        return jsonify({'error': str(e)}), 500
