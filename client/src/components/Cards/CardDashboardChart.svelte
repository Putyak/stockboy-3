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
          "Nov 01",
          "Nov 02",
          "Nov 03",
          "Nov 04",
          
          "Nov 05",
          
          "Nov 06",
          
          "Nov 07",
          
          "Nov 08",
          
          "Nov 09",
          
          "Nov 10",
          
          "Nov 11",
          
          "Nov 12",
          
          "Nov 13",
          
          "Nov 14",
          
          "Nov 15",
          
          "Nov 16",
          
          "Nov 17",
          
          "Nov 18",
          
          "Nov 19",
          
          "Nov 20",
          
          "Nov 21",
          
          "Nov 22",
          
          "Nov 23",
          
          "Nov 24",
          
          "Nov 25",
          
          "Nov 26",
          
          "Nov 27",
          
          "Nov 28",
          
          "Nov 29",
          
          "Nov 30",
          
          "Dec 01",
          
          "Dec 02",
          
          "Dec 03",
          
          "Dec 04",
          
          "Dec 05",
          
          "Dec 06",
          
          "Dec 07",
          
          "Dec 08",
          
          "Dec 09",
          
          "Dec 10",
          
          "Dec 11",
          
          "Dec 12",
          
          "Dec 13",
          
          "Dec 14",
          
          "Dec 15",
          
          "Dec 16",
          
          "Dec 17",
          
          "Dec 18",
          
          "Dec 19",
          
          "Dec 20",
          
          "Dec 21",
          
          "Dec 22",
          
          "Dec 23",
          
          "Dec 24",
          
          "Dec 25",
          
          "Dec 26",
          
          "Dec 27",
          
          "Dec 28",
          
          "Dec 29",
          
          "Dec 30",
          
          "Dec 31",
          
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
          
          "Jan 31",
          
          "Feb 01",
          
          "Feb 02",
          
          "Feb 03",
          
          "Feb 04",
          
          "Feb 05",
          
          "Feb 06",
          
          "Feb 07",
          
          "Feb 08",
          
          "Feb 09",
        ],
        datasets: [
          {
            label: 'Sales',
            type: 'line',
            backgroundColor: "rgba(59,148,104,0.3)",
            borderColor: "rgba(59,148,104,0.8)",
            data: [1046.68,
          
          1391.59,
        
          1541.81,
        
          1400.66,
        
          1523.36,
        
          847.58,
        
          835.81,
        
          1021.27,
        
          910.13,
        
          3908.11,
        
          2846.37,
        
          1219.15,
        
          2055.44,
        
          2046.43,
        
          1678.62,
        
          1922.37,
        
          3768.63,
        
          1154.39,
        
          1453.23,
        
          2240.98,
        
          1955.28,
        
          4260.25,
        
          1676.44,
        
          2372.55,
        
          968.02,
        
          2745.61,
        
          1765.8,
        
          2696.14,
        
          5706.78,
        
          3483.07,
        
        
        
          1769.79,
        
          2534.34,
        
          1037.7,
        
          2236.01,
        
          3698.13,
        
          3486.96,
        
          3118.16,
        
          3865.33,
        
          4423.79,
        
          5225.36,
        
          3737.78,
        
          5130.47,
        
          4803.69,
        
          5219.77,
        
          5615.66,
        
          5235.59,
        
          4753.41,
        
          4393.11,
        
          4658.43,
        
          4669.45,
        
          2494.98,
        
          2482.96,
        
          1429.34,
        
          719.68,
        
          1386.11,
        
          1061.67,
        
          1376.94,
        
          1592.53,
        
          1169.91,
        
          978.11,
        
          741.51,
        
        
        
        
        
          747.13,
        
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
        
          3680.18,
        
        
        
          3014.01,
        
          3009.1,
        
          3329.22,
        
          6893.2,
        
          3021.62,
        
          1320.15,
        
          1991.58,
        
          2121.74,
        
          1063.4, ],
            fill: true,
            

          },
          {
            label: 'Quantity Sold',
            fill: false,
            ///backgroundColor: "rgba(143,208,252,0.2)",
            backgroundColor: "rgba(95,185,248,0.8)",
            data: [97,
            
            201,
          
            171,
          
            172,
          
            1418,
          
            78,
          
            76,
          
            93,
          
            83,
          
            564,
          
            404,
          
            111,
          
            215,
          
            223,
          
            167,
          
            198,
          
            441,
          
            115,
          
            131,
          
            245,
          
            228,
          
            1802,
          
            171,
          
            307,
          
            88,
          
            255,
          
            163,
          
            291,
          
            743,
          
            344,
          
          
          
            157,
          
            301,
          
            95,
          
            221,
          
            370,
          
            331,
          
            295,
          
            368,
          
            456,
          
            548,
          
            334,
          
            465,
          
            447,
          
            523,
          
            537,
          
            473,
          
            436,
          
            402,
          
            438,
          
            450,
          
            225,
          
            281,
          
            133,
          
            66,
          
            135,
          
            100,
          
            169,
          
            184,
          
            110,
          
            90,
          
            71,
          
          
          
          
          
            69,
          
            150,
          
            143,
          
            65,
          
            477,
          
            217,
          
            102,
          
            1712,
          
            70,
          
            516,
          
            76,
          
            146,
          
            214,
          
            188,
          
            128,
          
            121,
          
            222,
          
            185,
          
            149,
          
            119,
          
            144,
          
            86,
          
            89,
          
            129,
          
            190,
          
            142,
          
            202,
          
            98,
          
            91,
          
            108,
          
            562,
          
          
          
            369,
          
            493,
          
            458,
          
            840,
          
            392,
          
            140,
          
            196,
          
            206,
          
            101,],
            type:'bar',
            
          },
        {
          type: 'bar',
          label: 'FBA',
          backgroundColor: "rgba(239, 153, 64, .8)",

          data: [
          
          
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
          
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
          
          
          
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            742,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            360,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
          
          
            0,
          
            293,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
            0,
          
          
          
        ]
        }
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
          Dashboard
        </h6>
        <h2 class="text-white text-xl font-semibold">
          Sales, Quantity Sold & FBA Transfer
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
