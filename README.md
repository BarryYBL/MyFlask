FLASK自动化测试平台：
a:在启动后，页面进入127.0.0.1:5000后会出现报错，所有的预配置数据库和数据此时会去进行创建，再次发起请求即可登陆页面  


1：默认账号admin/admin，只有admin用户可以进行注册用户，每个用户都有自己的配置   

2: 需要先配置请求头部，格式有校验：如 {"Content-Type": "application/json;charset=UTF-8"}

3：测试用例场景是集合测试用例作为一个整体，可以对测试用例场景进行执行/复制  

4：测试分组 是可以作为测试用例的集合分组，可以包含测试场景，可用于在测试执行页面执行的一类分组  

5：测试报告生成页面和excel，但是excel目前是将所有的测试用例打印出来，后续会添加上测试场景归属  

6：关于全局变量，全局变量的格式按照${ZDBM_IP}中的${变量名}，写在请求中，支持名称/URL/请求报文/请求头部,变量均为全局，尽量不要重名  

7：测试用例执行是顺序执行的，暂不支持多线程  

8：预期结果的格式  如 ：     包含:123          指请求的响应结果包含123数字

i[](https://github.com/yangleiqing0/test/blob/master/20190819154824.png)
![](https://github.com/yangleiqing0/test/blob/master/20190819131549.png)
![](https://github.com/yangleiqing0/test/blob/master/20190819132150.png)
