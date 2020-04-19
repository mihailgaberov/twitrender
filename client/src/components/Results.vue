<template>
  <div class="results">
    <div class="alert alert-success">From <strong>22.10.2017</strong> to <strong>16.06.2018</strong>
      the word <q class="example-quote french-quote">javascript</q>" has been twitted
      <strong>777</strong> times.
    </div>
  </div>
</template>
<script>
export default {
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
