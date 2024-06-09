var atrasoVsEmDia = {
    labels: ['Sucesso', 'Devoluções', 'Avarias','Outros'],
    datasets: [{
        data: [80,10,8,2 ], // Valores percentuais ou absolutos para cada fatia
        backgroundColor: ['#57B657','#FF4747',' #FFA500','#808080'], // Cores das fatias
        borderColor: 'white', // Defina a cor da borda desejada
        borderWidth: 1,

        // ... outras configurações do conjunto de dados
    }]
};

document.addEventListener('DOMContentLoaded', function() {
   // Obtém o contexto do canvas
   var ctx = document.getElementById('atrasoVsEmDia').getContext('2d');
    // Configurações do gráfico
    var options = {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        title: {
            display: true,
            text: 'Sucesso de Entregas por Mês',
            fontSize:16,
            fontColor: 'white',

        },
        legend: {
            position: 'right' // Define a posição da legenda para 'direita'
        },
    };

    // Cria o gráfico
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: atrasoVsEmDia,
        options: options
    });
})

