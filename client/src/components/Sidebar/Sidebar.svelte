<script>
  import { link } from "svelte-routing";

  // core components
  import NotificationDropdown from "components/Dropdowns/NotificationDropdown.svelte";
  import UserDropdown from "components/Dropdowns/UserDropdown.svelte";

  let collapseShow = "hidden";

  function toggleCollapseShow(classes) {
    collapseShow = classes;
  }

  export let location;
</script>
<!-- Begin Collapsed Nav -->
<nav
  class="md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-nowrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-20 py-4 px-4"
>
  <div
    class="md:flex-col md:items-stretch md:min-h-full md:flex-nowrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
  >
    <!-- Toggler -->
    <button
      class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
      type="button"
      on:click={() => toggleCollapseShow('bg-white m-2 py-3 px-4')}
    >
      <i class="fas fa-bars"></i>
    </button>
    <!-- Brand -->
    <a
      use:link
      class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-4 px-0"
      href="/"
    >
      Stockboy
    </a>
    <!-- User -->
    <ul class="md:hidden items-center flex flex-wrap list-none">
      <li class="inline-block relative">
        <NotificationDropdown />
      </li>
      <li class="inline-block relative">
        <UserDropdown />
      </li>
    </ul>
    <!-- Collapse -->
    <div
      class="md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded {collapseShow}"
    >
      <!-- Collapse header -->
      <div
        class="md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-blueGray-200"
      >
        <div class="flex flex-wrap">
          <div class="w-6/12">
            <a
              use:link
              class="md:block text-left md:pb-2 text-blueGray-600 mr-0 inline-block whitespace-nowrap text-sm uppercase font-bold p-4 px-0"
              href="/"
            >
              Stockboy
            </a>
          </div>
          <div class="w-6/12 flex justify-end">
            <button
              type="button"
              class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
              on:click={() => toggleCollapseShow('hidden')}
            >
              <i class="fas fa-times"></i>
            </button>
          </div>
        </div>
      </div>
      <!-- Form -->
      <form class="mt-6 mb-4 md:hidden">
        <div class="mb-3 pt-0">
          <input
            type="text"
            placeholder="Search"
            class="border-0 px-3 py-2 h-12 border border-solid border-blueGray-500 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-base leading-snug shadow-none outline-none focus:outline-none w-full font-normal"
          />
        </div>
      </form>

      <!-- Begin Non-Collapsed Nav -->
      <!-- Search -->
      <form
        class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mb-2 p-1"
        >
        <div class="relative flex w-full flex-wrap items-stretch">
          <span
            class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"
          >
            <i class="fas fa-search"></i>
          </span>
          <input
            type="text"
            placeholder="Search here..."
            class="border-1 px-3 py-3 placeholder-blueGray-400 text-blueGray-600 relative bg-white bg-white rounded text-sm shadow outline-none focus:outline-none focus:ring w-full pl-10"
          />
        </div>
      </form>
      <!-- Divider -->
      <hr class="my-4 md:min-w-full" />
      <ul class="md:flex-col md:min-w-full flex flex-col list-none">
        <li class="items-center">
          <a
            use:link
            href="/dashboard"
            class="text-xs uppercase py-3 font-bold block {location.href.indexOf('/dashboard/') == -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-tv mr-2 text-sm {location.href.indexOf('/dashboard/') == -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Dashboard
          </a>
        </li>
      </ul>
      <!-- Divider -->
      <hr class="my-4 md:min-w-full" />
      <!-- Heading -->
      <h6
        class="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
      >
        Sales
      </h6>
      <!-- Navigation -->

      <ul class="md:flex-col md:min-w-full flex flex-col list-none">
        <li class="items-center">
          <a
          use:link
          href="/dashboard/sales"
            class="text-xs uppercase py-3 font-bold block {location.href.indexOf('/dashboard/sales') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-chart-area mr-2 text-sm {location.href.indexOf('/dashboard/sales') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Overview
          </a>
        </li>

        <li class="items-center">
          <a
            use:link
            href="/dashboard/cogs"
            class="text-xs uppercase py-3 font-bold block  {location.href.indexOf('/dashboard/cogs') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-cogs mr-2 text-sm {location.href.indexOf('/dashboard/cogs') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            COGs
          </a>
        </li>

        <li class="items-center">
          <a
            use:link
            href="/dashboard/channels"
            class="text-xs uppercase py-3 font-bold block  {location.href.indexOf('/dashboard/channels') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-chart-bar mr-2 text-sm {location.href.indexOf('/dashboard/channels') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Channels
          </a>
        </li>

        <li class="items-center">
          <a
            use:link
            href="/dashboard/orders"
            class="text-xs uppercase py-3 font-bold block {location.href.indexOf('/dashboard/orders') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-receipt mr-2 text-sm {location.href.indexOf('/dashboard/orders') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Orders
          </a>
        </li>
      </ul>

      <!-- Divider -->
      <hr class="my-4 md:min-w-full" />
      <!-- Heading -->
      <h6
        class="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
      >
        Products
      </h6>
      <!-- Navigation -->

      <ul class="md:flex-col md:min-w-full flex flex-col list-none">
        <li class="items-center">
          <a
            use:link
            href="/dashboard/products"
            class="text-xs uppercase py-3 font-bold block {location.href.indexOf('/dashboard/products') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-shopping-bag mr-2 text-sm {location.href.indexOf('/dashboard/products') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Overview
          </a>
        </li>

        <li class="items-center">
          <a
            use:link
            href="/dashboard/inventory"
            class="text-xs uppercase py-3 font-bold block  {location.href.indexOf('/dashboard/inventory') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-archive mr-2 text-sm {location.href.indexOf('/dashboard/inventory') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Inventory
          </a>
        </li>
        <li class="items-center">
          <a
            use:link
            href="/dashboard/shipments"
            class="text-xs uppercase py-3 font-bold block  {location.href.indexOf('/dashboard/shipments') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-truck mr-2 text-sm {location.href.indexOf('/dashboard/shipments') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Shipments
          </a>
        </li>
        <li class="items-center">
          <a
            use:link
            href="/dashboard/fba"
            class="text-xs uppercase py-3 font-bold block  {location.href.indexOf('/dashboard/fba') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fab fa-amazon mr-2 text-sm {location.href.indexOf('/dashboard/fba') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            FBA
          </a>
        </li>

      </ul>

      <!-- Divider -->
      <hr class="my-4 md:min-w-full" />
      <!-- Heading -->
      <h6
        class="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
      >
        People
      </h6>
      <!-- Navigation -->
      <ul class="md:flex-col md:min-w-full flex flex-col list-none">
        <li class="items-center">
          <a
            use:link
            href="/dashboard/customers"
            class="text-xs uppercase py-3 font-bold block {location.href.indexOf('/dashboard/customers') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-users mr-2 text-sm {location.href.indexOf('/dashboard/customers') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Customers
          </a>
        </li>

        <li class="items-center">
          <a
            use:link
            href="/dashboard/suppliers"
            class="text-xs uppercase py-3 font-bold block  {location.href.indexOf('/dashboard/suppliers') !== -1 ? 'text-red-500 hover:text-red-600':'text-blueGray-700 hover:text-lightBlue-600'}"
          >
            <i
              class="fas fa-parachute-box mr-2 text-sm {location.href.indexOf('/dashboard/suppliers') !== -1 ? 'opacity-75' : 'text-blueGray-700'}"
            ></i>
            Suppliers
          </a>
        </li>

      </ul>

    </div>
  </div>
</nav>
