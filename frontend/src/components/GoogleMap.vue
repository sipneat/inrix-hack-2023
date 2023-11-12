<template>
  <div class="map">
    <GoogleMap api-key="AIzaSyBKpiq156O3XjKxdWvoEeSOWwqeX_ZNW5c" style="width: 550px; height: 950px; margin-left: 210px; padding-top: 350px; position: absolute;" :center="center" :zoom="15">
      <MarkerCluster>
      <Marker v-for="(location, i) in locations" :options="{ position: location }" :key="i" />
    </MarkerCluster>
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

let locations = [];

async function callProcessData(adr, rad) {
  const response = await fetch(`http://localhost:5000/processData?address=${adr}&radius=${rad}`)
  const data = await response.json();

  return data;
}

async function callLatLon(adrs) {
  const response = await fetch(`http://localhost:5000/adrToLatLon/${adrs}`)
  const data = await response.json();

  return data;
}

function generatePoints(adr, rad) { 
  const rawData = callProcessData(adr, rad);

  for (let i = 0; i < Object.keys(rawData).length; i++) {
    latLon = callLatLon(result[i]["name"]);
    locations.push({
      lat: latLon[0],
      lng: latLon[1],
    });

  }
}

export default defineComponent({
  props: { adr: String, rad: Number },
  components: { GoogleMap, Marker },
  setup() {
    let lati = 37.7680183;
    let long = -122.3878772;
    const center = { lat: lati, lng: long };

    const adr = "1 Warriors Way San Francisco";
    const rad = 0.2;
    generatePoints(adr, rad);

    return { center, locations };
  },
});
</script>