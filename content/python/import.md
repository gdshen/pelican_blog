Title:python中import的相关问题
Date:March 3, 2015 5:20 PM

### Python中的import

#### 额外知识
- dir()默认显示当前模块定义的变量,方法,属性,以及模块名字
- **模块**:一个python文件就是一个模块

#### import 基本作用
使用import语句可以使得用户自定义模块,或者系统库/用户安装的库在当前模块中可以调用
```python
import moduletest
from module import object
from module import as something
from module import * # 最好不要使用
```
从以上两种import的用法中可以看出,import的对象必须是模块,或者是模块中的变量/方法,在实际的使用过程中,尽量少使用from ... import ...的方式,因为这样会导致局部变量命名空间的污染,容易导致变量间的覆盖

#### relative & absolute import
在python2.5及其以前默认使用implicit relative import,而且python3中,implicit relative的方式已经禁用,我们现在只需要考虑explicit relative import和absolute import两种方式.

##### relative import
```python
import .foo
from .foo import bar
import ..foo
from ..foo import bar
```
这种方式构建的依赖关系在工程移植的时候容易broken(?),如果在python2中使用import语句的话,也推荐使用`from __future__ import absolute_import`,来使用absolute import

#### import 搜索路径问题
在absolute import中,搜索路径根据sys.path列表中给定的路径进行查询,而path[0]一般则是当前脚本的绝对路径,在交互式调用python解释器的时候,path[0]则是空.可以通过添加环境变量PYTHONPATH来改变path,或者
```python
import sys
sys.path.append("full/path")
```
来添加import搜索的路径,这种方法一般用在模块位置比较特殊的地方
