async function uploadXMLFiles() {
    const input = document.getElementById('xmlFilesInput');
    const files = input.files;
    
    if (files.length === 0) {
        alert('Por favor, selecione ao menos um arquivo XML.');
        return;
    }

    const formData = new FormData();
    for (const file of files) {
        formData.append('xml_files', file);
    }

    try {
        const response = await fetch('/operacional/upload_xml/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Erro ao enviar arquivos XML.');
        }

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao enviar os arquivos XML.');
    }
}
