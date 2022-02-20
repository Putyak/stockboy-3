<script>
  // core components
  import Flatpickr from "svelte-flatpickr";
  import "flatpickr/dist/flatpickr.css";
  import "flatpickr/dist/themes/dark.css";
	
  let value, formattedValue;

	const options = {
		enableTime: false,
    mode: "range",
    maxDate: "today",
    dateFormat:"m/d/y",
    defaultDate: ["2022-1-14", "2022-2-14"],
    allowInput: true,

		onChange(selectedDates, dateStr) {
			console.log('flatpickr hook', selectedDates, dateStr);
		}
	};

	$: console.log({ value, formattedValue });

	function handleChange(event) {
		const [ selectedDates, dateStr ] = event.detail;
		console.log({ selectedDates, dateStr });
	}

	function handleSubmit(event) {
		event.preventDefault();

		console.log(event.target.elements['date'].value);
	}
</script>

<!-- Datepicker -->
<div class="bg-blueGray-800 md:pt-32 pt-12 flex justify-end px-4">
  <div class="px-4 md:px-10">
    <div>
      <form on:submit={handleSubmit}>
        <Flatpickr {options} bind:value bind:formattedValue on:change={handleChange} name="date" autocomplete="off" placeholder="1/14/2022 to 2/14/2022" />
    
        <button class="bg-lightBlue-600 px-4 py-2 text-white drop-shadow-md hover:bg-lightBlue-900 focus:outline-none" type="submit">
          Go
        </button>
      </form>
    </div>
  </div>
</div>
