<script>
import Admin from "../../layouts/Admin.svelte";


  // core components

  //export let statSubtitle = "Traffic";
  //export let statTitle = "350,897";
  // The value must match one of these strings
  // "up" or "down"
  export let statArrow = "up";
  export let statPercent = "3.48";
  // can be any of the text color utilities
  // from tailwindcss
  export let statPercentColor = "text-emerald-500";
  export let statIconName = "far fa-chart-bar";
  // can be any of the background color utilities
  // from tailwindcss
  export let statIconColor = "bg-red-500";



  export let stat_name = 'sales'
  export let color_reverse = false
  export let days = "30"
  export let value = 0

  const change_color = {
    'negative' : "bg-red-500",
    'positive': "text-emerald-500",
  }

  export let stat_description = "Last "+ days + "days";


  const card_types = {
    'sales': {
      'title': "Gross Sales",
      'icon': "far fa-chart-bar",
      'icon_bg': "bg-emerald-500",
      'prefix': "$",
    },
    'shipping': {
      'title': "Shipping Charged",
      'icon': "fas fa-truck",
      'icon_bg': "bg-teal-500",
      'prefix': "$",
    },
    'discounts': {
      'title': "Discounts",
      'icon': "fas fa-percent",
      'icon_bg': "bg-red-300",
      'prefix': "-$",
    },
    'burn': {
      'title': "Avg. Burn Rate",
      'icon': "fas fa-fire",
      'icon_bg': "bg-red-600",
      'prefix': "",
    },
    'qty': {
      'title': "Quantity Sold",
      'icon': "fas fa-abacus",
      'icon_bg': "bg-orange-300",
      'prefix': "",
    },
    'orders': {
      'title': "Total Orders",
      'icon': "fas fa-cash-register",
      'icon_bg': "bg-orange-300",
      'prefix': "",
    },
    'cancelled': {
      'title': "Cancelled Orders",
      'icon': "fas fa-cash-register",
      'icon_bg': "bg-orange-300",
      'prefix': "",
    },
    'cogs': {
      'title': "Cost of Goods Sold",
      'icon': "fas fa-reciept",
      'icon_bg': "bg-amber-200",
      'prefix': "",
    },
    'profit': {
      'title': "Gross Profit",
      'icon': "fas fa-file-invoice-dollar",
      'icon_bg': "bg-emerald-900",
      'prefix': "",
    },
    'unique_products': {
      'title': "Unique Products Sold",
      'icon': "fas fa-shapes",
      'icon_bg': "bg-orange-300",
      'prefix': "",
    },
    'avg_order_qty': {
      'title': "Avg Order Qty",
      'icon': "fas fa-cart-shopping",
      'icon_bg': "bg-BlueGrey-300",
      'prefix': "",
    },   
    'avg_order_value': {
      'title': "Unique Customers",
      'icon': "fas fa-user",
      'icon_bg': "bg-teal-700",
      'prefix': "",
    },
    'total_inventory': {
      'title': "Total Inventory",
      'icon': "fas fa-boxes-stacked",
      'icon_bg': "bg-Amber-800",
      'prefix': "",
    },   
    'inventory_value': {
      'title': "Inventory Value",
      'icon': "fas fa-hand-holding-dollar",
      'icon_bg': "bg-teal-600",
      'prefix': "$",
    },
    'inventory_days': {
      'title': "Inventory Days",
      'icon': "fas fa-calendar-days",
      'icon_bg': "bg-indego-500",
      'prefix': "",
    },   
    'inventory_days': {
      'title': "Inventory Days",
      'icon': "fas fa-calendar-days",
      'icon_bg': "bg-indego-500",
      'prefix': "",
    },
    'cost_per_day': {
      'title': "Cost Per Day",
      'icon': "fas fa-chart-pie",
      'icon_bg': "bg-red-500",
      'prefix': "",
    },
    'unique_customers': {
      'title': "Unique Customers",
      'icon': "fas fa-user",
      'icon_bg': "bg-pink-500",
      'prefix': "",
    },
    'repeat_customers': {
      'title': "Repeat Customers",
      'icon': "fas fa-user",
      'icon_bg': "bg-pink-500",
      'prefix': "",
    },
  }


</script>

<div
  class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
>
  <div class="flex-auto p-4">
    <div class="flex flex-wrap">
      <div class="relative w-full pr-4 max-w-full flex-grow flex-1">
        <h5 class="text-blueGray-400 uppercase font-bold text-xs">
          {card_types[stat_name]['title']}
        </h5>
        <span class="font-semibold text-xl text-blueGray-700">
          {value}
        </span>
      </div>
      <div class="relative w-auto pl-4 flex-initial">
        <div
          class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full {card_types[stat_name]['icon_bg']}"
        >
          <i class="{card_types[stat_name]['icon']}"></i>
        </div>
      </div>
    </div>
    <p class="text-sm text-blueGray-400 mt-4">
      <span class="mr-2 {statPercentColor}">
        <i
          class="{statArrow === 'up' ? 'fas fa-arrow-up' : 'fas fa-arrow-down'}"
        ></i>
        {statPercent}%
      </span>
      <span class="whitespace-nowrap">{stat_description}</span>
    </p>
  </div>
</div>
