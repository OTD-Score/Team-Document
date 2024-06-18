<template>
  <div id="app">
    <top-nav></top-nav>
    <router-view />
  </div>
    
</template>

<script>
import topNav from '@/components/top-nav/top-nav.vue'

export default {
  name: 'App',
  components: {
    'top-nav' : topNav,
  }
}
</script>
  
  
<style>
  body{
    margin: 0;
  }
  #app{
    width:100%;
    height:100%;
    font-size:16px;
    background:white;
    box-sizing: content-box;

  }
  </style>