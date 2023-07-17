# Git

* Git配置
  * `git config`工具，专门用来配置或读取相应的工作环境变量
  * 环境变量存放在以下位置
    * /etc/gitconfig：系统中对所有用户都普遍适用的配置，对应--system选项
    * ~/.gitconfig：用户目录下的配置文件只适用于该用户，对应--global选项
    * 当前项目的Git目录中的配置文件（工作目录中.git/config）：只对当前项目有效
    * 每一级配置都会覆盖上层的相同配置
  * 修改用户信息
    * `git config --global user.name 'name'`：修改用户名
    * `git config --global user.email name@qq.com`：修改电邮
    * `git config --global core.editor emacs`：修改默认文本编辑器为emacs，一般为vi或vim
    * `git config --global merge.tool vimdiff`：修改差异分析工具为vimdiff
  * 查看配置信息：`git config --list`
    * 来自不同配置文件的变量实际采用最后一个
  * 查看特定环境变量：`git config user.name`

* Git工作流程
  * 克隆Git资源作为工作目录
  * 在克隆的资源上添加或修改文件
  * 若其他人修改了，可以更新资源
  * 在提交前查看修改
  * 提交修改
  * 修改完成后，若发现错误，可以撤回提交并再次修改并提交
* 工作区、暂存区、版本库
  * 工作区：在电脑中能看到的目录
  * 暂存区：stage或index，一般存放在.git目录下的index文件中，有时也叫索引
  * 版本库：工作区的隐藏目录.git
  * <img src="C:\Users\Desire\AppData\Roaming\Typora\typora-user-images\image-20221229162144823.png" alt="image-20221229162144823" style="zoom:50%;" />
  * HEAD实际是指向master分支的一个游标，命令中HEAD可以用master替换
  * objects标识的区域为Git的对象库，实际位于.git/objects下，里面包含了创建的各种对象及内容
  * 对工作区修改的文件执行`git add`命令时，暂存区的目录树被更新，同时工作区修改的文件内容被写入到对象库中的一个新的对象中，而该对象的ID被记录在暂存区的文件索引中
  * 执行提交操作（git commit）时，暂存区的目录树写到版本库中，master分支会做相应的更新
  * 执行`git reset HEAD`命令时，暂存区的目录树会被重写，被master分支指向的目录树替换，但工作区不受影响
  * 执行`git rm --cached <file>`命令时，会直接从暂存区删除文件，工作区不变
  * 执行`git checkout .`或`git checkout -- <file>`时，会用暂存区全部或指定的文件替换工作区的文件
  * 执行`git checkout HEAD .`或`git checkout HEAD <file>`时，会用HEAD指向的master分支中的全部或者部分文件替换暂存区和工作区中的文件
* 创建仓库
  * 使用`git init`命令初始化一个git仓库，执行后，Git仓库会生成一个.git目录，该目录包含了资源的所有元数据
  * `git init directory`即将directory初始化为一个git仓库
  * 使用`git add`对要纳入版本控制的文件进行跟踪
  * 使用`git clone`从现有Git仓库中拷贝项目：`git clone <repo>`或`git clone <repo> <directory>`（克隆到指定目录）
  * 编辑配置文件：`git config -e`（当前仓库），`git config -e --global`
* 基本操作
  * Git的工作就是创建和保存项目的快照及与之后的快照进行对比
  * <img src="C:\Users\Desire\AppData\Roaming\Typora\typora-user-images\image-20221229164610006.png" alt="image-20221229164610006" style="zoom:50%;" />
  * 创建仓库
    * `git init`：初始化仓库
    * `git clone`：拷贝一份远程仓库
  * 提交和修改
    * `git add`：添加文件到暂存区
    * `git status`：查看仓库当前状态，显示由变更的文件
    * `git diff`：比较文件的不同，即暂存区和工作区的差异
    * `git commit`：提交暂存区到本地仓库
    * `git reset`：回退版本
    * `git rm`：将文件从暂存区和工作区删除
    * `git mv`：移动或重命名工作区文件
  * 提交日志
    * `git log`：查看历史提交记录
    * `git blame <file>`：以列表形式查看指定文件的历史修改记录
  * 远程操作
    * `git remote`：远程仓库操作
    * `git fetch`：从远程获取代码库
    * `git pull`：下载远程代码并合并
    * `git push`：上传远程代码并合并
* 分支管理
  * 一条分支代表一条独立的开发线
  * Git分支实际上是指向更改快照的指针
  * 创建分支命令：`git branch <branchname>`
  * 切换分支命令：`git checkout <branchname>`，切换分支时，Git会用该分支最后提交的快照替换工作目录的内容，所以多个分支不需要多个目录，`git checkout -b <branchname>`创建新分支并立即切换到该分支下
  * 合并分支命令：`git merge <branchname>`，合并后branchname分支仍然存在
  * 列出分支基本命令：`git branch`，没有参数时会列出在本地的分支，init时默认创建master分支
  * 删除分支：`git branch -d <branchname>`
  * 合并冲突：Git会合并修改，出现合并冲突（两个分支都修改了同一个文件）时需要手动修改，通过`git add`告诉Git文件冲突已经解决
* 查看提交历史
  * `git log`查看提交历史，--oneline选项为简洁版本，--graph选项查看历史记录中什么时候出现了分支、合并，--reverse选项逆向显示所有日志，--author=name查找name用户的提交日志，指定日期的选项：--before,--after,--until,--since
  * `git blame <file>`查看指定文件的修改记录
* 标签
  * 当到达一个重要阶段并希望永远记住那个特别的提交快照，可以用`git tag`给它打上标签，-a选项会创建一个带注解的标签，记录时间作者和注解，Git会打开编辑器让你写一句标签注解
  * 追加标签：忘记给某个提交打标签又将其发布了`git tag -a <tagname> <commit号>`
  * 查看所有标签：`git tag`
  * 指定标签信息命令：`git tag -a <tagname> -m "runoob.com标签"`
  * PGP签名标签命令：`git tag -s <tagname> -m "runoob.com标签"`
* 远程仓库
  * 添加远程库：`git remote add [shortname] [url]`，shortname为自定义的远程仓库的别名
  * 查看当前的远程库：`git remote`，-v参数可看到每个别名的实际链接地址
  * 提取远程仓库
    * 从远程仓库下载新分支与数据：`git fetch`，该命令执行完需要执行`git merge`远程分支到你所在的分支
    * 从远程仓库提取数据并尝试合并到当前分支：`git merge`
  * 推送到远程仓库：`git push [alias] [branch]`，将你的[branch]分支推送成为[alias]远程仓库上的[branch]分支
  * 删除远程仓库：`git remote rm [shortname]`
* Git服务器搭建