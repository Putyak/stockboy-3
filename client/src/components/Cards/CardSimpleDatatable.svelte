<script>
    import { data } from '../../Dummy/TableData.js'  
    import { Datatable } from 'svelte-simple-datatables'
    
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

    let rows
    


</script>


<div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
    <div class="rounded-t mb-0 px-4 py-3 border-0">
        <div class="flex flex-wrap items-center">
          <div class="relative w-full px-4 max-w-full flex-grow flex-1">
            <h3 class="font-semibold text-base text-blueGray-700">
              Sales by SKU
            </h3>
          </div>
          <div class="relative w-full px-4 max-w-full flex-grow flex-1 text-right">
            <button 
              class="bg-indigo-500 text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
              type="button"
            >
              CSV
              <i class="fas fa-download"></i>
            </button>
          </div>
        </div>
      
    <Datatable {settings} {data} bind:dataRows={rows}>
        <thead class="mt-6">
            <th data-key="sku" 
                class="px-6 sortable bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                sku
                <i class="fas fa-sort"></i>
            </th>
            <th data-key="name" 
                class="px-6 sortable bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                Name
                <i class="fas fa-sort"></i>
            </th>
            <th data-key="qty" 
                class="px-6 sortable bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                Qty Sold
                <i class="fas fa-sort"></i>
            </th>
            <th data-key="sales" 
                class="px-6 sortable bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                Sales
                <i class="fas fa-sort"></i>
            </th>
            <th data-key="burn" 
                class="px-6 sortable bg-blueGray-50 text-blueGray-500 align-middle border border-solid border-blueGray-100 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-nowrap font-semibold text-left">
                Burn
                <i class="fas fa-sort"></i>
            </th>
        </thead>
        <tbody>
        {#if rows}
            {#each $rows as row}
            <tr>
                <td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                    {row.sku} {#if row.img != "None"}<img src="{row.img}" width=100px> {:else}<br/><i class="fas fa-image fa-4x"></i> {/if}</td>
                <td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs p-4">
                    {row.name}</td>
                <td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                    {row.qty}</td>
                <td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                    ${row.sales}</td>
                <td class="border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-nowrap p-4">
                    {row.burn}</td>
            </tr>
            {/each}
        {/if}
        </tbody>
    </Datatable>
</div>
</div>
