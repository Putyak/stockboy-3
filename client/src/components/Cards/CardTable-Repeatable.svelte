<script>
  // core components
  import TableDropdown from "components/Dropdowns/TableDropdown.svelte";
  import { Datatable } from "svelte-simple-datatables";
  import { each } from "svelte/internal";


  const marketplace_icons = [
    {'name': 'amazon', 'icon': 'fab fa-amazon'},
    {'name': 'etsy' , 'icon':  'fab fa-etsy'},
    {'name': 'walmart' , 'icon': 'fab fa-walmart'},
    {'name': 'manual' , 'icon': 'fa fa-store'},
    {'name': 'shopify' , 'icon': 'fab fa-shopify'},
    {'name': 'woocommerce' , 'icon': 'fab fa-wordpress' },
  ]

  let status_color

  let rows
  const settings = {
        pagination: true,
        scrollY: false,
        rowsPerPage: 25,
        sortable: true,
        css: true,
        blocks: {
            searchInput: true,
            paginationButtons: true,
            paginationRowCount: true,
        }
    }


  const table_name = "Orders"
  const table_headers = ["Order Date", "Order ID", "Store name", "Order Status", "Ship To", "Order Qty"]

  let sales_by_sku = getOrders();
    
    async function getOrders() {
        return await fetch('http://127.0.0.1:5555/orders')
            .then((response) => response.json())
            .then((data) => {
                return data;
        
         });
    }
    

  const bootstrap = "../assets/img/bootstrap.jpg";
  const angular = "../assets/img/angular.jpg";
  const sketch = "../assets/img/sketch.jpg";
  const react = "../assets/img/react.jpg";
  const vue = "../assets/img/react.jpg";

  const team1 = "../assets/img/team-1-800x800.jpg";
  const team2 = "../assets/img/team-2-800x800.jpg";
  const team3 = "../assets/img/team-3-800x800.jpg";
  const team4 = "../assets/img/team-4-470x470.png";

  // can be one of light or dark
  export let color = "light";
</script>

<div
  class="relative flex flex-col min-break-wordsw-0 pb-4 w-full shadow-lg rounded {color === 'light' ? 'bg-white' : 'bg-red-800 text-white'}"
>
  <div class="rounded-t mb-0 px-4 py-3 border-0">
    <div class="flex flex-wrap items-center">
      <div class="relative w-full px-4 max-w-full flex-grow flex-1">
        <h3
          class="font-semibold text-lg {color === 'light' ? 'text-blueGray-700' : 'text-white'}"
        >
          {table_name}
        </h3>
      </div>
    </div>
  </div>
  <div class="block w-full ">
    <!-- Projects table -->
    {#await getOrders()}
    <p>waiting</p>
    {:then data}
    
    <Datatable {settings} {data} bind:dataRows={rows} classList="w-full">
    <!-- <table class="items-center w-full bg-transparent border-collapse"> -->
      <thead>
        <tr>
          {#each table_headers as header}
          <th
            class="px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left {color === 'light' ? 'bg-blueGray-50 text-blueGray-500 border-blueGray-100' : 'bg-red-700 text-red-200 border-red-600'}"
          >
            {header}
          </th>
          {/each}
        </tr>
      </thead>
      <tbody>      
        {#if rows}
        {#each $rows as row}
        <tr>

          <td
            class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4 text-left flex items-center"
          >
            <span
              class="ml-3 font-bold {color === 'light' ? 'btext-blueGray-600' : 'text-white'}"
            >
              {row.order_date}
            </span>
          </td>
          
          <td
            class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
          <a href="#" class="text-lightBlue-700">
            {row.order_number}
          </a>
          </td>
          <td
            class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
          {#each marketplace_icons as store }
            {#if row.order_store.toLowerCase().includes(store.name)}
          <i
            class="{store.icon} px-2"
           />
            {/if}
          {/each}
          {row.order_store}
          </td>
          <td
            class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
          {#if  row.order_status.includes('shipped') }
            <i class='fas fa-circle text-emerald-700 mr-2'></i>
          {:else if row.order_status.includes('cancelled')}
            <i class='fas fa-circle text-red-500 mr-2'></i>
          {:else if row.order_status.includes('awaiting') }
            <i class='fas fa-circle text-LightBlue-500 mr-2'></i>
          {/if}
            
            {row.order_status}
          </td>
          <td
            class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            {row.ship_to}

          </td>
          <td
            class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4"
          >
            <div class="flex items-center">
              <span class="mr-2">{row.order_qty}</span>
            </div>
          </td>
        </tr>
        {/each}
        {/if}
      </tbody>
    </Datatable>
    {/await}

  </div>
</div>
