<script>
  import { onMount } from "svelte";
  // library that creates chart objects in page
  import Chart from "chart.js";

  export let labels
  export let data
  export let meta
  

  // init chart
  onMount(async () => {
    let config = {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: meta['data_label'],
            backgroundColor: "rgba(85,182,133,.7)",
            borderColor: "rgba(85,182,133,.7)",
            data: data,
            fill: false,
            barThickness: 15
          },
        ]
      },
      options: {
        maintainAspectRatio: false,
        responsive: true,
        title: {
          display: false,
          text: meta['title'],
          fontColor: "white",
        },
        tooltips: {
          mode: "index",
          intersect: false,
        },
        hover: {
          mode: "nearest",
          intersect: true,
        },
        legend: {
          text: meta['legend'],
          labels: {
            fontColor: "white",
          },
          align: "end",
          position: "bottom",
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
                labelString: "Day",
              },
              gridLines: {
                borderDash: [2],
                borderDashOffset: [2],
                color: "rgba(33, 37, 41, 0.3)",
                zeroLineColor: "rgba(33, 37, 41, 0.3)",
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2],
              },
            },
          ],
          yAxes: [
            {
              ticks: {
                  fontColor: "rgba(255,255,255,.7)",
                },
              display: true,
              scaleLabel: {
                display: false,
                labelString: "Value",
              },
              gridLines: {
                borderDash: [2],
                drawBorder: false,
                borderDashOffset: [2],
                color: "rgba(255, 255, 255, 0.2)",
                zeroLineColor: "rgba(33, 37, 41, 0.15)",
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2],
              },
            },
          ],
        },
      },
    };
    let ctx = document.getElementById("bar-chart").getContext("2d");
    window.myBar = new Chart(ctx, config);
  });
</script>

<div
  class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded bg-blueGray-800"
>
  <div class="rounded-t mb-0 px-4 py-3 bg-transparent">
    <div class="flex flex-wrap items-center">
      <div class="relative w-full max-w-full flex-grow flex-1">
        <h6 class="uppercase text-blueGray-100 mb-1 text-xs font-semibold">
          {meta['title']}
        </h6>
        <h2 class="text-white text-xl font-semibold">
          {meta['subtitle']}
        </h2>
      </div>
    </div>
  </div>
  <div class="p-4 flex-auto">
    <div class="relative h-350-px">
      <canvas id="bar-chart"></canvas>
    </div>
  </div>
</div>
