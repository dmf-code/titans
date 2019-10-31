<template>
  <div>
    <el-button :size="cSize" type="primary" @click="dialogFormVisible = true">{{ cName }}</el-button>

    <el-dialog title="爬取规则" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="任务类型" :label-width="formLabelWidth">
          <el-input v-model="form.type" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="任务名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>

        <json-editor ref="jsonEditor" v-model="jsonText" />
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <template v-if="cType == 'add'">
          <el-button type="primary" @click="add">确 定1</el-button>
        </template>
        <template v-if="cType == 'update'">
          <el-button type="primary" @click="update">确 定2</el-button>
        </template>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import JsonEditor from "@/components/JsonEditor";
export default {
  name: "DialogForm",
  components: { JsonEditor },
  props: {
    cName: {
      default: "添加"
    },
    cSize: {
      default: "medium"
    },
    cType: {
      default: "add"
    }
  },
  data() {
    return {
      dialogFormVisible: false,
      form: {
        name: "",
        type: ""
      },
      formLabelWidth: "120px",
      jsonText: ""
    };
  },
  methods: {
    add() {
      this.dialogFormVisible = false;
      this.axios
        .post("/api/tasks/", {
          type: this.form.type,
          name: this.form.name,
          jsonText: this.jsonText
        })
        .then(response => {
          console.log(response.data);
        });
    },
    update() {
      console.log("update");
    }
  }
};
</script>

<style>
.dialog-footer {
  min-height: 2em;
}

/* .el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
} */
.el-main {
  background-color: #e9eef3;
  color: #333;
  /* text-align: center;
  line-height: 160px; */
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.el-button {
  float: right;
}
</style>
