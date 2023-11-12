<template>
  <div class="map">
    <GoogleMap api-key="AIzaSyBKpiq156O3XjKxdWvoEeSOWwqeX_ZNW5c" style="width: 25vw; height: 25vh" :center="center" :zoom="15">
      <Marker :options="{ position: center }" />
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

export default defineComponent({
  components: { GoogleMap, Marker },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };

    return { center };
  },
});
</script>