# wallhaven-api-for-python
wallhaven api for python

## 前言

### 本人第一次做,代码如果有BUG请原谅

## 描述

api支持: https://wallhaven.cc/help/api (官方)

## 依赖

```sh
# pip install requests
```

## 快速开始

导入库文件

```python
# import wallhavenapi
```

搜索(基础)

```python
# wallhavenapi.search(search = 'name', page = 'number', purity = 'sfw')
```

搜索(高级)

```python
# wallhavenapi.search_x(search = 'name', page = 'number', purity = 'sfw', x_api = 'your x-api')
```

下载(基础)
```python
# wallhavenapi.download(dir_name = 'your path')
```


下载(高级)
```python
# wallhavenapi.download_x(dir_name = 'your path', x_api = 'your x-api')
```

## 使用方法

### wallhavenapi.search_x

* x_api {Srting} 你的 **[Wallhaven](https://wallhaven.cc) ** [api key](https://wallhaven.cc/settings/account)
* page {Srting} 页数
* purity {Srting} 有sfw , sketchy , nsfw 模式
* search {Srting} 搜索名

### wallhavenapi.search

* page {Srting} 页数
* purity {Srting} 有sfw , sketchy , nsfw 模式
* search {Srting} 搜索名


### wallhavenapi.download_x

* x_api {Srting} 你的 **[Wallhaven](https://wallhaven.cc) ** [api key](https://wallhaven.cc/settings/account)
* path {Srting} 下载文件夹路径

### wallhavenapi.download

* path {Srting} 下载文件夹路径
