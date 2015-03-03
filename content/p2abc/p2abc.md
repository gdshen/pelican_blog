Title:privace-preserving attribute-based credential初了解
Date:February 21, 2015 7:10 PM
Tags:p2abc

## 初步了解p2abc
#### 预备知识

1. **war**是java的一种打包格式,Web Archive file
2. **Jersey**是一个RESTFUL请求服务JAVA框架
3. **servlet**是在服务器上运行的小程序
4. **Jetty** 是一个开源的servlet容器,基于java

#### 目的
基于属性证书的隐私保护身份认证协议,具有一下性质

1. 认证对方不能够获取比需要提供的更多的信息
2. 认证对方不能够由提供的子证书推导出其拥有者
3. 认证方不能够组合别人的属性

#### 应用场景
1. 需要验证身份的购买服务
2. 身份认证过程

#### 角色组成
- issuer
- user
- verifer
- inspector
- revocation

#### 设置p2abc系统的流程
1. 单个issuer产生系统参数并分发
2. revocation产生子集参数并分发,inspector产生公私钥
3. 设置证书的规范并分发
4. issuer产生参数并分发到user和verfier
5. 设置issuer和presentation的政策
