<script>
  import { Datatable, SearchInput } from 'svelte-simple-datatables'
  import { CSVDownloader } from 'svelte-csv';


  export let rows
  export let response
  export let meta

  const table_name = meta['title']
  const table_headers =  ["SKU", "Name", "QTY Sold", "Sales", "Burn"]

  const marketplace_icons = [
    {'name': 'amazon', 'icon': 'fab fa-amazon'},
    {'name': 'etsy' , 'icon':  'fab fa-etsy'},
    {'name': 'walmart' , 'icon': 'fab fa-weebly'},
    {'name': 'manual' , 'icon': 'fas fa-store'},
    {'name': 'shopify' , 'icon': 'fab fa-shopify'},
    {'name': 'woocommerce' , 'icon': 'fab fa-wordpress' },
  ]

  let status_color

  
  /// Datatable Constants
  
  const settings = {
      pagination: true,
      scrollY: false,
      rowsPerPage: 25,
      sortable: true,
      css: true,
      blocks: {
          searchInput: false,
          paginationButtons: true,
          paginationRowCount: true,
      }
  }

  
</script>


<div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
  <div class="rounded-t mb-0 px-4 py-3 border-0">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full px-4 max-w-full flex-grow flex-1">
          <h3 class="font-semibold text-base text-blueGray-700">
            {meta['title']}
          </h3>
        </div>
        <div class="relative w-full p-4 max-w-full flex-grow flex-1 text-center">
          <SearchInput classList="w-full rounded border-blueGray-400"/>
        </div>

        <div class="relative w-full px-4 max-w-full flex-grow flex-1 text-right">
          <CSVDownloader class="hover:bg-purple-600"
              data={response} filename={'stockboy-report.csv'} bom={true}
              >CSV <i class="fas fa-download py-2"></i>
          </CSVDownloader>

        </div>
      </div>
     
      {#await response}
          <p>waiting</p>
      {:then data}

          
      <Datatable {settings} {data} bind:dataRows={rows} classList="w-full">
          <thead class="mt-6 w-full">
              {#each meta.keys as key,i}
              
                <th data-key="{key}"
                    class="px-6 sortable bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                    {meta['header'][i]}
                    <i class="fas fa-sort"></i>
            </th>
              {/each}
          </thead>
          <tbody>

          {#if rows}
              {#each $rows as row}
              <tr>
                {#each meta.keys as key, i}
                  <td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-s p-4">
                    {#if key=='sku'}
                    <!-- SKU cell -->
                    <strong class="text-center">{row[key]}</strong> 
                      {#if row.img != "None"}<img src="{row.img}" width=100px class="pt-2 rounded mx-auto text-center"> {:else}<br/><i class="fas fa-image fa-4x"></i> {/if}
                    
                    {:else if key=='cost'}
                    <!-- Cost cell -->
                      <input value={row[key]}>
                    
                    {:else if key=='order_number'}
                    <!-- Order ID cell -->
                    <a href="./orders/{row[key]}" class="text-lightBlue-700">{row[key]}</a>

                    {:else if key=='order_store'}
                    <!-- Order Store cell -->
                      {#each marketplace_icons as icon }
                        {#if row[key].toLowerCase().includes(icon.name)}
                          <i
                            class="{icon.icon} px-2"
                          />
                        {/if}
                      {/each}
                      {row[key]}


                    {:else if key=='order_status'}
                    <!-- Order Status cell -->
                      {#if  row[key].includes('shipped') }
                      <i class='fas fa-circle text-emerald-700 mr-2'></i>
                      {:else if row.order_status.includes('cancelled')}
                        <i class='fas fa-circle text-red-500 mr-2'></i>
                      {:else if row.order_status.includes('awaiting') }
                        <i class='fas fa-circle text-LightBlue-500 mr-2'></i>
                      {/if}
                      {row[key]}

                      
                    {:else}
                    <!-- Normal cell -->
                      {row[key]}
                    {/if}

                    
                  </td>
                {/each}
              </tr>
            {/each}
          {/if}
          </tbody>
      </Datatable>
      {/await}
</div>
</div>
