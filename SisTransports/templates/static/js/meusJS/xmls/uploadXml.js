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
        let dadosTbody = prepara_dados(result)
        popula_tbody_paginacao('paginacaoImportacaoNF','notasImportadas',dadosTbody,false,1,5,false,false)
        alert(result.message);
    } catch (error) {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao enviar os arquivos XML.');
    }
}

const prepara_dados = (result)=>{
    let dados = []
    result.data.forEach(element => {
        dados.push({nf:element.ide.nNF,
                    remetente:truncateString(element.emit.xNome,10),
                    destinatario:truncateString(element.dest.xNome,10),
                    origem:truncateString(element.emit.xBairro,7),
                    destino:truncateString(element.dest.xBairro,7),
                    volume:element.ide.volume,
                    peso:element.ide.peso,
                    valorNfe:element.ide.valorNF
        })
    });
    return dados
}