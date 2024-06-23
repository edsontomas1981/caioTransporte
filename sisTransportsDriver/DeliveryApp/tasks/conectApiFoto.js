export const fetchAPI = async (url, method = 'GET', data = null, isMultipart = false) => {
  const headers = isMultipart ? {} : {
    'Content-Type': 'application/json',
  };

  const config = {
    method: method,
    headers: headers,
    body: isMultipart ? data : JSON.stringify(data),
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
    return null;
  }
};
