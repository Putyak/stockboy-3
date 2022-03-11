<script>
  // core components
  import Table from "components/Cards/CardTable-Repeatable.svelte";
  import BarChart from "components/Charts/BarChart.svelte";
  export let location;

  let orders_by_day = getOrdersbyDay();

  async function getOrdersbyDay() {
      return await fetch('http://127.0.0.1:5555/orders/by-day')
          .then((response) => response.json())
          .then((data) => {
              return data;
      
        });
  }


  let meta = {
    'data_label': 'Orders',
    'title': 'Orders Chart',
    'legend': 'Orders',

  }

</script>


<div class="flex flex-wrap">
  <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">           
    
    {#await orders_by_day}
    <p>loading</p>
    {:then orders}
      <BarChart labels={orders.labels} data={orders.data} meta={meta}/>
      {/await}
  </div>
  <div class="w-full px-4">
    <div
      class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
    >
      <Table />
    </div>
  </div>
</div>
