<script>
  // core components
  import LineChart from "components/Charts/LineChart.svelte";
  import DataTable from "components/Tables/DataTable.svelte";
  import CardStat from "components/Headers/CardStat.svelte";
  import HeaderDatepicker from "components/Headers/HeaderDatepicker.svelte";

  
  let sales_by_day = getSalesbyDay();

  async function getSalesbyDay() {
      return await fetch('http://127.0.0.1:5555/sales/by-order')
          .then((response) => response.json())
          .then((data) => {
              return data;
      
        });
  }

  let sales_by_sku = getSalesbySKU();



  async function getSalesbySKU() {
      return await fetch('http://127.0.0.1:5555/sales/by-sku')
          .then((response) => response.json())
          .then((data) => {
              return data;
      
        });
  }


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

<!-- Header Stats -->
<div class="relative bg-blueGray-800 pt-8 pb-16 mb-8">
  <div class="px-4 md:px-10 mx-auto w-full ">
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

<div class="md:px-10">
  <!-- Chart -->
  <div class="flex flex-wrap">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
        {#await sales_by_day}
        <p>loading. . . </p>
          {:then chart_data}
          <LineChart labels={chart_data.days_in_range} data={chart_data.sales_by_day} meta={chart_meta}/>
        {/await}
    </div>
  </div>
 
  <!-- Data Table -->
  <div class="flex flex-wrap mt-4">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      {#await getSalesbySKU()}
      <p>LOADING. . . </p>

      {:then table_data}
      <DataTable response={table_data} meta={table_meta}  />
      {/await}
    </div>
  </div>
</div>
