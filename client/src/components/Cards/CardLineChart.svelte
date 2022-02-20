<script>
  import { onMount } from "svelte";
  // library that creates chart objects in page
  import Chart from "chart.js";

  // init chart
  onMount(async () => {
    var config = {
      type: "line",
      data: {
        labels: [
          "Jan 01",
        
        "Jan 02",
        
        "Jan 03",
        
        "Jan 04",
        
        "Jan 05",
        
        "Jan 06",
        
        "Jan 07",
        
        "Jan 08",
        
        "Jan 09",
        
        "Jan 10",
        
        "Jan 11",
        
        "Jan 12",
        
        "Jan 13",
        
        "Jan 14",
        
        "Jan 15",
        
        "Jan 16",
        
        "Jan 17",
        
        "Jan 18",
        
        "Jan 19",
        
        "Jan 20",
        
        "Jan 21",
        
        "Jan 22",
        
        "Jan 23",
        
        "Jan 24",
        
        "Jan 25",
        
        "Jan 26",
        
        "Jan 27",
        
        "Jan 28",
        
        "Jan 29",
        
        "Jan 30",
        
        "Jan 31"
        ],
        datasets: [
          {
            label: 'Sales',
            type: 'line',
            backgroundColor: "rgba(59,148,104,0.4)",
            borderColor: "rgba(59,148,104,0.8)",
            data: [ 747.13,
          
          1504.95,
        
          1032.09,
        
          700.2,
        
          3015.18,
        
          1592.78,
        
          855.07,
        
          2734.71,
        
          768.01,
        
          2715.39,
        
          822.55,
        
          1219.59,
        
          1875.58,
        
          1465.14,
        
          1068.57,
        
          1173.22,
        
          1224.9,
        
          1547.21,
        
          1344.01,
        
          964.48,
        
          1182.77,
        
          914.38,
        
          903.98,
        
          1277.36,
        
          1535.78,
        
          1372.88,
        
          1705.05,
        
          929.0,
        
          891.37,
        
          1066.34,
        
          3680.18,],
            fill: true,
            

          },
        ]
      },
      options: {
        maintainAspectRatio: false,
        responsive: true,
        elements: {
          line: {
            tension: .3,
          },
        },
        title: {
          display: false,
          text: "Sales Charts",
          fontColor: "white",
        },
        legend: {
          labels: {
            fontColor: "white",
          },
          align: "end",
          position: "bottom",
        },
        tooltips: {
          mode: "index",
          intersect: false,
        },
        hover: {
          mode: "nearest",
          intersect: true,
        },
        scales: {
          xAxes: [
            {
              ticks: {
                fontColor: "rgba(255,255,255,.7)",
              },
              display: true,
              
              scaleLabel: {
                display: false,
                labelString: "Month",
                fontColor: "white",
              },
              gridLines: {
                display: false,
                borderDash: [2],
                borderDashOffset: [2],
                color: "rgba(33, 37, 41, 0.3)",
                zeroLineColor: "rgba(0, 0, 0, 0)",
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2],
              },
            },
          ],
          yAxes: [
            {
              
              ticks: {
                beginAtZero: true, 
                fontColor: "rgba(255,255,255,.7)",
                
              },
              display: true,
              
              scaleLabel: {
                display: false,
                labelString: "Value",
                fontColor: "black",
              },
              gridLines: {
                
                borderDash: [3],
                borderDashOffset: [3],
                drawBorder: false,
                color: "rgba(255, 255, 255, 0.15)",
                zeroLineColor: "rgba(33, 37, 41, 0)",
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2],
              },
            },
          ],
        },
      },
    };
    var ctx = document.getElementById("line-chart").getContext("2d");
    window.myLine = new Chart(ctx, config);
  });
</script>

<div
  class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-blueGray-800"
>
  <div class="rounded-t mb-0 px-4 py-3 bg-transparent">
    <div class="flex flex-wrap items-center">
      <div class="relative w-full max-w-full flex-grow flex-1">
        <h6 class="uppercase text-blueGray-100 mb-1 text-xs font-semibold">
          Sales
        </h6>
        <h2 class="text-white text-xl font-semibold">
          /x days/
        </h2>
      </div>
    </div>
  </div>
  <div class="p-4 flex-auto">
    <!-- Chart -->
    <div class="relative h-350-px">
      <canvas id="line-chart"></canvas>
    </div>
  </div>
</div>
