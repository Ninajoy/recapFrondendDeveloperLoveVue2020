<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>All Talks</h3>
          <nuxt-link to="/talks/add" class="btn btn-info">Add talk</nuxt-link>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="d-inline-flex flex-row justify-content-around flex-wrap mb-5">
        <template v-for="theme in themes" class="filter">
          <div :key="theme.id">
            <filter-button :filterByTheme="filterByTheme" :theme="theme" ></filter-button>
          </div>
        </template>
        </div>
      </div>
    </div>
    <div class="row">
      <template v-for="talk in talks">
        <div :key="talk.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <talk-card :onDelete="deleteTalk" :talk="talk"></talk-card>
        </div>
      </template>
    </div>
  </main>
</template>
<script>
import talkCard from "~/components/talkCard.vue";
import filterButton from "~/components/filterButton.vue";
import filter from "lodash/filter";

export default {
  head() {
    return {
      title: "talks list"
    };
  },
  components: {
    talkCard,
    filterButton
  },
  async asyncData({$axios, params}) {
    try {
      let talks = await $axios.$get('/talks/');
      let options = await $axios.$options('/talks/');
      let themes = options.actions.POST.theme.choices;
      return { talks, themes };
    } catch (e) {
      console.log(e);
      return { talks : [], options : [] };
    }
  },
  data() {
    return {
      talks: [],
      options: [],
      themes: []
    };
  },
  methods: {
    async deleteTalk(talk_id) {
      try {
        await this.$axios.$delete(`/talks/${talk_id}/`);
        let newTalks = await this.$axios.$get('/talks/');
        this.talks = newTalks;
      } catch (e) {
        console.log(e);
      }
    },
    async filterByTheme(e) {
      let selectedTheme = e.currentTarget.dataset.filter;
      let tofilterTalks = await this.$axios.$get('/talks/');
      let filteredTalks = filter(tofilterTalks, (talk) =>
        talk.theme === selectedTheme
      )
      this.talks = filteredTalks;
    }
  }
};
</script>
<style scoped>
</style>
