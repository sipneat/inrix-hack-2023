<template>
  <div class="map">
    <GoogleMap api-key="AIzaSyBKpiq156O3XjKxdWvoEeSOWwqeX_ZNW5c" style="width: 550px; height: 950px; margin-left: 210px; padding-top: 350px; position: absolute;" :center="center" :zoom="15">
      <Marker v-for="(location, i) in locations" :options="{ position: location, label: `${i}` }" @click="() => handleClick(`${i}`)" />
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

var locations = [];
var names = [];
var cost = [];
var dist = [];

function getDistanceBetweenPoints(latitude1, longitude1, latitude2, longitude2, unit = 'miles') {
    let theta = longitude1 - longitude2;
    let distance = 60 * 1.1515 * (180/Math.PI) * Math.acos(
        Math.sin(latitude1 * (Math.PI/180)) * Math.sin(latitude2 * (Math.PI/180)) + 
        Math.cos(latitude1 * (Math.PI/180)) * Math.cos(latitude2 * (Math.PI/180)) * Math.cos(theta * (Math.PI/180))
    );
    if (unit == 'miles') {
        return Math.round(distance, 5);
    } else if (unit == 'kilometers') {
        return Math.round(distance * 1.609344, 2);
    }
}

async function callProcessData(adr, rad) {
  const response = await fetch(`http://127.0.0.1:5000/processData?address=${adr}&radius=${rad}`)
  const data = await response.json();

  return data;
}

async function callLatLon(adrs) {
  const response = await fetch(`http://127.0.0.1:5000/adrToLatLon/${adrs}`)
  const data = await response.json();

  return data;
}

async function generatePoints(adr, rad) { 
  const rawData = await callProcessData(adr, rad);
  const home = await callLatLon(adr + " san francisco");
  const homeLat = home[0];
  const homeLon = home[1];

  for (let i = 0; i < rawData.length; i++) {
    let latLon = await callLatLon(rawData[i]["name"] + " san francisco");

    locations.push({
      lat: latLon[0],
      lng: latLon[1],
    });

    names.push({name: rawData[i]["name"]});

    if (rawData[i]["amenities"][0] == undefined)
      cost.push({cost: "N/A"});
    else
      cost.push({cost: rawData[i]["amenities"][0]["name"]});

    dist.push({ dist: getDistanceBetweenPoints(latLon[0], latLon[1], homeLat, homeLon)});
}
}

export default defineComponent({
  props: { adr: String, rad: Number },
  components: { GoogleMap, Marker },
  async setup() {
    let lati = 37.7680183;
    let long = -122.3878772;
    const center = { lat: lati, lng: long };

    const handleClick = (arg) => {
      // Handle marker click here
      console.log(locations[arg]);
      console.log(names[arg]);
      console.log(cost[arg]);
      console.log(dist[arg]);
    };

    const adr = "1 Warriors Way San Francisco";
    const rad = 0.5;
    await generatePoints(adr, rad);
    console.log(locations);
    console.log(names);
    console.log(cost);
    console.log(dist);

    return { center, locations, handleClick };
  },
});


</script>