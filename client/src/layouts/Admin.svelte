<script>
  import { Router, Route } from "svelte-routing";

  // components for this layout
  import AdminNavbar from "components/Navbars/AdminNavbar.svelte";
  import Sidebar from "components/Sidebar/Sidebar.svelte";
  import HeaderStats from "components/Headers/HeaderStats.svelte";
  import FooterAdmin from "components/Footers/FooterAdmin.svelte";
  import CardLineChart from "components/Cards/CardLineChart.svelte";
  import CardBarChart from "components/Cards/CardBarChart.svelte";
  import CardPageVisits from "components/Cards/CardPageVisits.svelte";
  import CardSocialTraffic from "components/Cards/CardSocialTraffic.svelte";



  // pages for this layout
  import Dashboard from "views/admin/Dashboard.svelte";
  import Settings from "views/admin/Settings.svelte";
  import Tables from "views/admin/Tables.svelte";
  import Maps from "views/admin/Maps.svelte";

  export let location;
  export let admin = "";
</script>


  <div>
    <Sidebar location={location}/>
    <div class="relative md:ml-64 bg-blueGray-100">
      <AdminNavbar />
      <HeaderStats />
      

      {#if location.href.indexOf('/admin/') == -1 }
      
      <div class="px-4 md:px-10 mx-auto w-full mt-12">
        <div class="flex flex-wrap">
          <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
            <CardLineChart />
          </div>
        </div>
        <div class="flex flex-wrap mt-4">
          <div class="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
            <CardPageVisits />
          </div>
          <div class="w-full xl:w-4/12 px-4">
            <CardSocialTraffic />
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
