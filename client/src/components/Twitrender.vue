<template>
  <div class="container">
    <Headline />
    <Carousel v-if="searchResults === ''" />
    <Results v-if="searchResults !== ''" :results="searchResults" />
    <Controls />
  </div>
</template>

<script>
import Headline from './Headline.vue';
import Carousel from './Carousel.vue';
import Results from './Results.vue';
import Controls from './Controls.vue';

export default {
  name: 'Twitrender',
  data() {
    return {
      searchResults: '',
    };
  },
  components: {
    Controls, Carousel, Headline, Results,
  },
  methods: {
    showResults(res) {
      if (res.data !== '') {
        this.searchResults = res.data;
      }
    },
  },
};
</script>

<style scoped>

</style>
