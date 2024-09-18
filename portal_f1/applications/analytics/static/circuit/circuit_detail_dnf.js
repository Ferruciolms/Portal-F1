$(document).ready(function() {
    var chart_circuit_dnfs = document.getElementById('circuit_dnfs');

    let chartCircuitDnfs = new Chart(chart_circuit_dnfs, {
        type: 'line',
        data: {
            labels: [], // eixo x
            datasets: [{
                label: 'DNFs by year',
                borderWidth: 2,
                pointStyle: 'circle',
                data: [],
                fill: true,
                cubicInterpolationMode: 'default',
                tension: 0.4,
                borderColor: 'rgba(255, 99, 71, 0.5)',
                backgroundColor: 'rgba(255, 99, 71, 0.5)',
                }
            ]


        },
        options: {
            aspectRatio: 2,
            interaction: {
                mode: 'x',
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        title: function(context) {
                            return 'DNFs in ' + context[0].label;
                        },
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            const dnfValue = context.dataset.data[context.dataIndex]; // Valor de DNFs para o ponto de dados atual
                            if (dnfValue !== null && dnfValue !== undefined) {
                                label += dnfValue.toFixed(0);
                                label = label.replace(".", ",");
                            }
                            return label;
                        },
                    }
                },
            },
            responsive: true,
            scales: {
                y: {
                    ticks: {
                        callback: function(value) {
                            return value;
                        }
                    }
                },
            }
        }
    });

    // Função para atualizar o gráfico com os dados da API
    function updateCircuitDnfsChart(){
        $.ajax({
            method: "GET",
            url: '/api/circuit/detail/dnf/?circuit=' + circuit,
            success: function(data){
                console.log(chartCircuitDnfs)

                    chartCircuitDnfs.data.labels = data.labels;
                    chartCircuitDnfs.data.datasets[0].data = data.data;

                chartCircuitDnfs.update();
            },
            error: function(error_data){
                console.log(error_data);
            }
        });
    }

    updateCircuitDnfsChart();
});
