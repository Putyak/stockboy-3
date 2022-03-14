<script>
  // core components
  import CardLineChart from "components/Cards/CardLineChart.svelte";
  import CardSimpleDatatable from "../../components/Cards/CardSimpleDatatable.svelte";
  export let location;
  import CardStat from "components/Headers/CardStat.svelte";

  import HeaderDatepicker from "components/Headers/HeaderDatepicker.svelte";
  
    /// Replace with Stats Requests

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

<HeaderDatepicker />

<!-- Header Stats -->
<div class="relative bg-blueGray-800 pt-8 pb-16 mb-8">
  <div class="px-4 md:px-10 mx-auto w-full ">
    <div>
      <!-- Card stats -->
      <div class="flex flex-wrap">
        {#each card_stats as stat}
        <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
          <CardStat stat_name={stat['name']} value={stat['value']} />
        </div>
        {/each}
      </div>
    </div>
  </div>
</div>
<div>
  <div class="flex flex-wrap">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      <CardLineChart />
    </div>
  </div>
  <div class="flex flex-wrap mt-4">
    <div class="w-full xl:w-12/12 mb-12 xl:mb-0 px-4">
      <CardSimpleDatatable />
    </div>
  </div>
</div>
