<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import SearchBar from './components/SearchBar.vue'
import Buttons from './components/Buttons.vue'
import GoogleMap from './components/googleMap.vue';
import StreetView from './components/StreetView.vue';
import MainPage from './components/MainPage.vue'
</script>

<template>
  <MainPage />
  <Suspense>
  <GoogleMap />
  </Suspense>
</template>
