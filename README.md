# Pockie Pirates - Preservation & Restoration Project (Community Fix)

[![Language](https://img.shields.io/badge/Language-English%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](#)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Battle%20Engine%20Restored-brightgreen.svg)](#)
[![Upstream](https://img.shields.io/badge/Upstream-GetsuLid%2FPockie--Pirates--Restoration--Project-orange.svg)](https://github.com/GetsuLid/Pockie-Pirates-Restoration-Project)

> 🌐 **Language Switch / 语言切换**:  
> [English](README.md) | [简体中文](README_CN.md)

---

## 📌 Upstream Project & Attribution

This repository is maintained at:  
👉 **[https://github.com/l-an-ran/Pockie-Pirates-Restoration-Project-fix](https://github.com/l-an-ran/Pockie-Pirates-Restoration-Project-fix)**

This project is directly based on the foundational restoration work by **@GetsuLid**:  
👉 **Original Upstream Repository: [https://github.com/GetsuLid/Pockie-Pirates-Restoration-Project](https://github.com/GetsuLid/Pockie-Pirates-Restoration-Project)**

Special thanks to **@GetsuLid** and the community for preserving the classic 2012 web Flash game *Pockie Pirates* (*Xiaoxiao Haizeiwang*), excavating historical client assets, and establishing the Python AMF3 server architecture.

---

## 🚀 Recent Work & Core Fixes

Building upon the upstream repository, our recent work focuses on **re-engineering the missing combat logic, fixing asset index mismatch bugs, repairing sprite animation state machines, and achieving high-fidelity battle rendering**:

### 1. Binary Index Decryption (`data.tpi`) & Correct Atlas Remapping
* **Root Problem:** The original asset slicing logic mistakenly assumed that the exported atlas filenames (`img_N`) corresponded 1:1 with the indices in the `.ani` configuration files, resulting in fragmented garbage textures and misplaced sprites.
* **Our Solution & Fix:**
  * Reverse-engineered the binary `assets/Env/data.tpi` pack to build an accurate global memory lookup table across 203 large atlases;
  * Mapped protagonist Swordsman (`soldier1001`) to its true position in `img_00124`, and the Trainee Swordsman enemy (`soldier10004`) to `img_00119`;
  * Cleanly re-extracted all native action frames: idle breathing, dash charge, hurt impact, and the complete 5-frame Iai slash skill sequence.

### 2. Native Clean Battle Background & Artifact Removal
* **Accurate Background Mapping:** Analyzed `assets/Env/ani/icon.ani` to locate the authentic native stage background `campbattlebg_1.png` (1000×600 clean lossless original) for the Windmill Village shallow-water plank duel.
* **Clutter Removal:** Removed synthetic HUD overlays, chatbars, and mismatched composite images to maintain 100% visual fidelity to the original game.

### 3. Orientation Inversion & Sprite State Machine Bug Elimination
* **Facing Direction Fix:** Added horizontal mirroring (`scaleX(-1)`) to right-side enemy units, ensuring they properly face the protagonist in combat.
* **Fixed Model Mutation Bug:** Discovered and eliminated a timer variable typo that repeatedly overwrote the protagonist's sprite with the enemy texture during idle breathing loops.
* **State Machine Guard:** Enforced strict mutually exclusive states (idle, attack dash, Iai skill slash, and hurt stagger) so that breathing timers cannot interrupt active animation sequences.

### 4. Vector-Engineered Native Damage Floaters & Critical Hit Typography
* **Scrapped Garbage Slices:** Deprecated the legacy script that erroneously sliced animation particle effects (`animation_*.pvr`) as numeric text.
* **1:1 High-Fidelity Typography Engine:**
  * **Standard Damage:** High-saturation `#ff3b14` bold typography with 1.5px black outer strokes and multi-directional drop shadows (`-42`), animated with elastic float-up physics.
  * **Critical Hits:** Deep-crimson "CRIT" header combined with brilliant gold damage numerals (`-238`) and zoom-shake feedback.
  * **Skill Banner:** 52px italic gradient typography for Swordsman's signature skill *Sword Art: Gale* (剑技·狂风) accompanied by an impact shockwave.

### 5. Additive Blending Glitch Fix & Hit Impact Polish
* **Glitch Elimination:** In standard web DOM rendering, Flash's additive blending mode (`BlendMode.ADD`) causes ugly rectangular black borders around external aura sprites. These intrusive external slices have been removed.
* **Impact Enhancement:** Polished native hit feedback using high-intensity flash-white effects (`brightness(2.6)`) alongside the protagonist's fluid 5-frame draw-and-sheathe Iai cut.

### 6. Chapter 1 Quest 100003 Official Battle Flow Closure
* Bound the SQLite game configuration tables (`cfg_task` 100003, `cfg_camp` 1001, `cfg_army` 10101, and `cfg_monster` 100001);
* Positioned combatants on the authentic 9-grid front-center slot (position 5), successfully completing the turn sequence, skill execution, enemy fade-out, and 3-star victory dialogue modal.

---

## 🛠️ Quick Start & Running Guide

### 1. Launch Server and Game Launcher
On Windows, double-click:
```cmd
一键启动游戏.bat
```
*(Or run `python launcher.py` via terminal)*

### 2. Access Links
* **Main Game Portal:** `http://127.0.0.1:8888/`
* **High-Fidelity Battle Showcase:** `http://127.0.0.1:8888/battle.html`
* **Server Health Status:** `http://127.0.0.1:8888/status`

---

## ⚖️ Disclaimer

1. All code and research in this repository are strictly for **reverse engineering research, software preservation, and educational purposes**.
2. This project is **strictly non-commercial**.
3. All original assets, audio, art, and intellectual property belong to their respective original game developers and copyright holders.
