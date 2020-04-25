<template>
  <div class="controls">
    <div class="choose-period">Choose <i>period.</i></div>
    <label>From</label>
    <b-form @submit="onSubmit">
      <b-form-datepicker calendar-width="300"
                         class="datepicker-from"
                         size="lg"
                         v-model="searchForm.startDate"
                         today-button
                         reset-button
                         :min="min"
                         :max="max"
                         locale="en" />
      <label>To</label>
      <b-form-datepicker size="lg"
                         calendar-width="300"
                         v-model="searchForm.endDate"
                         today-button
                         reset-button
                         :min="min"
                         :max="max"
                         locale="en" />
      <div class="search-field">
        <b-form-input type="search"
                      placeholder="Search word here..."
                      size="lg"
                      v-model="searchForm.word" />
      </div>
      <div>
        <b-button type="submit" class="search-button" variant="dark" size="lg">Search</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Controls',
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const minDate = new Date(2017, 4, 27);
    const maxDate = new Date(today);

    return {
      value: '',
      min: minDate,
      max: maxDate,
      searchForm: {
        word: '',
        startDate: '',
        endDate: '',
      },
    };
  },
  methods: {
    search(word = '', startDate = '', endDate = '') {
      if (!word) return;

      // const path = /search/${word}?start_date=${startDate}&end_date=${endDate}
      let path = `http://localhost:5000/search/${word}`;

      if (startDate && endDate) {
        path = `http://localhost:5000/search/${word}?start_date=${startDate}&end_date=${endDate}`;
      } else if (startDate && !endDate) {
        path = `http://localhost:5000/search/${word}?start_date=${startDate}`;
      } else if (!startDate && endDate) {
        path = `http://localhost:5000/search/${word}?end_date=${endDate}`;
      }

      axios
        .get(path)
        .then((res) => {
          console.log('>>> res', res);
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.error(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.search(this.searchForm.word, this.searchForm.startDate, this.searchForm.endDate);
    },
  },
};
</script>

<style scoped>
  .choose-period {
    color: dimgray;
    font-weight: bold;
    font-size: 1.8em;
  }

  .search-field {
    margin: 1em 0;
  }

  .search-button {
    width: 100%;
  }
</style>
