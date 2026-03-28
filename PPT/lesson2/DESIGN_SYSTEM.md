# 轻舟课程视觉系统手册 (Qingzhou PPT Design System 2.0)

本手册基于 **Lesson 2: AI Prompt Engineering** 的前三页打磨成果提炼，定义了“Apple 极简主义”的核心视觉资产与实施逻辑。

---

## 1. 排版系统 (Typography Mastery)

我们严禁在 HTML 中硬编码字号，所有文字必须归口至以下标准类名：

### A. 标题层级 (Hero Hierarchy)
1. **`.t-hero-main` (封面级)**:
   - **参数**: `clamp(3rem, 7vw, 5.5rem)` / `900` / `LH 1.2` / `-0.03em`
   - **场景**: 仅用于课程首页或章节大封面。
2. **`.t-hero-impact` (冲击级)**:
   - **参数**: `clamp(2.2rem, 5.5vw, 4.4rem)` / `900` / `white-space: nowrap`
   - **场景**: 灵魂拷问页、金句页。强制单行展示，增强横向视觉张力。
3. **`.t-hero-page` (内页级)**:
   - **参数**: `clamp(2rem, 4.5vw, 3.8rem)` / `800` / `LH 1.3`
   - **场景**: 所有内容页的正标题。

### B. 正文层级 (Text Hierarchy)
- **`.t-subtitle`**: 叙事副级。`clamp(1.2rem, 2.5vw, 2rem)`，`opacity: 0.75`。
- **`.t-digit`**: 数字增强。`900` 加粗 + `Accent Orange`，增强数据冲击力。
- **`.t-card-title`**: Bento 卡片标题。`1.85rem` / `800`。
- **`.t-body`**: 阅读级文字。`1.15rem` / `LH 1.7` / `opacity: 0.65`。

---

## 2. 空间与节奏 (Spacing & Rhythm)

通过“垂直间距系统”确保每一页都有 Apple 级的呼吸感：

- **`.v-gap-impact` (5.5rem)**: 主标题下方的“思考留白”，用于灵魂拷问。
- **`.v-gap-hero` (3.5rem)**: 封面页或普通页面的主副标题间距。
- **`.v-gap-section` (8vh)**: 标题与下方 Bento 网格/列表之间的逻辑区隔。
- **`.v-gap-lg` (8vh)**: 底部金句或总结块的浮动高度。

---

## 3. 视觉组件与材质 (Materials & Visuals)

### A. 玻璃拟态 (Glassmorphism 2.0)
- **容器**: `.bento-card`
- **材质**: `rgba(255,255,255,0.03)` 背景 + `blur(40px)` + `border: 1px solid rgba(255,255,255,0.1)`。
- **圆角**: 统一 `28px` (iOS Widget 标准)。

### B. 背景噪音控制 (Atmosphere)
- **`.buzzword-rain`**: 废话雨效果。
- **参数**: `opacity: 0.05` -> `0.25`，配以 `2.5px` 动态模糊。确保背景作为“氛围层”存在，不干扰文字阅读。

---

## 4. 叙事逻辑规范 (Narrative Guidelines)

- **封面页**: 主标题必须具备“外脑”等高光词汇。
- **拷问页**: 必须采用“指令 vs 运气”或“专业 vs 业余”的二元对比叙事。
- **内容页**: 采用 Bento Grid 结构，信息点不得超过 3 个，确保单页认知负荷最小化。

---
> [!NOTE]
> **设计师寄语**：
> 顶级的设计不是堆砌，而是对间距、字重与虚实层级的极致克制。本系统各参数已完成多屏校准，后续每张 Slide 均需强制执行“设计语义化”。
