## 项目简介

任务清单管理系统采用 `B／S` 架构，基于 `Linux` 平台开发。采用轻量级的` Web`服务器 `Nginx`， 其后端实现建议采用基于`Python` 语言的 Flask 开源 `Web` 框架，进而增强扩展性。数据库采用关系型数据库  `Mariadb` ，前端的技术栈使用 `Bootstrap` 框架。该系统面向学生或者企业员工，提供任务添加、任务删除、任务完成标记， 任务搜索 ，可视化操作、数据实时展现等功能，目的在于轻松查看自己和他人的工作安排，合理规划手头任务。


## 项目功能


就像一般的 `Todo List `应用一样， 实现了以下功能：
- 用户登录、注册、注销
- 管理数据库连接
- 列出现有的待办事项
- 创建新的待办事项
- 检索单个待办事项
- 编辑待办事项或标记待办事项
- 删除待办事项

## 技术分析


- 为什么选择Flask?

	Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 `WSGI `工具箱采用 `Werkzeug` ，模板引擎则使用 `Jinja2 `。Flask使用 BSD 授权。
  
  Flask也被称为` “microframework”` ，因为它使用简单的核心，用 extension 增加其他功能。Flask没有默认使用的数据库、窗体验证工具。
  
  因此Flask是一个使用Python编写的轻量级Web应用框架。轻巧易扩展，而且够主流，有问题不怕找不到人问，最适合这种轻应用了。


- 为什么选择`Mariadb`?

    `MariaDB`数据库管理系统是`MySQL的`一个分支，主要由开源社区在维护，采用`GPL`授权许可` MariaDB`的目的是完全兼容`MySQL`，包括`API`和命令行，使之能轻松成为`MySQL`的代替品。`MariaDB`虽然被视为`MySQL`数据库的替代品，但它在扩展功能、存储引擎以及一些新的功能改进方面都强过`MySQL`。而且从`MySQL`迁移到`MariaDB`也是非常简单的.

- 为什么选择Bootstrap?

    Bootstrap 是一个用于快速开发 Web 应用程序和网站的前端框架。Bootstrap 是基于 `HTML、CSS、JavaScript` 的。具有移动设备优先、浏览器支持良好、容易上手、响应式设计等。


