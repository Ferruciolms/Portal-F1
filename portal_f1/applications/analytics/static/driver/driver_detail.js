$(document).ready(function() {
    var chart_driver_years = document.getElementById('driver_years');

    let chartDriveYears = new Chart(chart_driver_years, {
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

                              return 'Poles in year - '+year
                            },
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                if (context.parsed.y !== null) {
                                    label += context.raw.y.toFixed(0) + " - Pole(s)";
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
    updateDriverYearChart();

    function updateDriverYearChart(){
    $.ajax({
            method: "GET",
            url: '/api/driver/detail/year/?driver=' + driver,
            success: function(data){
                for (var i = 0; i < data.labels.length; ++i) {
                    var newDataset = {
                        type: data.type[i],
                        borderWidth: 2,
                        pointStyle: 'rectRounded',
                        fill: false,
                        cubicInterpolationMode: 'monotone',
                        tension: 0.4,
                        borderColor: data.color[i],
                        backgroundColor: data.color[i],
                        label: data.labels[i],
                        data: data.data[i],
                    }
                    chartDriveYears.data.datasets.push(newDataset);
                }
                chartDriveYears.update();
            },
            error: function(error_data){
                console.log(error_data);
            }
        })

    }
});

