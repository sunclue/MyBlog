# Flask

https://tutorial.helloflask.com/

## 准备工作

* 使用python3内置venv创建虚拟环境
  * `python -m venv envname`envname自定义
  * 激活虚拟环境：`./env/Scripts/activate`，激活后命令提示符前出现环境名
  * 退出虚拟环境：`./env/Scripts/deactivate`

## hello

* `flask run`命令会使用内置的开发服务器运行程序，默认监听本地机的5000端口

* 从flask包中导入Flask类，实例化Flask类创建一个程序对象

* 注册处理函数，该函数用于处理某个请求，也叫视图函数（view function）

  * ```python
    @Flaskinstance.route('/')
    def funcname():
        ...
    ```

  * 注册为给这个函数带上一个装饰器帽子，使用`Flaskinstance.route()`装饰器为这个函数绑定对应的URL，用户访问该URL时会触发这个函数，获取返回值，并将返回值显示到浏览器窗口，`/`对应根地址

  * 一个视图函数可绑定多个url，只需附加多个装饰器

* 程序发现机制

  * Flask默认程序存储在app.py或wsgi.py的文件中
  * 使用其他名称需要设置系统环境变量`FLASK_APP`选择启动的程序

* 管理环境变量

  * `FLASK_DEBUG`设置为1时可开启调试模式，程序出错时页面显示错误信息，代码变动程序会自动重载
  * Flask2.3及以上版本可使用--debug选项在运行时开启调试模式
  * 安装python-dotenv后Flask会从项目根目录的.flaskenv和.env文件读取环境变量并设置

* 视图函数名作为代表某个路由的端点（endpoint），同时用来生成视图函数对应的URL，程序内的URL可通过Flask的url_for()函数生成，第一个参数为端点值，默认为视图函数的名称

* Flask支持在URL规则字符串里对变量设置处理器，对变量进行预处理，如`/user/<int:number>`会将URL中的number部分转换为整型

* 开头为`.`的文件默认隐藏，ls无法看到，加入-f选项查看

## 模板

* 模板是包含变量和运算逻辑的HTML或其他格式的文本
* 渲染是执行这些变量替换和逻辑计算的过程
* Flask中渲染由Jinja2完成
* 默认设置中Flask从程序实例所在模块同级目录的templates文件夹中寻找模板
* Jinja2语法与python相似
* 模板中需要特定的定界符将Jinja2语句和变量标记出来
  * `{{...}}`标记变量
  * `{%...%}`标记语句，如if，for
  * `{#...#}`标记注释
* 模板中使用的变量需要渲染时传递进去
* 为方便处理变量，Jinja2提供了一些过滤器
  * `{{变量|过滤器}}`
  * 所有过滤器： https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters
* 渲染主页模板
  * 使用render_template()函数可渲染模板，必须传入的参数为模板文件名（相对于template目录的文件路径），模板内部使用的变量通过关键字参数传入函数
* [Faker](https://github.com/joke2k/faker)可实现自动生成虚拟数据，如时间、人名、地名、随机字符等
* Jinja2还在模板中提供了一些测试器、全局函数可以使用，[Jinja2文档](https://jinja.palletsprojects.com/en/3.0.x/templates/)

## 静态文件

* 指内容不需要动态生成的文件，如图片、css、JS脚本
* Flask中需要创建一个static文件夹保存静态文件，该文件夹和程序模块、template文件夹在同一目录层级
* 引入静态文件需要给出资源所在的URL，使用url_for()获取，传入的端点值为static，同时使用关键字参数filename传入相对于static文件夹的文件路径
* python脚本中url_for()函数需要从flask包导入，模板中直接使用
* 添加favicon
  * favicon是显示在标签页和书签栏的网站头像，格式为ICO、PNG或GIF
* 可借助前端框架完善页面样式，如Bootstrap、Semantic-UI、Foundation等

## 数据库

* 示例使用SQLite，它基于文件，不需要单独启动数据库服务器

* 使用SQLAlchemy操作数据库

  * SQLAlchemy是一个python数据库工具
  * 可通过定义类表示数据库的一张表（类属性表示表中的字段/列）
  * 通过类进行各种操作代替写SQL语句
  * 使用Flask-SQLAlchemy扩展集成SQLAlchemy

* 设置数据库URI

  * Flask使用Flask类实例的config字典写入和获取配置变量，配置变量名称必须使用大写，写入配置语句一般放在扩展类实例化语句之前
  * SQLite的数据库连接地址格式`sqlite:////数据库文件的绝对地址`，Windows系统只需三个斜杠

* 创建数据库模型

  * 模型类的编写限制

    * 模型类要声明继承db.Model，db为SQLAlchemy实例

    * 每一个类属性（字段）要实例化db.Column，传入的参数为字段的类型，常用字段类

      db.Integer、db.String(size)、db.Text、db.DateTime、db.Float、db.Boolean

    * 在db.Column中添加额外的选项可以对字段进行设置

      `primary_key`设置是否为主键，`nullable`设置是否允许为空值，`index`是否设置索引，`unique`是否允许重复值，`default`设置默认值

* 创建数据库表

  * 创建模型类后，创建表和数据库文件

  * ```shell
    (env) $ flask shell
    >>> from app import db
    >>> db.create_all()
    ```

  * 执行命令后出现数据库文件data.db

  * 数据库文件不需要提交到git

  * 改动模型类需要重新创建

  * ```python shell
    >>> db.drop_all()
    >>> db.create_all()
    ```

  * 此操作会删除所有数据，若想不破坏数据库内数据的前提下改变表的结构，需要使用数据库迁移工具，如集成了Alembic的Flask-Migrate扩展

  * flask可自定义命令

    * 导入click模块
    * 注册为命令，`@app.cli.command()`
    * 设置选项，`@click.option(vars)`
    * 默认情况下函数名称为命令的名字，函数名中的下划线会被转换为连接线，自定义表名可以设置`__tablename__`属性
    * 执行时前面需要加flask

* 数据库的增删查改
  * 增
    * 一个记录就是某个模板类的一个实例，创建时使用关键字参数传参
    * 将改动添加进数据库会话：`db.session.add(ModelInstance)`
    * 提交数据库会话（真正修改数据库）：`db.session.commit()`
  * 删
    * `db.session.delete(ModelInstance)`
  * 查
    * 查询语句格式：`<模型类>.query.<过滤方法（可选）>.<查询方法>`
    * 过滤方法：filter(),filter_by(),order_by(),group_by()
    * 查询方法：all(),first(),get(id),count(),first_or_404(),get_or_404(id),paginate()
  * 改
    * 先get，然后修改属性值

## 模板优化

* 自定义错误页面
  * 先写一个404错误模板
  * 然后使用`app.errorhandler()`装饰器注册一个错误处理函数，参数为404，当404错误触发时该函数执行
  * 需要返回第二个返回值，为状态码，视图函数默认200
* 模板上下文处理函数
  * 对于多个模板内都要使用的变量，可以使用`app.context_processor`装饰器注册一个模板上下文处理函数
  * 需要返回一个字典，返回值会同一注入到每一个模板的上下文环境中，可以直接在模板中使用，不需要在render_template函数中传入
* 使用模板继承组织模板
  * Jinja2提供了模板继承机制解决模板内容重复问题，与python类继承相似
  * 定义一个基模板，基模板中包含完整的HTML结构和导航栏、页首、页脚等通用部分，子模版中通过`extends`标签声明继承某个基模板
  * 基模板中需要在实际的子模版中追加或重写的部分定义成块（block），块使用`block`标签创建，`{%block 块名称%}`作为开始标记，`{%endblock%}`或`{%endblock 块名称%}`作为结束标记，通过在子模版中定义一个同名块可以向基模板的对应块位置追加或重写内容
  * 默认的块重写方式是覆盖，想要追加内容需要在子块中使用super()声明，即`{{super()}}`
  * 因为基模板会被所有其他页面模板继承，若在基模板使用了某个变量，那么该变量需要使用模板上下文处理函数注入到所有模板中

## 表单

* `<form>`标签中若不指定method默认为GET

* `<input>`必须包含name属性，否则无法提交数据，服务器端也需要name属性获取对应字段的数据

* `<label>`可以使鼠标点击标签文字时激活对应的输入框，for属性填入要绑定的`<input>`元素的id值

* 创建新条目

  * `<input>`中autocomplete属性设为off关闭自动完成，required标志属性必须输入

* 处理表单数据

  * 默认情况下，当表单中的提交按钮按下时，浏览器会创建一个新的请求，默认发往当前URL（`<form>`中的属性action可指定目标URL）

  * 修改视图函数使其能接受POST请求，默认只能GET

    `@app.route('/',methods=['GET','POST'])`

  * Flask会在请求触发后把请求信息放到`request`对象里，可以从flask包导入

  * request只有在请求触发时才包含数据，只能在视图函数中调用，包含请求的所有信息

    * request.path：请求路径
    * request.method：请求的方法
    * request.form：表单数据
    * request.args：查询字符串

  * flash消息

    * 在页面上显示提示消息最简单的实现：在视图函数里定义一个包含消息内容的变量，传入模板，然后在模板里渲染显示

    * flash函数用来在视图函数里向模板传递提示消息，get_flashed_message函数用来在模板中获取提示消息

    * 从flask包中导入flash，然后再视图函数中调用传入要显示的消息内容

    * flash函数在内部会把消息存储在Flask提供的session对象中，session用来在请求间存储数据，它把数据签名后存储在浏览器的Cookie中，需要设置签名所需的密钥：

      `app.config['SECRET_KEY']='dev' #等同于app.secret_key='dev'`

      密钥值在开发时可随便设置，部署时应设置为随机字符，且不应该明文写在代码中

  * 重定向响应

    * 重定向响应会返回一个新的URL，浏览器在接收到这样的响应后会向这个新URL再次发起一个请求
    * Flask提供了redirect函数来快捷生成这种响应，传入重定向的目标URL作为参数

* 编辑条目

  * 编辑的实现与创建类似

* 删除条目

  * 获取条目并删除即可

* 手动验证表单数据不可靠，一般使用集成了WTForms的扩展Flask-WTF简化表单处理，而且其内置CSRF保护功能

* CSRF 是一种常见的攻击手段。以我们的删除表单为例，某恶意网站的页面中内嵌了一段代码，访问时会自动发送一个删除某个电影条目的 POST 请求到我们的程序。如果我们访问了这个恶意网站，就会导致电影条目被删除，因为我们的程序没法分辨请求发自哪里。解决方法通常是在表单里添加一个包含随机字符串的隐藏字段，同时在 Cookie 中也创建一个同样的随机字符串，在提交时通过对比两个值是否一致来判断是否是用户自己发送的请求。在我们的程序中没有实现 CSRF 保护。

## 用户认证

* 安全存储密码

  * 密码不能明文存储在数据库中，保险的方式是对每个密码生成独一无二的密码散列值

  * Flask的依赖Werkzeug内置了用于生成和验证密码散列值的函数

    `werkzeug.security.generate_password_hash()`为给定的密码生成哈希值

    `werkzeug.security.check_password_hash()`检查给定的散列值与密码是否对应

* 使用Flask-Login实现用户认证

  * 是个扩展 
  * 初始化除了要实例化外，还需要实现一个用户加载回调函数，还需要让存储用户的模型类继承Flask-Login提供的UserMixin类
  * 提供一个`current_user`变量，注册用户加载回调函数的目的是，程序运行后，若用户已经登陆，current_user变量的值会是当前用户的用户模型类记录
  * 继承UserMixin类后模型类将拥有几个用于判断认证状态的属性和方法，最常用的是is_authenticated属性：若当前用户已经登陆，则current_user.is_authenticated会返回True

* 登录

  * 登录用户使用Flask-Login提供的login_user函数实现，需要传入用户模型类作为参数

* 登出

  * 使用logout_user函数

* 认证保护

  * 有些页面或URL不允许未登录的用户访问，页面上的有些内容需要对未登陆的用户隐藏
  * 对于不允许未登录用户访问的视图，只需要为视图函数附加一个login_required装饰器即可
  * 添加login_required装饰器后，若未登录的用户访问对应的URL，Flask-login会把用户重定向到登录页面，并显示一个错误提示，为执行这个重定向操作，需要把`login_manager.login_view`的值设为登录视图端点（函数名），放在login_manager实例定义下即可，设置`login_manager.login_message`定义错误提示消息
  * 有些能对未登录用户开放但页面内有些操作不开放的页面只需要对current_user.is_authenticated验证即可
  * 模板内容保护：在模板中可以直接使用current_user变量，使用if语句配合current_user.is_authenticated值隐藏即可

## 测试

* 为程序编写自动化测试
* 单元测试
  * 对程序中的函数等独立单元测试
  * 可使用python标准库中的测试框架unittest编写单元测试
  * 测试用例继承unitteest.TestCase类，该类中创建的test_开头的方法被视为测试方法
  * 测试固件的方法，setUp()在每个测试方法执行前被调用，tearDown()在每个测试方法执行后被调用
  * 每个测试方法对应一个要测试的函数/功能/使用场景
  * 使用断言方法判断函数返回值是否符合预期，断言方法出错则该测试方法未通过，常用assertEqual、assertNotEqual等
  * 执行unittest.main方法
* 测试Flask程序
* 测试覆盖率
  * 使用Coverage.py检查测试覆盖率
  * 执行命令`coverage run --source=app test_watchlist.py`，--source指定要检查的模块或包
  * `coverage report`查看覆盖率报告
  * `coverage html`获取详细的HTML格式的覆盖率报告

## 组织代码

* 可以使用单脚本，也可以使用包
* 使用包组织代码
  * 需要创建一个包
  * 可将代码放入不同文件
  * `__init__()`必需，用于创建程序实例，初始化扩展
  * 其他代码可分类，如视图函数、错误处理函数、模型类、命令函数，名称自定义
  * 需要注册到程序实例的函数，需要导入`__init__()`，为避免循环导入，在最后导入
  * 需要修改环境变量`FLASK_APP`
  * templates和static需要放在包下

## 部署上线

* 有两种部署方式：传统部署和云部署
  * 传统部署一般要在一个Linux系统上完成所有操作
  * 云部署使用云平台，云平台已经设置好了底层服务，只需上传代码并进行一些简单操作
* 部署前：
  * 生成依赖列表：`pip freeze > requirements.txt`
  * 配置变量：有些变量在生产环境下需要不同的值，部署时需要修改为从环境变量中读取
  * 部署程序时，不会使用flask内置的开发服务器运行程序，对于写到`.env`中的环境变量，需要使用python-dotenv导入
* 初始化程序运行环境
  * 上传代码有两种方式：从Github上拉取、在本地将代码压缩为压缩文件，在Files标签页上传
  * 使用uuid模块生成`SECRET_KEY`：`uuid.uuid4().hex`
  * 安装依赖并进行初始化操作