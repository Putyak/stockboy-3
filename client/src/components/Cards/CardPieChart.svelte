<script>
  import { onMount } from "svelte";
  // library that creates chart objects in page
  import Chart from "chart.js";

  // init chart
  onMount(async () => {
    
    var colors = ['#1ba3c6', '#2cb5c0', '#30bcad', '#21B087', '#33a65c', '#57a337', '#a2b627', '#d5bb21', '#f8b620', '#f89217', '#f06719', '#e03426', '#f64971', '#fc719e', '#eb73b3', '#ce69be', '#a26dc2', '#7873c0', '#4f7cba']
      
    var pie_data_categories = {
      labels : [
        
          'Keychain',
          'Enamel Pins',
          'None',
          'uncategorized',
          'Socks',
          'Glasses Cases',
          'Hair Accessories',
          'Test Products',
          'Home Decor',
        
      ],
      datasets : [{

        data : [

          
            41077.85,
            59968.88,
            3559.68,
            5531.55,
            94463.03,
            17189.58,
            4612.15,
            404.68,
            1862.13,
          
          ]
        ,
        backgroundColor: colors}
    ]

    }
    var pie_init_categories =  {
      type:'pie',
      data: pie_data_categories,
      options: {
        responsive: true
      }
    };

    var ctx = document.getElementById("pie-chart").getContext("2d");
    window.myPie = new Chart(ctx, pie_init_categories);
  });
</script>

<div
  class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-white"
>
  <div class="rounded-t mb-0 px-4 py-3 bg-transparent">
    <div class="flex flex-wrap items-center">
      <div class="relative w-full max-w-full flex-grow flex-1">
        <h2 class="text-blueGray-700text-xl font-semibold">
          Product Category Sales
        </h2>
      </div>
    </div>
  </div>
  <div class="p-4 flex-auto">
    <!-- Chart -->
    <div class="relative">
      <canvas id="pie-chart"></canvas>
    </div>
  </div>
</div>
