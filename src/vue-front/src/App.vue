<template>
  <div id="app">
    <router-view></router-view>
    <footer>
      For more instructions and codes, view
      <a href="https://github.com/">GitHub</a>.
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}
footer {
  text-align: center;
  margin: 20px 0px;
}
</style>
