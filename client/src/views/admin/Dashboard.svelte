<script>
  // core components
  //import LineChart from "components/Charts/LineChart.svelte";
  //import DataTable from "components/Tables/DataTable.svelte";
  //import CardStat from "components/Headers/HeaderCardStat.svelte";
  import HeaderDatepicker from "components/Headers/HeaderDatepicker.svelte";


  import CardDashboardChart from "components/Cards/CardDashboardChart.svelte";
  import CardPieChart from "components/Cards/CardPieChart.svelte";
  import CardShortTable from "components/Cards/CardShortTable.svelte";
  import CardStat from "components/Headers/CardStat.svelte";



  export let location;
  
  let orders_by_day = getOrdersbyDay();
    
    async function getOrdersbyDay() {
        return await fetch('http://137.184.139.204/sales/by-order')
            .then((response) => response.json())
            .then((data) => {
                return data;
        
          });
    }
  
    let stat
  
     

  /// Replace with Stats Requests
  let card_stats = [
    {'name': "sales",
    'value':  "50,897",},
    {'name': "shipping",
    'value':  "2,356",},
    {'name': "discounts",
    'value':  "924",},
    {'name': "burn",
    'value':  "38.2",},
  ]


  let range_days = 30;

  /// Chart Constants
const chart_meta = {
    data_label: 'Sales',
    title: 'Sales Chart',
    legend: 'Sales',
    subtitle: range_days.toString() + " days"
  

  }
  /// Table Constants

  const table_meta = {
    header: ["SKU", "Name", "QTY Sold", "Sales", "Burn"],
    title: "Sales",
    keys: ['sku','name','qty','sales', 'burn'],
  }
  
</script>


<HeaderDatepicker />


<div class="relative bg-blueGray-800 pt-8 pb-16">
  <div class="px-4 md:px-10 mx-auto w-full">
    <div>
        <!-- Card stats -->
        <div class="flex flex-wrap">
          {#each card_stats as stat}
            <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
              <CardStat stat_name={stat['name']} value={stat['value']} />
            </div>
          {/each}
      </div>
    </div>
  </div>
</div>




<div class="px-4 md:px-10 mx-auto w-full mt-12">
  <div class="flex flex-wrap">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      {#await orders_by_day}
      <p>loading</p>
      {:then dashboard_chart}
        <CardDashboardChart orders_by_day={dashboard_chart}/>
      {/await}
    </div>
    
  </div>
  <div class="flex flex-wrap mt-4">
    <div class="w-full xl:w-6/12 mb-12 xl:mb-0 px-4">
      <CardShortTable />
    </div>
    <div class="w-full xl:w-6/12 px-4">
      <CardPieChart />
    </div>
  </div>
</div>
