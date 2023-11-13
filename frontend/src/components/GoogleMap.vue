<template>
  <div class="map">
    <GoogleMap api-key="KEY" style="width: 550px; height: 950px; margin-left: 210px; padding-top: 350px; position: absolute;" :center="center" :zoom="15">
      <Marker v-for="(location, i) in locations" :options="{ position: location }" @click="handleClick(`${i}`)" />
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

var locations = [];
var names = [];
var costs = [];
var dists = [];
var prob = [];

function getDistanceBetweenPoints(latitude1, longitude1, latitude2, longitude2, unit = 'miles') {
    let theta = longitude1 - longitude2;
    let distance = 60 * 1.1515 * (180/Math.PI) * Math.acos(
        Math.sin(latitude1 * (Math.PI/180)) * Math.sin(latitude2 * (Math.PI/180)) + 
        Math.cos(latitude1 * (Math.PI/180)) * Math.cos(latitude2 * (Math.PI/180)) * Math.cos(theta * (Math.PI/180))
    );
    if (unit == 'miles') {
        return distance.toFixed(2);
    } else if (unit == 'kilometers') {
        return Math.round(distance * 1.609344, 2);
    }
}

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
      costs.push({cost: "N/A"});
    else
      costs.push({cost: rawData[i]["amenities"][0]["name"]});

    dists.push({ dist: getDistanceBetweenPoints(latLon[0], latLon[1], homeLat, homeLon)});

    if (rawData[i]["probability"] == null)
      prob.push({prob: "N/A"});
    else
      prob.push({prob: rawData[i]["probability"]});
}
}

let adr = "1 warriors way san francisco";
let rad = 0.2;

export default defineComponent({
  components: { GoogleMap, Marker },
  data() {
        return {
            name: "",
            cost: "",
            dist: "",
            prob: ""
        };
    },
    mounted() { 
    this.emitter.on("search", ({adr, rad}) => {
      console.log(adr);
      console.log(rad);
      this.removeMarker(10);
    });
  },
    methods: {
        handleClick(arg) {
        const clickedName = names[arg];
        console.log(clickedName);
        const clickedCost = costs[arg];
        console.log(clickedCost);
        const clickedDist = dists[arg];
        console.log(clickedDist);
        const clickedProb = prob[arg];
        console.log(clickedProb);
        this.emitter.emit('handleClick', { name: clickedName, cost: clickedCost, dists: clickedDist, prob: clickedProb });
        }
    },
  async setup() {
    let lati = 37.7680183;
    let long = -122.3878772;
    const center = { lat: lati, lng: long };

    await generatePoints(adr, rad);
    console.log(locations);
    console.log(names);
    console.log(costs);
    console.log(dists);
    

    return { center, locations };
  },
});


</script>