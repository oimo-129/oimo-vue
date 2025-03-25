//入口函数
import { createApp } from 'vue'

//ElementPlus 
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import App from './App.vue'  // 暂时使用相对路径避免别名问题

const app = createApp(App)

// 使用ElementPlus
app.use(ElementPlus, {
  locale: zhCn,
})

// 挂载应用
app.mount('#app')