# mahjong-helper-majsoul-mitmproxy
本项目用于将雀魂的牌局发到[日本麻将助手mahjong-helper](https://github.com/EndlessCheng/mahjong-helper)，基于[mitmproxy](https://github.com/mitmproxy/mitmproxy)的中间人攻击方式，不支持牌谱分析。

#### 当前雀魂各服版本（实时更新）  
![CHINESE](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgame.maj-soul.com%2F1%2Fversion.json&label=CHINESE&query=$.version&color=FF8C00&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAACsklEQVQ4ja2Tf0zMcRjHX9/7Ud0l59RCFssWmemGom5mNysbLb+GuM2G8mOMCGu0rD9aNuRHymxnNqbGqcwMG1lrRLmkRXOESoit311X1/34+MO37YY/vf96Pu89z+f5fJ73+5H4G1nAWWAPkAzoZL4LeAiU+SdLfrESKAZOAzeAVpl3AiogABgD5gImwPNn5yYgDngAXANKgZbbFw+J+jsnBdAJvA8KUNnNqUYBaP2LrwFXgQrAAtjmzAwfFG23RHtNkUhNinMaYiJ7gI6c3SkeoA4Q/l+oAdqB/mPpSVsLTu3US6FpXwDF9nVL9RmbVwSHaCTcPiV5xZUj96oaPsp1lSpg/vSwENdhc+KGyHCdtmvIKxYkZA51PyucUf36Kxv3n+uKmBqqWGVapPGM9JG5KUFzr6ohWJ7NAQnIBmI1geoge/mh9f29fdR+HPZGTZ2kmBwRKRmiI3jywi6Mi2ZL+oXbPztsRbOiV+b2dnUPdAIxKmBKmE4b8qgwLZUxF0XWl+4Rj9LF4hiNVxGkvPGuQxgXRkt371f7ANWrNx84l71Jv/mopRMYVAE/50TqjZ9+OCi50+i+cnytOj79yvDwqMtRaUnR2Vvs0r7cy85qW2s3oG77Nugzxc1UAG5gIrJ0pUBFaU6KAL5PC9P1lOWbReaWZaOXcs2eoaarwmErEsD36yczPG+tBwXQCAyMy/gcsALNQFNZvlkAn0ae5ouHJXt98fOi+svPZIhtqxOd9ttZotayS8hS5qnkC6xALBBoWhA1wdnf7QUCghRuQrWSlGQI11Q+fuk4f2TNhJp6OxesdX3AEiDB30x1QEvBjqVe+XnNQGN6imFsoOqEuHlijVApFe2ATbZxqL+RxmEBlgOjgE/mBOAC1PLZAIz74J9IloczCgzLcScwxO8N/b/4BZ4sCAP6Ouu4AAAAAElFTkSuQmCC&logoWidth=16) ![ENGLISH](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmahjongsoul.game.yo-star.com%2Fversion.json&label=ENGLISH&query=$.version&color=FF8C00&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADT0lEQVQ4jUXN2WtcVQDA4d+520xmsbOkM5OYNJkak5hJNQtE2mCgkj6ILUVEoTSIG0KVgpT4oIjig4qi5k0U8cWttr5IoUGoFBrRSilN1DRdNBMbkzTNNklmJplz7tx7fPDB7x/4BMDJZ0/kDw4fznquj1/1AM3Ia5/hyQpVDQDzi7OkExl2ptLUJOKcuzbO2V8vCOv1x+s/MKans3LuIyIdRynd0ly7uoTcKpPt7mN2coKqlLRm2/B8jTYExcIa+1v28Ol7J7TIf9hRCaVigfDunQR2JHA3lxl+qYxhaBKpDCuLC3QPPgJas3j9KoZpQjhMOl1H+K4Y1sJs0agrCUztM/zxGMeH2gjYEaSSzM3O4FgO4+dGEQLC4Si1u5qRrqK0WUQrhTW3IrmnM45lC159vp1kMoowobauntvzc9i2hVKKUDiMcl0W/84jXUm5JowhQIzk7leTRW0fGfA4m0/QfsegIRpgNKDJZOqZmvmdvs5u1gvbuK6ivFXGlRLbMBGAtb5hkAraXPzRZSkh6acGUXbZdMu8eWyIny63MDVxk3+W5onVxHBxaWxuZGlhhYrcRjzduU/llGl3KY0SJnlHcysTx/VW+eP6DZoMh0LI4eT571GywtTYz1y8fIWp8VlCdg1W0AkS3VYULJMzVolUIkMgaPHOyLv8cPo8k59/SeqhfRTXitS2t/DgkQYSjfWE1Rl+ufIXljAMqgEHp1RBahfTsdHKRxgWj77wBLmeNpr2H0AIF9Bow+C7T74l29fL1tgkVkVJNu7OMDjQT/TUN6B9TMNEBwJQkTQ/cB+itASRHSAEIGgtbhOrzbArlUYcasqpunjSLhTXiIaieNojFkvSmmvj2NvHwXbAMEEDAnTVhdI6zww+RyaewPJ9g9urKwRtC9NyuLO6zuDe3RSki7YCCK1B6/92IRCmBaEohmUQb85iKe2vVIqbdenaDOubCoFg8OWnyJ8eRXo+QeGDAIQBmOAp3nrxDfDgz/wMAuDeUFL31LewXZGEgkFeOfoYyT2NLE/cxGpvpuvQAbTvUcXgyd6H0VWH3q5+Jm78tiH431pnvCGeSzZxsKODvQM9mKEwSkne/+Ir5pYXiVgRpCoSCcY4NX3paw1D/wJx5WDqjkxa0wAAAABJRU5ErkJggg==&logoWidth=16) ![JAPANESE](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgame.mahjongsoul.com%2Fversion.json&label=JAPANESE&query=$.version&color=FF8C00&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADT0lEQVQ4jUXN2WtcVQDA4d+520xmsbOkM5OYNJkak5hJNQtE2mCgkj6ILUVEoTSIG0KVgpT4oIjig4qi5k0U8cWttr5IoUGoFBrRSilN1DRdNBMbkzTNNklmJplz7tx7fPDB7x/4BMDJZ0/kDw4fznquj1/1AM3Ia5/hyQpVDQDzi7OkExl2ptLUJOKcuzbO2V8vCOv1x+s/MKans3LuIyIdRynd0ly7uoTcKpPt7mN2coKqlLRm2/B8jTYExcIa+1v28Ol7J7TIf9hRCaVigfDunQR2JHA3lxl+qYxhaBKpDCuLC3QPPgJas3j9KoZpQjhMOl1H+K4Y1sJs0agrCUztM/zxGMeH2gjYEaSSzM3O4FgO4+dGEQLC4Si1u5qRrqK0WUQrhTW3IrmnM45lC159vp1kMoowobauntvzc9i2hVKKUDiMcl0W/84jXUm5JowhQIzk7leTRW0fGfA4m0/QfsegIRpgNKDJZOqZmvmdvs5u1gvbuK6ivFXGlRLbMBGAtb5hkAraXPzRZSkh6acGUXbZdMu8eWyIny63MDVxk3+W5onVxHBxaWxuZGlhhYrcRjzduU/llGl3KY0SJnlHcysTx/VW+eP6DZoMh0LI4eT571GywtTYz1y8fIWp8VlCdg1W0AkS3VYULJMzVolUIkMgaPHOyLv8cPo8k59/SeqhfRTXitS2t/DgkQYSjfWE1Rl+ufIXljAMqgEHp1RBahfTsdHKRxgWj77wBLmeNpr2H0AIF9Bow+C7T74l29fL1tgkVkVJNu7OMDjQT/TUN6B9TMNEBwJQkTQ/cB+itASRHSAEIGgtbhOrzbArlUYcasqpunjSLhTXiIaieNojFkvSmmvj2NvHwXbAMEEDAnTVhdI6zww+RyaewPJ9g9urKwRtC9NyuLO6zuDe3RSki7YCCK1B6/92IRCmBaEohmUQb85iKe2vVIqbdenaDOubCoFg8OWnyJ8eRXo+QeGDAIQBmOAp3nrxDfDgz/wMAuDeUFL31LewXZGEgkFeOfoYyT2NLE/cxGpvpuvQAbTvUcXgyd6H0VWH3q5+Jm78tiH431pnvCGeSzZxsKODvQM9mKEwSkne/+Ir5pYXiVgRpCoSCcY4NX3paw1D/wJx5WDqjkxa0wAAAABJRU5ErkJggg==&logoWidth=16)  

## 用前须知
> 魔改千万条，安全第一条。<br/>使用不规范，账号两行泪。<br/>本脚本仅供学习参考交流，请使用者于下载24小时内自行删除，不得用于商业用途，否则后果自负。<br/>本插件仅供学习参考交流，请使用者于下载24小时内自行删除，不得用于商业用途，否则后果自负。<br/>本插件仅供学习参考交流，请使用者于下载24小时内自行删除，不得用于商业用途，否则后果自负。  
  
> 警告：<br />雀魂游戏官方可能会检测并封号！<br />如产生任何后果与作者无关！<br />使用本脚本则表示同意此条款！  

### Telegram频道&交流群
[![频道 https://t.me/Mahjong_Soul](https://s2.loli.net/2022/11/08/4vS2BLMGhudkXQy.jpg)](https://t.me/Mahjong_Soul)[![交流 https://t.me/Mahjong_Soul_Chat](https://s2.loli.net/2022/11/08/KL8A7U9fDsZEmjp.jpg)](https://t.me/Mahjong_Soul_Chat)

可以直接点击图片进入，也可以通过扫码进入。

## 支持作者
[点我为作者发电](https://afdian.net/a/Avenshy)

注意：脚本完全免费使用，作者不盈利！

发电是自愿行为，作者**非常非常非常非常非常**感谢你！

## 使用说明  
**注意：无需按照原助手的使用说明进行配置！** 

以下内容仅适用于Windows系统！

如果你在使用其他系统，相信你有能力自行解决的😊
### 准备工作
1. 安装[Python](https://www.python.org/downloads/)。
   - 安装时必须勾选`pip`和`Add Python to environment variables`。
2. 下载本项目并解压。
   - 如果不会下载或网络环境较差，可以在[蓝奏云](https://wwtd.lanzout.com/b0485otfg#ilovecatfood)下载（密码：ilovecatfood）。
3. 安装依赖。
   - 直接运行`install_requirements.cmd`
   - 或者打开命令行界面输入`pip install -r requirements.txt`。

### 使用方法
1. 启动`mitmproxy`。
   - 直接运行`run.cmd`
   - 或者打开命令行界面输入`mitmdump -p 23410 -s addons.py`。
   - 这里的`23410`是本地端口，可以自行修改，下一步的端口也要同步修改。
2. 启动小助手，选择雀魂
3. 启动**带参数的**浏览器。
   - 将Chrome或者Edge的快捷方式 复制->粘贴 出现一个副本，对快捷方式副本 右键->属性->目标 的后面按一个空格后添加<br />` --proxy-server=127.0.0.1:23410 --ignore-certificate-errors https://game.maj-soul.com/1/`
   - 可以修改最后的网址以访问雀魂的其他服
4. 如果配置正确，小助手可以正常使用了

## Q&A🤔
1. 为什么启动浏览器之后没有效果？
   - 关闭所有浏览器窗口后再启动带参数的浏览器。
2. 进不去游戏？
   - 先使用浏览器进入游戏一次，关闭后再启动带参数的浏览器
3. 看不懂怎么办？出现错误怎么解决？
   - 提issue或者加群！

## 特别感谢❤️
[747929791/majsoul_wrapper](https://github.com/747929791/majsoul_wrapper)
