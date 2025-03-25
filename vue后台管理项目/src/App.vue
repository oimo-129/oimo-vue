<template>
  <el-button type="primary" size="default" @click="">
    测试按钮
  </el-button>

  <!-- 添加字体图标 -->
  <el-button type="success" size="small" :icon="Edit"> 编辑按钮 </el-button>
</template>

<script>
import { defineComponent } from 'vue'
import { ElConfigProvider } from 'element-plus'
import { Edit } from '@element-plus/icons-vue'

export default defineComponent({
  components: {
    ElConfigProvider,
  },
  setup() {
    return {
      zIndex: 3000,
      size: 'small',
      Edit
    }
  },
})
</script>