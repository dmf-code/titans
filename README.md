# titans
Selenium automation framework - Selenium自动化框架

![](https://github.com/dmf-code/photos/blob/master/titans.jpg)

### 前端

采用Element-UI进行前端布局设计，前后分离的模式

![](https://github.com/dmf-code/photos/blob/master/%E5%89%8D%E6%9C%9F%E9%A1%B5%E9%9D%A2%E5%B8%83%E5%B1%80.png)

### 后端

`flask` 框架进行编写，数据表结构如下
```mysql
CREATE TABLE `configs` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(32) NOT NULL COMMENT '任务类型',
  `name` varchar(32) DEFAULT NULL COMMENT '任务名称',
  `json_text` json DEFAULT NULL COMMENT '任务命令集',
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;


CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `uuid` varchar(36) NOT NULL COMMENT '分布式唯一id',
  `result` json DEFAULT NULL COMMENT '结果集',
  `type` varchar(32) DEFAULT NULL COMMENT '任务类型',
  `name` varchar(32) DEFAULT NULL COMMENT '任务名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

### 服务端

`Selenium` 自动化框架，采用 `json` 配置化的形式进行数据采集或自动化测试等


### chromedirver下载（对应相应的版本）

https://npm.taobao.org/mirrors/chromedriver


