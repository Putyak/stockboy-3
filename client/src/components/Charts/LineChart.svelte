<script>
  import { onMount } from "svelte";
  // library that creates chart objects in page
  import Chart from "chart.js";


  export let labels
  export let data
  export let meta


  // init chart
  onMount(async () => {
    var config = {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: meta['data_label'],
            type: 'line',
            backgroundColor: "rgba(59,148,104,0.4)",
            borderColor: "rgba(59,148,104,0.8)",
            data: data,
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
          text: meta['title'],
          fontColor: "white",
        },
        legend: {
          labels: {
            fontColor: "white",
            text: meta['legend'],
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
          {meta.title}
        </h6>
        <h2 class="text-white text-xl font-semibold">
          {meta.subtitle}
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
