<script>
  // core components
  import LineChart from "components/Charts/LineChart.svelte";
  import Datatable from "../../components/Tables/DataTable.svelte";
  export let location;
  
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


  let meta = {
    'data_label': 'Sales',
    'title': 'Sales Chart',
    'legend': 'Sales',

  }

  
</script>

<div>
  <div class="flex flex-wrap">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
        {#await sales_by_day}
        <p>loading. . . </p>
          {:then chart_data}
          <LineChart labels={chart_data.days_in_range} data={chart_data.sales_by_day} meta={meta}/>
        {/await}
    </div>
  </div>
  <div class="flex flex-wrap mt-4">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      {#await sales_by_sku}
      {:then table_data}
      <p>LOADING. . . </p>
      <Datatable />
      {/await}
    </div>
  </div>
</div>
