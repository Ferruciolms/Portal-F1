$(document).ready(function() {
    var chart_driver_seasons = document.getElementById('driver_seasons');

    let chartDriverSeason = new Chart(chart_driver_seasons, {
        responsive: true,
        drawTicks: false,
            data: {
                labels: [], //eixo x
                datasets: []
            },
            options: {
                aspectRatio: 2,
                interaction: {
                    //intersect: false,
                    mode: 'x',
                },
                            plugins: {
                    tooltip: {
                        callbacks:{
                            title: function(context) {
                              const d = Date.parse(context[0].raw.x);
                              const date = new Date(d);

                              year  = 1900 + date.getYear();

                              return  'Points in year - ' +year
                            },
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                if (context.parsed.y !== null) {
                                    label += context.raw.y.toFixed(0);
                                    label = label.replace(".", ",")
                                }

                              return label
                            },
                        }
                    },
                },

                responsive: true,
                scales: {
                    y: {
                        ticks: {
                            callback: function(value, index, values) {
                                return value;
                            }
                        }
                    },
                    x: {
                        display: true,
                        title: {
                          display: true
                        },

                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 31,
                            callback: function(value, index, values) {
                                return value;
                            }
                        },
                        type: 'time',
                           time: {
                                unit: 'year',
                                displayFormats: {
                                    'year': 'YYYY',
                                }

                           }
                    }
                 }
            }
        });
    updateDriverSeasonChart();

    function updateDriverSeasonChart(){
    $.ajax({
            method: "GET",
            url: '/api/driver/detail/season/?driver=' + driver,
            success: function(data){
                for (var i = 0; i < data.labels.length; ++i) {
                    var newDataset = {
                        type: data.type[i],
                        borderWidth: 2,
                        pointStyle: 'circle',
                        fill: false,
                        cubicInterpolationMode: 'default',
                        tension: 0.4,
                        borderColor: data.color,
                        backgroundColor: data.color,
                        label: data.labels[i],
                        data: data.data[i],

                    }
                    chartDriverSeason.data.datasets.push(newDataset);
                }
                chartDriverSeason.update();
            },
            error: function(error_data){
                console.log(error_data);
            }
        })

    }
});