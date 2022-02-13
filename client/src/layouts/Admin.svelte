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
  import Maps from "views/admin/Maps.svelte";
  import HeaderDatepicker from "../components/Headers/HeaderDatepicker.svelte";
  

  export let location;
  export let admin = "";
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
            <CardDashboardChart />
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
          <Route path="settings" component="{Settings}" />
          <Route path="tables" component="{Tables}" />
          <Route path="maps" component="{Maps}" />
        </Router>
        <FooterAdmin />
      </div>
  </div>
</div>
