<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import SearchBar from './components/SearchBar.vue'
import Buttons from './components/Buttons.vue'
import GoogleMap from './components/googleMap.vue';
import StreetView from './components/StreetView.vue';
</script>

<template>
  <header>

    <div class="wrapper">
      <SearchBar />
      <GoogleMap />
      <StreetView />
      <Buttons />
    </div>
  </header>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: inline-block;
  }
}
</style>
