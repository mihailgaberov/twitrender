<template>
  <div class="results">
    <div class="alert alert-success">From <strong>{{ results.startDate ? results.startDate : '27.05.2017 00:00:00GMT' }}</strong> to <strong>{{ results.endDate ? results.endDate : new Date().toDateString() }}</strong>
      the word <q class="example-quote french-quote">{{ results.word }}</q>" has been twitted
      <strong>{{ results.result }}</strong> times.
    </div>
  </div>
</template>
<script>
export default {
  props: ['results'],
  name: 'Results',
};
</script>

<style scoped>
  .results {
    display: flex;
    align-items: center;
    min-height: 180px;
  }

  .alert {
    margin-top: 1em;
    font-size: 1.3em;
  }

  .french-quote {
    font-weight: bold;
    quotes: "«" "»";
  }

  .example-quote:before {
    content: open-quote;
  }
  .example-quote:after {
    content: close-quote;
  }
</style>
