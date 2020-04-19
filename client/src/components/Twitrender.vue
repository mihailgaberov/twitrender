<template>
  <div class="container">
    <Headline />
    <Carousel />
<!--    <Results />-->
    <Controls />
  </div>
</template>

<script>
import Headline from './Headline.vue';
import Carousel from './Carousel.vue';
// import Results from './Results.vue';
import Controls from './Controls.vue';

export default {
  name: 'Twitrender',
  components: {
    Controls, Headline, Carousel,
  },
};
</script>

<style scoped>

</style>
