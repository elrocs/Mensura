import { createApp } from 'vue'
import App from './App.vue'
import './assets/index.css'
import router from './router/router'

router.beforeEach((to, from, next) => {
    document.title = to.meta.title || 'Default Title'
    next()
  })

createApp(App).use(router).mount('#app')