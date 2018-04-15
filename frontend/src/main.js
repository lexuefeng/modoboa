import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/lib/buefy.css'
import '@mdi/font/css/materialdesignicons.css'

import Cookies from 'js-cookie'

import App from './App'
import router from './router'
import store from './store'

Vue.use(Buefy)

Vue.config.productionTip = false

/* Deal with django CSRF protection */
let csrftoken = Cookies.get('csrftoken')
Vue.http.headers.common['X-CSRFTOKEN'] = csrftoken

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: { App },
    template: '<App/>'
})
