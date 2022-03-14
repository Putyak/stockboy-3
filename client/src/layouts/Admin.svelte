<script>
  import { Router, Route } from "svelte-routing";
  

  // components for this layout
  import AdminNavbar from "components/Navbars/AdminNavbar.svelte";
  import Sidebar from "components/Sidebar/Sidebar.svelte";
  import FooterAdmin from "components/Footers/FooterAdmin.svelte";

  // pages for this layout
  import Dashboard from "views/admin/Dashboard.svelte";

  import Sales from "views/admin/Sales.svelte";
  import COGS from "views/admin/COGS.svelte";
  import Channels from "views/admin/Channels.svelte";
  
  import Orders from "views/admin/orders/OrdersIndex.svelte";
  import Order from "views/admin/orders/OrderID.svelte";

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



</script>


  
    <Sidebar location={location}/>
    
    <div class="relative md:ml-64 bg-blueGray-100">
      <AdminNavbar />
      
      
      {#if location.href.indexOf('/dashboard/') == -1 }
        <Dashboard />
      {/if}

      
        <Router url="dashboard">
          <Route path="sales" component="{Sales}" />
          <Route path="cogs" component="{COGS}" />
          <Route path="channels" component="{Channels}" />

          <Route path="orders" component="{Orders}" />
          <Route path="orders/:id" component="{Order}" />

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
