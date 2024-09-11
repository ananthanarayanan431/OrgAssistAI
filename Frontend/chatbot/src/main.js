

import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router/route'

import { createAuth0 } from '@auth0/auth0-vue'

const app = createApp(App)
app.use(createPinia())
app.use(router)

// app.use(
//     createAuth0({
//         domain:"dev-6w26jkstvqmcs81o.us.auth0.com",
//         clientId:"1fl0VhqrqZumOEYuIxFGe61VQIo0Ge1D",
//         authorizationParams: {
//             redirect_uri:'http://localhost:5173'
//         },
//         onRedirectCallback: (appState) => {
//             console.log('Redirect callback triggered', appState);
//             router.push(appState && appState.targetUrl ? appState.targetUrl : window.location.pathname);
//         },
//         cacheLocation: 'localstorage'
//     })
// )
app.mount('#app')

// app.config.errorHandler = (err, vm, info) => {
//     console.error('Global error:', err, info);
// };