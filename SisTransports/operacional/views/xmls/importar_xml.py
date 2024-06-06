from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@login_required(login_url='/auth/entrar/')
@require_http_methods(["POST","GET"])
def importar_xml (request):
    return render(request, 'importar_xmls.html')
