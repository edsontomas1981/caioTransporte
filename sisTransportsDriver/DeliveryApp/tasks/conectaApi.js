  export const fetchAPI = async (url, method = 'GET', data = null) => {

    const headers = {
      'Content-Type': 'application/json',
      // Adicione quaisquer headers adicionais necessários aqui
    };

    const config = {
      method: method,
      headers: headers,
      // Incluir o corpo da requisição se houver dados para enviar
      body: data ? JSON.stringify(data) : null,
    };

    try {
      const response = await fetch(url, config);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const responseData = await response.json();
      return responseData;
    } catch (error) {
      console.error('Erro ao fazer requisição:', error);
      // Se necessário, você pode lidar com erros aqui, como lançar um alerta
      return null; // Retorna null em caso de erro
    }
  };
