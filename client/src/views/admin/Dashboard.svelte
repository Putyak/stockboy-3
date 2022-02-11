<script>
  // core components
  import CardLineChart from "components/Cards/CardLineChart.svelte";
  import CardPageVisits from "components/Cards/CardDatatable.svelte";
  export let location;
</script>

<div>
  <div class="flex flex-wrap">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      <CardLineChart />
    </div>
  </div>
  <div class="flex flex-wrap mt-4">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      <CardPageVisits />
    </div>
  </div>
</div>
