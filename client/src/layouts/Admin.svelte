<script>
  import { Router, Route } from "svelte-routing";
  

  // components for this layout
  import AdminNavbar from "components/Navbars/AdminNavbar.svelte";
  import Sidebar from "components/Sidebar/Sidebar.svelte";
  import FooterAdmin from "components/Footers/FooterAdmin.svelte";
  import CardDashboardChart from "components/Cards/CardDashboardChart.svelte";
  import CardPieChart from "../components/Cards/CardPieChart.svelte";
  import CardShortTable from "../components/Cards/CardShortTable.svelte";
  import CardStats from "../components/Cards/CardStats-Repeatable.svelte"
  import HeaderDatepicker from "../components/Headers/HeaderDatepicker.svelte";

  // pages for this layout
  import Sales from "views/admin/Sales.svelte";
  import COGS from "views/admin/COGS.svelte";
  import Channels from "views/admin/Channels.svelte";
  import Orders from "views/admin/Orders.svelte";

  import Products from "views/admin/Products.svelte";
  import Inventory from "views/admin/Inventory.svelte";
  import Shipments from "views/admin/Shipments.svelte";
  import FBA from "views/admin/FBA.svelte";

  import Customers from "views/admin/Customers.svelte";
  import Suppliers from "views/admin/Suppliers.svelte";



  import Settings from "views/admin/Settings.svelte";
  import Tables from "views/admin/Tables.svelte";
  import Maps from "views/admin/Maps.svelte";
  
  
  

  export let location;
  export let admin = "";


  let orders_by_day = getOrdersbyDay();
    
  async function getOrdersbyDay() {
      return await fetch('http://137.184.139.204/sales/by-order')
          .then((response) => response.json())
          .then((data) => {
              return data;
      
        });
  }

  let stat

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

</script>


  <div>
    <Sidebar location={location}/>
    <div class="relative md:ml-64 bg-blueGray-100">
      <AdminNavbar />
      <HeaderDatepicker />
      
      <div class="relative bg-blueGray-800 pt-8 pb-16">
        <div class="px-4 md:px-10 mx-auto w-full">
          <div>
            <!-- Card stats -->
            <div class="flex flex-wrap">
              {#each card_stats as stat}
              <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
                <CardStats stat_name={stat['name']} value={stat['value']} />
              </div>
              {/each}
            </div>
          </div>
        </div>
      </div>

      

      {#if location.href.indexOf('/dashboard/') == -1 }
      
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

      {/if}
      <div class="px-4 md:px-10 mx-auto w-full mt-12">
        <Router url="dashboard">
          <Route path="sales" component="{Sales}" />
          <Route path="cogs" component="{COGS}" />
          <Route path="channels" component="{Channels}" />
          <Route path="orders" component="{Orders}" />

          <Route path="products" component="{Products}" />
          <Route path="inventory" component="{Inventory}" />
          <Route path="shipments" component="{Shipments}" />
          <Route path="fba" component="{FBA}" />
          
          <Route path="customers" component="{Customers}" />
          <Route path="suppliers" component="{Suppliers}" />
          

          <Route path="maps" component="{Maps}" />
          <Route path="settings" component="{Settings}" />
          <Route path="tables" component="{Tables}" />
        </Router>
        <FooterAdmin />
      </div>
  </div>
</div>
