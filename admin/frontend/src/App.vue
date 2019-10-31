<template>
  <div id="app">
    <el-container>
      <el-header>爬虫规则列表</el-header>
      <el-main>
        <el-row>
          <dialog-form></dialog-form>
        </el-row>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
import DialogForm from "@/components/DialogForm";
export default {
  name: "App",
  components: { DialogForm }
};
</script>

<style scoped>
body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
  font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, SimSun, sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
}

#app {
  height: 100%;
}
</style>
