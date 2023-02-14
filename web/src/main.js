import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "./assets/main.css";

import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faRecycle } from '@fortawesome/free-solid-svg-icons';
import { faGears } from '@fortawesome/free-solid-svg-icons';
import { faHouse } from '@fortawesome/free-solid-svg-icons';
import { faChartLine } from '@fortawesome/free-solid-svg-icons';
import { faSignal } from '@fortawesome/free-solid-svg-icons';


library.add(faRecycle);
library.add(faGears);
library.add(faHouse);
library.add(faChartLine);
library.add(faSignal);

const app = createApp(App)
    .component('font-awesome-icon', FontAwesomeIcon);

app.use(router);

app.mount("#app");
