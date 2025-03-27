<template>
  <svg :width="size" :height="size">
    <use :xlink:href="prefix + name" :fill="color" :stroke="color"></use>
  </svg>
</template>
  
<script setup>
// 接收父组件传递来的参数
defineProps({
  // xlink属性值前缀
  prefix: {
    type: String,
    default: '#icon-'
  },
  // 提供使用图标的名字
  name: String,
  color: {
    type: String,
    default: 'green'
  },
  size: {
    type: [String, Number],
    default: '5em'
  }
})
</script>

<style scoped>
svg {
  vertical-align: middle;
}
</style>