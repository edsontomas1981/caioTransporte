from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
import os

@csrf_exempt
@require_http_methods(["POST","GET"])
def upload_xml(request):
    if request.FILES.getlist('xml_files'):
        xml_files = request.FILES.getlist('xml_files')
        fs = FileSystemStorage()
        for xml_file in xml_files:
            filename = fs.save(xml_file.name, xml_file)
            # Caminho completo do arquivo salvo
            uploaded_file_url = fs.url(filename)
            print(f'Arquivo XML salvo em: {uploaded_file_url}')
        
        return JsonResponse({'message': 'Arquivos XML recebidos com sucesso.'})
    return JsonResponse({'error': 'Nenhum arquivo XML encontrado.'}, status=400)
