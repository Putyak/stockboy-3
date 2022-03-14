<script>
  // core components
  import DataTable from "components/Tables/DataTable.svelte";
  import BarChart from "components/Charts/BarChart.svelte";
  export let location;



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
