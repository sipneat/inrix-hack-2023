import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import VueGoogleMaps from '@fawmi/vue-google-maps'

const app = createApp(App);
app.use(VueGoogleMaps, {
    load: {
        key: 'AIzaSyBKpiq156O3XjKxdWvoEeSOWwqeX_ZNW5c',
        // language: 'de',
    },
}).mount('#app')


createApp(App).mount('#app')
