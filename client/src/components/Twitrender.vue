<template>
  <div class="container">
    <Headline />
    <Results />
    <Controls />
  </div>
</template>

<script>
import Headline from './Headline.vue';
import Results from './Results.vue';
import Controls from './Controls.vue';

export default {
  name: 'Twitrender',
  components: { Controls, Results, Headline },
};
</script>

<style scoped>

</style>
