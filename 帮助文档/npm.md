npm install <包名> # 安装包到当前项目 (简写: npm i <包名>)
npm install -g <包名> # 全局安装包
npm install <包名>@<版本> # 安装特定版本的包

主要字段解释：
- **name**: 项目/包的名称
- **version**: 遵循语义化版本的版本号
- **description**: 项目描述
- **main**: 程序的入口文件
- **scripts**: 可执行的脚本命令
- **dependencies**: 生产环境依赖
- **devDependencies**: 开发环境依赖

## 5. 依赖管理

### 依赖类型

- **dependencies**: 生产环境必需的包
- **devDependencies**: 只在开发时需要的包
- **peerDependencies**: 兼容性依赖，指定宿主环境应该安装的包
- **optionalDependencies**: 可选依赖，安装失败不会导致npm失败

### 版本控制

NPM 使用语义化版本控制 (SemVer)：

- **固定版本**: `"express": "4.17.1"`
- **兼容补丁**: `"express": "~4.17.1"` (4.17.x)
- **兼容小版本**: `"express": "^4.17.1"` (4.x.x)
- **最新版本**: `"express": "*"` (不推荐在生产环境使用)

### 锁定依赖版本

`package-lock.json` 文件会自动生成，它精确记录了安装的每个依赖的确切版本。这确保了在不同环境中安装相同版本的依赖。

## 6. NPM 脚本

package.json 的 scripts 字段允许定义可执行命令：

