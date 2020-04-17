<template>
  <div class="container">
    <Headline />
    <Results />
  </div>
</template>

<script>
import Headline from './Headline.vue';
import Results from './Results.vue';

export default {
  name: 'Twitrender',
  components: { Results, Headline },
};
</script>

<style scoped>

</style>
