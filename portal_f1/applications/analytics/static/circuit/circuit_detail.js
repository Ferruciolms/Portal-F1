$(document).ready(function() {
    var chart_top_wins = document.getElementById('top_wins');

    let chartTopWins = new Chart(chart_top_wins, {
          type: 'bar',
  data: {
    labels: [],
    datasets: [
	    {
	    label: 'Wins in circuit',
        borderColor: 'rgba(255, 0, 0, 1)',
        backgroundColor: 'rgba(255, 0, 0, 1)',
        cubicInterpolationMode: 'monotone',
        tension: 0.8,
	    data: [],
      	borderWidth: 2
    	},
		]
  },
  options: {
  	scales: {
    	yAxes: [{
        ticks: {
					reverse: false
        }
      }]
    }
  }

    });

    updateChartTopWins();

    function updateChartTopWins(){
        $.ajax({
            method: "GET",
            url: '/api/circuit/detail/?circuit=' + circuit,
            success: function(data){
                console.log(chartTopWins)

                    chartTopWins.data.labels = data.labels;
                    chartTopWins.data.datasets[0].data = data.data;


                chartTopWins.update();
            },
            error: function(error_data){
                console.log(error_data);
            }
        });
    }
});