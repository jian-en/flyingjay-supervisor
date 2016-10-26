## 主要目的
1. 使用supervisor启动多个web项目，从而熟悉supervisor的使用方法
2. 使用一个任务，对于多个python框架进行性能测试

## 测试框架的种类
* wsgi - Benchmark

* Flask
* Django
* Falcon

* Tornado(+)
* ThriftRPC(+)
* Go(+)

## 任务定义
1. JSON: 将一个对象序列化, 以application/json的方式返回

## 条件定义
Gunicorn 19.6.0, 两个worker, 默认sync worker设置

## Supervisor使用
1. 安装: pip install supervisor
2. 模块使用: supervisord, supervisorctl, httpserver
3. 程序配置: program:x

## Reference
主要是受这篇帖子的启发:
http://klen.github.io/py-frameworks-bench/
