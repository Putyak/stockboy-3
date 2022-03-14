<script>
  // core components
  import DataTable from "components/Tables/DataTable.svelte";
  import BarChart from "components/Charts/BarChart.svelte";
  import CardStat from "components/Headers/CardStat.svelte";
  import HeaderDatepicker from "components/Headers/HeaderDatepicker.svelte";

  


  /// Get Orders Chart Data
  let orders_by_day = getOrdersbyDay();

  async function getOrdersbyDay() {
      return await fetch('http://127.0.0.1:5555/orders/by-day')
          .then((response) => response.json())
          .then((data) => {
              return data;
      
        });
  }

  /// Get Order Table Data
  let sales_by_sku = getOrders();
    
    async function getOrders() {
        return await fetch('http://127.0.0.1:5555/orders')
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

  const chart_meta = {
    data_label: 'Orders',
    title: 'Orders Chart',
    legend: 'Orders',
    subtitle: range_days.toString() + " days",
    }


  const table_meta = {
      header: ["Order Date", "Order ID", "Store name", "Order Status", "Ship To", "Order Qty"],
      title: "Orders",
      keys: ['order_date','order_number','order_store','order_status', 'ship_to','order_qty'],
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
<div class="flex flex-wrap">
  <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">           
    
    {#await orders_by_day}
    <p>loading</p>
    {:then orders}
      <BarChart labels={orders.labels} data={orders.data} meta={chart_meta}/>
      {/await}
  </div>
  <div class="w-full px-4">
    <div
      class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
    >      
    {#await getOrders()}
      <p>LOADING. . . </p>

    {:then table_data}
      <DataTable response={table_data} meta={table_meta}  />
    {/await}

    </div>
  </div>
</div>
