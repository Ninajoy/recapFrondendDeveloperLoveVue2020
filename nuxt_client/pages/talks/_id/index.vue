<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ talk.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="talk.image"
          alt
        />
      </div>
      <div class="col-md-6">
        <div class="talk-details">
          <h4>Speaker</h4>
          <p>{{ talk.speaker }}</p>
          <h4>Theme</h4>
          <p>{{ talk.theme }}</p>
          <h4>Summary</h4>
          <textarea class="form-control" rows="10" v-html="talk.summary" disabled />
          <a v-if="talk.slides" :href="talk.slides">Slides</a>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "View Talk"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let talk = await $axios.$get(`/talks/${params.id}`);
      return { talk };
    } catch (e) {
      return { talk: [] };
    }
  },
  data() {
    return {
      talk: {
        name: "",
        image: "",
        speaker: "",
        theme: "",
        summary: "",
        slides: ""
      }
    };
  }
};
</script>
<style scoped>
</style>
