<template>
  <div class="card talk-card" :data-theme="talk.theme">
    <img :src="talk.image" class="card-img-top" >
    <div class="card-body">
      <h5 class="card-title">{{ talk.name }} by {{ talk.speaker}}</h5>
      <p class="card-text">
        <strong>Summary:</strong> {{ talk.summary }}
      </p>
      <a v-if=talk.slides :href="talk.slides"> Slides </a>
      <div class="action-buttons">
        <nuxt-link :to="`/talks/${talk.id}/`" class="btn btn-sm btn-success"> View </nuxt-link>
        <nuxt-link :to="`/talks/${talk.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
        <button @click="onDelete(talk.id)"  class="btn btn-sm btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    props: ["talk", "onDelete"]
};
</script>
<style>
.talk-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
