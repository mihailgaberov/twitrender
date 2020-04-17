<template>
  <div class="controls">
    <label>Choose <i>period.</i></label>
    <b-form-datepicker v-model="value" :min="min" :max="max" locale="en"></b-form-datepicker>
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

</style>
