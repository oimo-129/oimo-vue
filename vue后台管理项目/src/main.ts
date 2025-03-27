//入口函数
import { createApp } from 'vue'
//ElementPlus 
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import Bpp from '@/Bpp.vue'  
//引入模板全局样式
import '@/styles/index.scss'

// 使用ElementPlus
const app = createApp(Bpp)

// 使用ElementPlus
app.use(ElementPlus, {
  locale: zhCn,
})
//在ts文件里面配置，入口文件导入
import 'virtual:svg-icons-register'
// 全局注册这个组件
import SvgIcon from '@/components/SvgIcon/index.vue'
//全局组件配置
import  globleComponent from '@/components'
//使用
app.use(globleComponent)

// svg 
app.component('SvgIcon',SvgIcon)

// 挂载应用
app.mount('#app')