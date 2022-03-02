<script>
  import { Router, Route } from "svelte-routing";
  

  // components for this layout
  import AdminNavbar from "components/Navbars/AdminNavbar.svelte";
  import Sidebar from "components/Sidebar/Sidebar.svelte";
  import HeaderStats from "components/Headers/HeaderStats.svelte";
  import FooterAdmin from "components/Footers/FooterAdmin.svelte";
  import CardDashboardChart from "components/Cards/CardDashboardChart.svelte";
  import CardPieChart from "../components/Cards/CardPieChart.svelte";
  import CardShortTable from "../components/Cards/CardShortTable.svelte";



  // pages for this layout
  import Dashboard from "views/admin/Dashboard.svelte";
  import Settings from "views/admin/Settings.svelte";
  import Tables from "views/admin/Tables.svelte";
  import Orders from "views/admin/Orders.svelte";
  import Maps from "views/admin/Maps.svelte";
  import HeaderDatepicker from "../components/Headers/HeaderDatepicker.svelte";
  

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


</script>


  <div>
    <Sidebar location={location}/>
    <div class="relative md:ml-64 bg-blueGray-100">
      <AdminNavbar />
      <HeaderDatepicker />
      <HeaderStats />
      

      {#if location.href.indexOf('/admin/') == -1 }
      
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
        <Router url="admin">
          <Route path="dashboard" component="{Dashboard}" />
          <Route path="orders" component="{Orders}" />
          <Route path="maps" component="{Maps}" />
          <Route path="settings" component="{Settings}" />
          <Route path="tables" component="{Tables}" />
        </Router>
        <FooterAdmin />
      </div>
  </div>
</div>
