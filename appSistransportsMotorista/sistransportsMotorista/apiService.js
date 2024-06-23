export const fetchData = async (url, setData, setLoading) => {
  setLoading(true);
  try {
    console.log(`Fetching data from URL: ${url}`);
    const response = await fetch(url);
    console.log(response)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log('Data fetched successfully:', data);

    if (Array.isArray(data.dados)) {
      setData(data.dados);
    } else {
      console.error('Erro: Dados recebidos não são um array.', data);
      // Aqui você pode definir o comportamento para lidar com dados que não são um array
      setData([]); // Define como array vazio em caso de erro
    }
  } catch (error) {
    console.error('Erro ao buscar dados:', error);
    // Aqui você pode definir o comportamento para lidar com o erro
    setData([]); // Define como array vazio em caso de erro
  } finally {
    setLoading(false);
  }
};
