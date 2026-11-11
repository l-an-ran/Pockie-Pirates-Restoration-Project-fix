# 《小小海贼王》(Pockie Pirates) 怀旧复活与战斗引擎修复项目

[![Language](https://img.shields.io/badge/Language-English%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Battle%20Engine%20Restored-brightgreen.svg)](#)
[![Upstream](https://img.shields.io/badge/Upstream-GetsuLid%2FPockie--Pirates--Restoration--Project-orange.svg)](https://github.com/GetsuLid/Pockie-Pirates-Restoration-Project)

> 🌐 **语言切换 / Language Navigation**：  
> [简体中文](README_CN.md) | [English](README.md)

---

## 📌 上游原项目致谢 (Upstream Credit)

本项目仓库（Fork / 修复维护版）：  
👉 **[https://github.com/l-an-ran/Pockie-Pirates-Restoration-Project-fix](https://github.com/l-an-ran/Pockie-Pirates-Restoration-Project-fix)**

本项目基于 **@GetsuLid** 开源的经典原版恢复工程开发：  
👉 **原始上游项目：[https://github.com/GetsuLid/Pockie-Pirates-Restoration-Project](https://github.com/GetsuLid/Pockie-Pirates-Restoration-Project)**

在此由衷感谢原作者及海内外开源社区对 2012 年经典页游《小小海贼王》（Pockie Pirates）资产挖掘、协议破译和底层服务端构建所奠定的坚实基础！

---

## 🚀 最近核心工作与攻关进展 (Recent Work & Fixes)

在原上游项目的基础上，我们针对原项目中**缺失的战斗系统逻辑、贴图索引乱码、角色动作突变以及渲染表现**进行了深度逆向破解与高保真修复，重点成果如下：

### 1. 深度破译二进制图集索引包 `data.tpi`（根治切片错位乱码）
* **问题根因**：原先的图集切片逻辑误认为导出的图集编号直接等同于 `.ani` 动作配置文件中的编号，导致切出的全是不相关的碎图、杂色块或空白。
* **攻关成果**：
  * 全面逆向解析了 `assets/Env/data.tpi` 二进制资源描述表，建立了 203 张大图集的全局真实寻址映射；
  * 破解出主角剑豪（`soldier1001`）实际映射在大图集 `img_00124`，见习剑士怪物（`soldier10004`）映射在 `img_00119`；
  * 重新切分出双方纯正原版的**待机、呼吸、冲锋前刺、受击后仰及 5 帧居合拔刀技能连贯动作序列**。

### 2. 战场纯净背景高保真还原与杂图切除
* **背景纠偏**：检索分析 `assets/Env/ani/icon.ani`，精确定位到第一战（风车村浅滩木甲板海战）对应的官方原版原生战场背景 `campbattlebg_1.png`（1000×600 标准无损原图）；
* **去除杂物**：彻底剔除之前误拼接的非原生 HUD、聊天条与占位贴图，保证战场画面的原汁原味与 100% 官方视觉对齐。

### 3. 敌方朝向纠偏与角色动作状态机 Bug 根治
* **敌方朝向修正**：增加水平镜像反转（`scaleX(-1)`），使右侧敌方单位正对主角迎战；
* **根治模型突变 Bug**：排查并修复了呼吸动画定时器中怪物贴图变量误赋给主角精灵图的严重笔误（此前导致主角在未受击时突变成怪物模型）；
* **动作状态机保护**：重构了角色状态管理，确保角色在执行冲锋（attack）、居合斩技能（skill）、受击硬直（hurt）期间，呼吸定时器严格互斥，保证整套技能连招连贯流畅。

### 4. 高保真原生伤害数字飘字与暴击排版重构
* **剔除乱码切片**：废除了原代码中误将动画特效碎片当作数字贴图提取的错误逻辑；
* **1:1 原版矢量伤害字体引擎**：
  * **普通伤害**：高饱和橙红色（`#ff3b14`）大字体，带 1.5px 纯黑外描边与深邃四向阴影（`-42`），配合上浮弹性回弹动画；
  * **暴击伤害**：深红隶书“暴击”大字加高亮金黄暴击数字（`-238`），附带缩放与震颤反馈；
  * **技能横幅**：橙金渐变、深红粗描边的 52px 倾斜大字【剑技·狂风】配合暗影横幅震屏绽放。

### 5. 剔除特效不透明方块，优化纯正打击反馈
* **问题修复**：针对 Flash 加色混合（Additive Blending / `BlendMode.ADD`）在标准 Web DOM 渲染中产生的不透明杂色矩形边框问题，移除了生硬的外部光刃贴图；
* **打击增强**：改用纯正的受击高光闪白（`brightness(2.6)`）与击退顿挫，让主角自身 5 帧连贯居合斩（拔刀、延伸、收刀）的视觉表现干净利落、拳拳到肉。

### 6. 风车村第一战役真实配置闭环
* 对照官方 SQLite 数据库 `cfg_task`（100003【勇敢的战斗】）、`cfg_camp`（1001【海贼袭击战】）、`cfg_army`（10101【见习剑士团一】）与 `cfg_monster`（100001）；
* 双方均置于官方 9 宫格阵型（前排中路 5 号位），完整跑通回合交替、技能释放、敌方战败渐隐退场及 3 星胜利结算弹窗闭环。

---

## 🛠️ 快速启动与体验指南

### 1. 运行服务端与启动器
在 Windows 上直接双击运行根目录下的脚本：
```cmd
一键启动游戏.bat
```
*(或在命令行中运行 `python launcher.py`)*

### 2. 访问与体验
* **主游戏页面**：浏览器访问 `http://127.0.0.1:8888/`
* **战斗引擎高保真演示**：浏览器直接打开 `http://127.0.0.1:8888/battle.html`
* **服务端健康状态**：`http://127.0.0.1:8888/status`

---

## ⚖️ 免责声明 (Disclaimer)

1. 本项目所有代码及逆向研究成果仅供**计算机软件逆向工程技术研究、个人学习与怀旧交流**使用。
2. 本项目**严禁用于任何商业目的与营利行为**。
3. 游戏的所有素材、音乐、原画及相关商标版权归原游戏版权所有方所有。
