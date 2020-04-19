<template>
  <div class="carousel-area">
    <div class="broadcast alert alert-success">
      <carousel :data="data" :controls="false" :indicators="false" :interval="3000" direction="up"></carousel>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          id: 1,
          searchedWord: 'React',
          message: 'Did you know that the most searched word during Christmas 2018 is',
          content(createElement, content) {
            return createElement('span', {
              class: 'broadcast-content',
            }, [
              createElement('span', [`${content.message} ${content.searchedWord}`]),
            ]);
          },
        },
        {
          id: 2,
          searchedWord: 'JavaScript',
          message: 'Did you know that the most searched word for 2019 is',
          content(createElement, content) {
            return createElement('span', {
              class: 'broadcast-content',
            }, [
              createElement('span', [`${content.message} ${content.searchedWord}`]),
            ]);
          },
        },
        {
          id: 3,
          searchedWord: 'TDD',
          message: 'Did you know that the most searched word during Christmas 2018 is',
          content(createElement, content) {
            return createElement('span', {
              class: 'broadcast-content',
            }, [
              createElement('span', [`${content.message} ${content.searchedWord}`]),
            ]);
          },
        },
      ],
    };
  },
};
</script>

<style scoped>
  .carousel-area {
    display: flex;
    min-height: 180px;
  }

  .broadcast {
    border: 1px solid #eee;
    border-radius: 0.25rem;
    display: flex;
    padding: 0.5rem 0.75rem;
    font-size: 1.3em;
    align-items: center;
  }

  .broadcast > .carousel {
    flex: 1;
  }

  .broadcast-content {
    align-items: center;
    display: flex;
    justify-content: space-between;
  }
</style>
