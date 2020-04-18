<template>
  <div class="controls">
    <div>Choose <i>period.</i></div>
    <label>From</label>
    <b-form-datepicker calendar-width="300"
                       class="datepicker-from"
                       size="lg"
                       v-model="value"
                       :min="min"
                       :max="max"
                       locale="en" />
    <label>To</label>
    <b-form-datepicker size="lg"
                       calendar-width="300"
                       v-model="value"
                       :min="min"
                       :max="max"
                       locale="en" />
    <div class="search-field">
      <b-form-input id="search" type="search" placeholder="Search word here..." size="lg" />
    </div>
    <div>
      <b-button class="search-button" variant="dark" size="lg">Search</b-button>
    </div>


  </div>
</template>

<script>
export default {
  name: 'Controls',
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    // 15th two months prior
    const minDate = new Date(today);
    minDate.setMonth(minDate.getMonth() - 2);
    minDate.setDate(15);
    // 15th in two months
    const maxDate = new Date(today);
    maxDate.setMonth(maxDate.getMonth() + 2);
    maxDate.setDate(15);

    return {
      value: '',
      min: minDate,
      max: maxDate,
    };
  },
};
</script>

<style scoped>
  .search-field {
    margin: 1em 0;
  }

  .search-button {
    width: 100%;
  }
</style>
