// Define os dados do gráfico
var dataAvarias = {
    labels: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
    datasets: [{
        label: 'Matriz',
        data: [0, 19, 3, 15, 2, 13, 0],
        // backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'red',
        borderWidth: 3,
        fill: false, // Desativa o preenchimento da área
        context:{'teste':'teste3'},
    }],
    
};

document.addEventListener('DOMContentLoaded', function() {
   // Obtém o contexto do canvas
   var ctx = document.getElementById('avarias').getContext('2d');
    // Configurações do gráfico
    var options = {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        title: {
            display: true,
            text: 'Tempo Médio de Entrega'
        },
        legend: {
            position: 'right' // Define a posição da legenda para 'direita'
        },
    };

    // Cria o gráfico
    var myChart = new Chart(ctx, {
        type: 'line',
        data: dataAvarias,
        options: options
    });
})



