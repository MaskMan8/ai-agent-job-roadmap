Python模块与项目结构

在 Python 中，一个 .py 文件就可以作为一个模块。每个文件都可以定义自己的函数，其他文件也可以导入这些函数。每个模块都有自己的职责使得代码更加容易维护、测试和复用。
重点：拆分文件不会改变函数原来的功能，只是改变了代码的组织方式

导入模块
import tools
tools.use1()
tools.use2()
import tools as t
t.use1()
t.use2()
只导入某个模块的某一个内容
from tools import use1,use2
from tools import use1 as t1,use2 as t2