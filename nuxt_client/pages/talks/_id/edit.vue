<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ talk.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img v-if="!preview" class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="talk.image">
        <img v-else class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="preview">
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitTalk">
          <div class="form-group">
            <label for>Talk Name</label>
            <input type="text" class="form-control" v-model="talk.name" >
          </div>
		  <div class="form-group">
            <label for>Speaker</label>
            <input type="text" class="form-control" v-model="talk.speaker">
          </div>
          <div class="form-group">
            <label for>Summary</label>
            <input type="text" v-model="talk.summary" class="form-control" name="summary" >
          </div>
          <div class="form-group">
            <label for>Talk image</label>
            <input type="file" @change="onFileChange">
          </div>
          <div class="form-group">
            <label for>Slides</label>
            <input v-model="talk.slides" type="text" class="form-control" name="slides">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Theme</label>
                <select v-model="talk.theme" class="form-control" >
                  <option value="Vue">Vue</option>
                  <option value="A11y">A11y</option>
                  <option value="Serverless">Serverless</option>
                  <option value="How we work">How we work</option>
				  <option value="Webpack">Webpack</option>
                  <option value="Svelte">Svelte</option>
                  <option value="Design">Design</option>
				  <option value="Nuxt">Nuxt</option>
                  <option value="WebAssembly">WebAssembly</option>
                  <option value="Audio">Audio</option>
                  <option value="Vue3">Vue3</option>
				  <option value="Climate">Climate</option>
                  <option value="Test">Test</option>
				  <option value="Vuex">Vuex</option>
                  <option value="Architecture">Architecture</option>
                </select>
              </div>
            </div>
          </div>
          <button type="submit" class="btn btn-success">Save</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head(){
      return {
        title: "Edit Talk"
      }
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
        summary: ""
      },
      preview: ""
    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.talk.image = files[0];
	  this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitTalk() {
	  let editedTalk = this.talk;
	  if (editedTalk.image.name == undefined) {
		  delete editedTalk["image"]
	  }
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedTalk) {
        formData.append(data, editedTalk[data]);
      }
      try {
        let response = await this.$axios.$patch(`/talks/${editedTalk.id}/`, formData, config);
        this.$router.push("/talks/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
</style>
