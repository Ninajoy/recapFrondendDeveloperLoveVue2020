<template>
  <header>
    <div class="text-box">
      <h1>Frontend Developer Love / Vuejs 🤓</h1>
      <p class="mt-3">Talks we loved ❤️ ️Amsterdam 2020</p>
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/talks">
        View Talks <span class="ml-2">&rarr;</span>
      </nuxt-link>
    </div>
  </header>
</template>
<script>

export default {
  head() {
    return {
      title: "Home page"
    };
  }
};
</script>
<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.9),
      rgba(0, 0, 0, 0.4)
    ),
    url("/images/vuejslight.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-size: 5rem;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
