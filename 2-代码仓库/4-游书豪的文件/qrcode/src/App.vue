<template>
    <list></list>
</template>

<script>
import list from '@/views/list/index.vue'

export default {
  name: 'App',
  components: {
    list
  }
}
</script>

<style>
html{
  height: 100%;
  background-color: rgb(241, 241, 241);
  overflow-y: scroll;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  box-sizing: border-box;
}
</style>
