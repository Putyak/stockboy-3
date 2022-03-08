<script>
  // core components
  import CardStats from "components/Cards/CardStats.svelte";
  
  
  export let card_data

</script>

<!-- Header -->
<div class="relative bg-blueGray-800 pt-8 pb-16">
  <div class="px-4 md:px-10 mx-auto w-full">
    <div>
      <!-- Card stats -->
      <div class="flex flex-wrap">
        <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
          <CardStats
            statSubtitle="Gross Sales"
            statTitle="$50,897"
            statArrow="up"
            statPercent="3.48"
            statPercentColor="text-emerald-500"
            statDescripiron="Since last /x/ days"
            statIconName="far fa-chart-bar"
            statIconColor="bg-emerald-500"
          />
        </div>
        <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
          <CardStats
            statSubtitle="Shipping Charged"
            statTitle="$2,356"
            statArrow="down"
            statPercent="3.48"
            statPercentColor="text-red-500"
            statDescripiron="Since last /x/ days"
            statIconName="fas fa-truck"
            statIconColor="bg-teal-500"
          />
        </div>
        <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
          <CardStats
            statSubtitle="Discounts"
            statTitle="-$924"
            statArrow="down"
            statPercent="1.10"
            statPercentColor="text-orange-500"
            statDescripiron="Since last /x/ days"
            statIconName="fas fa-percent"
            statIconColor="bg-orange-300"
          />
        </div>
        <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
          <CardStats
            statSubtitle="Avg. Burn Rate"
            statTitle="38.2"
            statArrow="up"
            statPercent="12"
            statPercentColor="text-emerald-500"
            statDescripiron="Since last /x/ days"
            statIconName="fas fa-fire"
            statIconColor="bg-red-600"
          />
        </div>
      </div>
    </div>
  </div>
</div>
