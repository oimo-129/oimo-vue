import { App } from 'vue'
import SvgIcon from './SvgIcon/index.vue'
import Pagination from './Pagination/index.vue'

// 给allComponents添加类型定义
interface Components {
  [key: string]: any;  // 添加索引签名
  SvgIcon: typeof SvgIcon;
  Pagination: typeof Pagination;
}

const allComponents: Components = {
    SvgIcon,
    Pagination
}
  



console.log("单个对组件进行打印：",SvgIcon,Pagination)
console.log(Object.keys(allComponents))
console.log("全部组件分类：",allComponents)

export default {
  install(app:App){
    //注册项目全部为全局部件
    Object.keys(allComponents).forEach(
        key =>{
        app.component(key,allComponents[key])
        }
    )
  }
}