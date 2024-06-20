import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css';

import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'

import axios from 'axios';
import VueCookies from 'vue-cookies';

import router from './router'

// Include CSRF token in your requests
const csrfToken = VueCookies.get('csrftoken');
axios.defaults.headers.common['X-CSRFToken'] = csrfToken;

const app = createApp(App)

app.use(ElementPlus);

app.use(createPinia())
app.use(router)

app.use(ElementPlus)

app.mount('#app')


// <template>
//   <el-button :plain="true" @click="open2">success</el-button>
//   <el-button :plain="true" @click="open3">warning</el-button>
//   <el-button :plain="true" @click="open1">message</el-button>
//   <el-button :plain="true" @click="open4">error</el-button>
// </template>

// <script lang="ts" setup>
// import { ElMessage } from 'element-plus'

// const open1 = () => {
//   ElMessage('this is a message.')
// }
// const open2 = () => {
//   ElMessage({
//     message: 'Congrats, this is a success message.',
//     type: 'success',
//   })
// }
// const open3 = () => {
//   ElMessage({
//     message: 'Warning, this is a warning message.',
//     type: 'warning',
//   })
// }
// const open4 = () => {
//   ElMessage.error('Oops, this is a error message.')
// }
// </script>




