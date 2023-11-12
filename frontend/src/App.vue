<script setup>
import GoogleMap from './components/googleMap.vue';
import MainPage from './components/MainPage.vue';
</script>

<template>
  <MainPage />
  <Suspense>
  <GoogleMap />
  </Suspense>
</template>
