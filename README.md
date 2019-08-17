@[toc](Hebook 软件设计说明书)
# 1 Hebook内容描述
Hebook定位于人脉信息管理平台，帮助用户存储、查询复杂的人脉信息，并基于对人脉信息的分析和推断，给用户提供人脉管理方案推荐。

## 主要功能模块
- 存储查询人脉信息
- 人脉信息统计与分析
- 人脉管理推荐

# 2 需求分析
## 2.1 角色分类
|序号| 名称 |描述| 权限|
|--|--| --| -- | 
| 1|  游客（Tourist）| 脱机使用Hebook的群体 |  1 增删查改联系人信息 （信息本地存储） | 
| 2  | 用户（User） | 使用Hebook的注册用户 | 1、查改看个人资料 2 增删查改联系人信息  3 查看人脉统计分析信息
| 3| VIP用户 | 使用Hebook的VIP用户| 1、查改看个人资料 2 增删查改联系人信息  3查看人脉统计分析信息 4 查看人脉管理方案推荐 

备注：*对没有的权限项，在不必要的情况下，系统可以不生成*


## 2.2 功能需求

### 2.2.1 功能需求总表
| 编号| 功能需求名称| 优先级别|
|--|--|--|
| fun01| 注册用户 ，填写用户信息| 高|
| fun02 | 用户管理个人信息 | 高 | 
| fun03| 添加联系人 ，填写联系人信息| 高 |
| fun04 | 修改联系人信息 | 高|
|fun05| 删除联系人 | 高 | 
|fun06| 查看联系人信息，提供筛选、排序、搜索功能| 高 |
| fun07| 人脉信息统计与分析 | 中 | 
|fun08| 人脉管理推荐 | 底 | 

### 2.2.2 功能需求描述
**fun01：注册用户，填写用户信息**
【功能概述】注册用户，填写注册信息，如登录手机号和密码设置等。 用户信息包括 姓名、性别、出生日期等，皆为非必填项目
【操作者】游客

**fun02：用户管理个人信息**
【功能概述】用户可对姓名、性别等个人信息进行修改管理。
【操作者】用户

**fun03：添加联系人 ，填写联系人信息**
【功能概述】游客或用户可以添加联系人，填写姓名、性别等信息。其中，与中间人关系、姓名，性别为必填项。
【操作者】游客、用户

**fun04：修改联系人信息**
【功能概述】游客或用户可以修改联系人信息，如姓名、性别等信息。
【操作者】游客、用户

**fun05：删除联系人**
【功能概述】游客或用户可以修改联系人。
【操作者】游客、用户

**fun06：查看联系人信息，提供筛选、排序、搜索功能**
【功能概述】游客和用户可以查看已添加的联系人信息，并可以按照联系人的相关信息信息筛选、排序以及搜索。
【操作者】游客、用户

**fun07：人脉信息统计与分析**
【功能概述】系统根据用户存储的人脉信息，对数据进行统计和分析，给出用户的相关人脉状况，如年龄分布，性别比列，职业领域，地域分布等。
【操作者】 系统

**fun08：人脉管理推荐**
【功能概述】系统根据用户存储的人脉信息，对用户的人脉管理进行推荐，如节日祝福提醒，好友生日提醒，久未联系提醒等。
【操作者】系统


## 2.3 用例图设计建模

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019080121230177.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)


## 2.4 实体属性分析
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190810165319759.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)

## 2.4 类图设计建模
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190810172819587.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)

## 2.4 组件图设计建模
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190810173023756.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)

# 3 数据库设计

## 3.1 设计规则
> 类名 全大写 
> 表名 首字母大写
> 其他 全部小写  。 多词用下划线_连接
> 每个表都有create_time,update_time,is_delete字段

## 3.2 User
| 名称 | CODE | 类型 |  描述| 可否为空 | 初始化| 
|--|--|--|--|--| --| 
| **用户ID** | user_id | char| U000001(U开头) | 否 | 表长度| 
|登录账号| account | int | 11位手机号| 否|
| 登录密码| password | char | 密文格式存储 | 否|
| 是否VIP | is_vip | bool | 0 不是vip 1 是vip |否| 0| 
| 联系人总数 | contact_count | int | 所有联系人的总数 | 否| 0 | 
| 姓名| name | char | | 否| 
| 性别 | gender | bool  |  0 女 1 男 | | | 
| 出生日期 | birthdate | time | | |  |  
| 联系电话1 | phone_number1 | int|
|联系电话2 |phone_number2 | int|
|社会状态 |state | int | 0 在读 1 在职 2 退休 3 无业
| 现居地 | residence | char |
| 籍贯| birthplace| char | 
| 婚姻状态| marital_status | int | 0 单身  1 恋爱 2 已婚


## 3.3 Contact
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
|**联系人ID** | contact_id| char | C000001（C开头）| 否| 表长度| 
| **用户ID** | user_id | char | user_id 外码 | 否 | 来源
| 总分| score | int | **评分计算规则？** | 否 | 60 |
| 未联系天数 |untouch_day | int | 自建立好友关系以来 | 否| 0 | 
| 主动联系次数 | contact_count_a | int | |否| 1 |
| 被动联系次数 | contact_count_b | int |  |否|0 |
| 联系总次数 | contact_count| int | 主动+被动 | 否 | 1 | 
| 联系码 | contact_code | int | 180位记录半年来的联系情况  0 未联系 1 主动 2 被动 3 互动 | 否|0|
| 联系频率 | contact_frequency | float | 联系总次数 / (当前时间-创建时间+1) | 否 | 1 | 
| 关系等级 | class | int | 1  挚友 2 好友 3 朋友 4 相识 5 存在 | 否 | 3 | 
| 关系人| associated | char | user_id/contact_id  | 否 | 页面来源 | 
|关系| relationship | int | 0 家人 1 亲戚  2 朋友 3 同学 4 同事 5 老师 6 领导 7 特别关注 8 其他 | 否 | 2 |
 | 姓名| name | char | | 否| 
| 性别 | gender | bool  |  0 女 1 男 | | | 
| 出生日期 | birthdate | time | | |  |  
| 联系电话1 | phone_number1 | int|
|联系电话2 |phone_number2 | int|
|社会状态 |state | int | 0 在读 1 在职 2 退休 3 无业
| 现居地 | residence | char |
| 籍贯| birthplace| char | 
| 婚姻状态| marital_status | int | 0 单身  1 恋爱 2 已婚


## 3.4 Education
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
| **教育ID** | education_id | int | | 否| 表长度|
| **人物ID** | person_id |char  |  user_id/contact_id 外码  |否 | 来源 | 
| 开始时间 | start_time | time | | | |
| 结束时间 | end_time | time |
| 学历|academic | int | 0 高中 1 专科 2 本科 3 硕士 4 博士 5 博后 6 硕博 | | 
| 学校名称 | school | char | | 否 | 
| 专业| major | char |
|领域 | field | char | 学习或研究领域 |

## 3.5 Job
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
| **工作ID** | job_id | int| | 否| 表长度 | 
| **人物ID** | person_id |char  |  user_id/contact_id 外码  |否 | 来源 | 
| 开始时间 | start_time | time | | | |
| 结束时间 | end_time | time |
| 公司名称 | company | char | | 否 | 
|薪资 | salary | float | | | 
|薪资单位 | salary_unit |int | 0 月薪 1 年薪 |  否 | 0 
|工作地点| work_place| char | 
|职位| position | char 


## 3.6 Mark  （* - * ）
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
| **标签ID** | mark_id | int| | 否| 表长度 | 
| 用户ID | user_id | char | user_id （user拥有一个mark 列表）外码 | 否 | 来源|
| 标签名称 | mark_name | char | | 否|
| 标签占有数 | mark_holder | int | 拥有这个标签的联系人的总数 | 否 | 0 |


## 3.7 Prefer（* - * ）
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
| **偏好ID** | prefer_id | int| | 否| 表长度 | 
| 用户ID | user_id | char | user_id （user拥有一个prefer 列表） | 否 | 来源|
| 偏好名称 | prefer_name | char | | 否|
| 偏好类型 | prefer_type | int | 0 喜好 1 讨厌 | 否 | 0 | 
| 偏好占有数 | prefer_holder|int |拥有这个偏好的联系人的总数 | 否 | 0 |


## 3.8 Authorization 
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
|**授权ID** | authorization_id | int| | 否 | 表长度 
| **用户ID** | user_id | char|  | 否 |来源|
| 应用名称 | app_name | int | 0 微信 1 QQ 2 微博 （目前只考虑这三个平台） | 否 |
|账号 | app_account | char | 第三方平台的账号 | 否 | 
| 授权码 | authorzation_code| char | **能有效登录第三方平台**|   


## 3.9 Social_app（根据 命名自行匹配）
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
| 社交ID | socia_id | int| | 否| 表长度 | 
| 联系人ID | contact_id | char | 外码 | 否 | 
| 社交平台 | social_platform | int | 0 微信 1 QQ 2 微博 （目前只考虑这三个平台）| 否 | 
| 社交账号 | social_account | char | 每个平台的用户ID不一样 | 否 |

## 3.10 Contact_description
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
|**描述ID** | descript_id | int | | 否| 表长度|
| **联系人ID** | contact_id| char | 用于描述联系人  外码 | 否| 来源
| 描述内容| descript_content | char | | 否 |


## 3.11 Contact_mark （关系表）
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
|**联系人ID** | contact_id| char | C000001（C开头）| 否| 表长度| 
| **标签ID** | mark_id | int| | 否| 表长度 | 


## 3. 12 Contact_prefer （关系表）
| 名称 | CODE | 类型 |  描述|  可否为空 | 初始化| 
|--|--|--|--|--|--| 
|**联系人ID** | contact_id| char | C000001（C开头）| 否| 表长度| 
| **偏好ID** | prefer_id | int| | 否| 表长度 | 


# 4 UI设计
## 颜色说明
| 编号 | 名称 | 色号 | 显示 | 描述 
| -- | --| --|--|--|
| 01| 主题色 | 00C88C | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817102837314.png)
|02| 字体色1 | 4A4A4A | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817102955132.png) | 联系人名称、 主要信息
|03| 字体色2 | 9B9B9B | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817103117101.png) | 附加信息、提示信息|
|04 | 模块背景色1 | FCFCFC | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817103236276.png) | 下拉栏模块背景色 
| 05 | 模块背景色2 | F1F1F2 | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817103425245.png) | 列表间隔色
| 06 | 输入框边框色 | D8D8D8 | ![在这里插入图片描述](https://img-blog.csdnimg.cn/2019081710354324.png)  | 也用作 holdplace 字体色
| 07 | 统计色-红 | EB5F53 | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817104059770.png) | 
| 08 | 统计色-橙 |F6B949| ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817104152415.png) | 也用作提示信息
|09 | 统计色-蓝 | 4CB6E9 | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817104232700.png) | 
|10 | 统计色-绿 | 7DB19C | ![ ](https://img-blog.csdnimg.cn/20190817104308781.png) | 
| 11| 统计色-紫 | 9268C7| ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817104346127.png) |
| 12 | 统计色-深蓝  | 6586A0 | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817104428655.png) | 


## 字体说明
| 编号| 名称 | 字体 | 字号 | 描述 | 
|--|--|--|--|--|
|01 | 主题 -Hebook | 微软雅黑 | 24px B | B即为加粗的意思
|02 |  一级字体 | 微软雅黑 | 18px | 用于标题等醒目内容
|03 |  button 字体 | 微软雅黑 | 18px B |  
|04| 二级字体 | 微软雅黑 | 14px |  
|05 | 三级字体 | 微乳雅黑 | 12px | 用为提示信息


## UI设计说明
### 底部导航栏：
- 联系人
- 统计
- 我的

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817105704317.png)

### 使用方式：
- 登录
可使用 联系人、统计、我的 三个模块
- 游客
只能使用联系人 一个模块
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817105750594.png)
### 第三方登录支持方式：
- 微信
- QQ
- 微博
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817105918908.png)

### 注册方式：
- 账号为手机号，获得验证码。 密码只输入一遍，可以通过点击 👁 按钮确定密码。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817110027711.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)

### 联系人查找方式：
- 搜索🔍 ：文字模糊查询，后期可提供语音输入
- 筛选 ： 下拉按钮展开。采用【即时相应】的方式，也就是说不需要在设定好筛选项之后点确定。筛选项列表如下：

| 编号 | 筛选项 | 内容 | 描述|
|--|--|--|--|
|01| 性别  |  0 女 1 男 | | | 
|02 | 年龄 |  0 0-18 1 18-26  2 26-40 3 40-100
|03 |社会状态 | 0 在读 1 在职 2 退休 3 无业
|04 | 现居地 | 列出所有联系人中出现过的现居地（需要及时计算） |  按数量从多到少排序，页面宽度不够时，左右滑动
|05 | 籍贯| 列出所有联系人中出现过的籍贯（需要及时计算） |  按数量从多到少排序，页面宽度不够时，左右滑动
|06 | 婚姻状态| 0 单身  1 恋爱 2 已婚
|07 | 标签 | User维护的标签列表 且标签占有数不为0的标签 | 按数量从多到少排序，页面宽度不够时，左右滑动
|08 | 偏好 | User维护的偏好列表 且偏好占有数不为0的标签 | 按数量从多到少排序，页面宽度不够时，左右滑动
| 09 | 学校 | 列出所有联系人中出现过的学校（需要及时计算）| 按数量从多到少排序，页面宽度不够时，左右滑动
|10 | 公司 | 列出所有联系人中出现过的公司（需要及时计算）| 按数量从多到少排序，页面宽度不够时，左右滑动


- 排序 ： 默认按照 联系人的【总分】排序，提供 【未联系天数】、【关系等级】、【联系频率】排序。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817110301471.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)


### 列表中显示的联系人信息：
- 头像
- 关系及等级 
- 未联系天数
- 联系频率
-  总分
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817112226215.png)

### 新建联系人
- 红色区域内为必填信息 ，点击修改。图像使用默认图像
- 若首先关联应用，则可从应用中自动匹配 联系人信息 ，自动填入。
- 其余内容均为非必填项。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817112338332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)

### 联系人详情页面
- 红色区域的信息由 【联系码】 提供，样式参照 GitHub。颜色设定如下：

| 适用情况 | 颜色 | 色号|描述
|--|--|--|--|
| 无联系 | 灰色 | F1F1F2 |
| 主动联系 | 橙色 | F6B949 |
|被动联系 | 蓝色 | 4CB6E9 |
| 互动联系 | 绿色 | 7DB19C |  既不能说主动，也不能算被动的情况

- 蓝色区域是联系人的基本信息显示区域，只显示非空项。 
- 黄色区域均为下拉展开。


![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817112627158.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)


### 个人中心（我的）
- Module 1 账户信息： 用户头像 、用户名称、登录账号（手机号）
- Module 2 用户信息：只显式非空项
- Module 3【 点击跳转选项卡】
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817144719592.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)


### 标签管理
- 显示现有标签，点击表示【删除标签】，button会变成灰色，点击【完成】之后才会消失。 （后续可以将【标签】恢复变为【vip-支持】）
- 在输入空内输入标签名称，点击【添加】后，出现在【现有标签】中，添加时【检查重复】，点击【完成】后才生效。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817145142830.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)

### 偏好管理
- 偏好管理中，将【喜欢】和【讨厌】分开管理
- 其他同上【标签管理】

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817145556509.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)


### 统计报表
- 直接显示项： 联系人总数即各级人脉比例（人数）、男女比例、年龄分布
- 下拉展开项： 社会状态、婚姻状态、地域分布、领域分布
- 高级统计项（vip-支持）：关系等级分布、联系频率分段（0.25，0.5.0，75）、总分分段（40，50，60，70，80，90）、标签统计（各个标签有多少人-可查看列表）、偏好统计（各个偏好有多少人-可查看列表）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190817145640661.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05HVWV2ZXIxNQ==,size_16,color_FFFFFF,t_70)








