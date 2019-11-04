<template>
  <el-table :data="bodyData" style="width: 100%">
    <el-table-column
      v-for="(item, key) in headData"
      :key="key"
      :prop="item.value"
      :label="item.name"
    ></el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        <dialog-form
          cType="update"
          cSize="mini"
          cName="编辑"
          @click.native="handleEdit(scope.$index, scope.row)"
          :editData="form"
        ></dialog-form>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import DialogForm from "@/components/DialogForm";
export default {
  name: "Table",
  components: { DialogForm },
  data() {
    return {
      headData: [],
      bodyData: [],
      form: {}
    };
  },
  mounted() {
    this.headData = [
      {
        name: "ID",
        value: "id"
      },
      {
        name: "类型",
        value: "type"
      },
      {
        name: "名称",
        value: "name"
      }
    ];
    this.axios
      .get("/api/tasks/")
      .then(response => {
        this.bodyData = response.data["data"];
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    handleEdit(index, row) {
      console.log("handleEdit");
      console.log(row);
      this.form = row;
    },
    handleDelete(index, row) {
      console.log(index, row);
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
        center: true
      })
        .then(() => {
          this.axios.delete("/api/tasks/" + row.id).then(response => {
            if (response.data.get("status") == true) {
              this.$message({
                type: "success",
                message: "删除成功!"
              });
              location.reload();
            } else {
              this.$message({
                type: "info",
                message: "已取消删除"
              });
            }
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除"
          });
        });
    }
  }
};
</script>
