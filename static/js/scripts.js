google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawVisualization);
google.charts.setOnLoadCallback(drawVisualization1);

function drawVisualization() {
  // Some raw data (not necessarily accurate)
  var data = google.visualization.arrayToDataTable([
    ['Month', 'Light', 'Temp'],
    ['20C',  165,         614.6],
    ['40C',  135,     682],
    ['60C',  157,    623],
    ['80C',  139,     609.4],
    ['100C',  136,    569.6]
  ]);

  var options = {
    title : 'Voltage over temprature per daily',
    vAxis: {title: 'Voltage'},
    hAxis: {title: 'Temperature'},
    seriesType: 'bars',
    series: {5: {type: 'line'}}
  };

  var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}

function drawVisualization1() {
    // Some raw data (not necessarily accurate)
    var data1 = google.visualization.arrayToDataTable([
      ['Month', 'Curr', 'Power'],
      ['20C',  165,         614.6],
      ['40C',  135,     682],
      ['60C',  157,    623],
      ['80C',  139,     609.4],
      ['100C',  136,    569.6]
    ]);
  
    var options1 = {
      title : 'Current over Power per daily',
      vAxis: {title: 'Current'},
      hAxis: {title: 'Power'},
      seriesType: 'bars',
      series: {5: {type: 'line'}}
    };
var chart = new google.visualization.ComboChart(document.getElementById('chart_div1'));
chart.draw(data1, options1);
}
