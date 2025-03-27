<template>
  <el-button type="primary" size="default" @click=""> 测试按钮 </el-button>

  <!-- 添加字体图标 -->
  <el-button type="success" size="small" :icon="Edit"> 编辑按钮 </el-button>

  <Test></Test>
  <Pagination></Pagination>

  <svg-icon name="home"></svg-icon>
  <svg-icon name="copyright" color="blue"></svg-icon>

  <!-- 测试SCSS  -->
   <div>
    <h1>
      测试代码
    </h1>
   </div>
</template>

<script>
import { defineComponent } from "vue";
import { ElConfigProvider } from "element-plus";
import { Edit } from "@element-plus/icons-vue";

// 这个是局部的，应该去掉
// import SvgIcon from "@/components/SvgIcon/index.vue";

export default defineComponent({
  components: {
    ElConfigProvider,
  },
  setup() {
    return {
      zIndex: 3000,
      size: "small",
      Edit,
    };
  },
});
</script>


<style scoped lang="scss">

  div{
    h1{
      color:$base-color;
    }
  }

</style>