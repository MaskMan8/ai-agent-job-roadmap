
异常处理，让程序遇到错误时还能继续运行。
finally常用于，关闭文件和释放资源。
先发制人捕获异常并处理
try:
    可能出错的代码

except 异常类型:
    处理错误代码
finally:
    最终执行代码(无论成功还是失败最后一定执行)

异常类型	          什么时候出现
ValueError	         数据的值不符合要求，例如 int("abc")
FileNotFoundError	 要读取的文件不存在
ZeroDivisionError	 除数是 0
OSError	             文件操作等系统操作出现问题

except ... as e
把捕获到的异常对象保存到变量 e


异常处理：判断程序执行时是否发生错误，例如输入 "abc"。
业务逻辑校验：判断数据是否符合业务要求，例如存款金额不能小于或等于 0

None：Python中表示“没有值”的特殊对象

