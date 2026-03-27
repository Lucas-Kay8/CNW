---
name: 菜鸟无忧-ppt
description: 菜鸟无忧 PPT presentation generation skill. Enforces the official visual style, animation logic, and layout structures for Qingzhou training course web slides.
---

# 菜鸟无忧 PPT Generator Skill (轻舟演示文案系统)

当用户要求“制作菜鸟无忧PPT”、“使用菜鸟无忧风格”、“以菜鸟无忧的格式做PPT/文稿”时，请严格遵守本 Skill 描述的视觉方案、代码结构及文案呈现方式。

## 1. 核心设计理念 (Philosophy)

- **视觉冲击**：如同发布会一般，要求极简、深色或留白、大图片、强对比。
- **顺滑沉浸**：一页（100vh），原生滚动捕捉（Scroll Snap），进入时伴随呼吸感（Fade + Transform）。
- **去冗余**：绝不要像Word文档那样密密麻麻地罗列要点，用视觉层级引导注意力。

## 2. 视觉规范 (Brand & Typography)

- **品牌强调色** (cainiao Blue)：`--accent: #008aff;`
- **背景色**：多用全屏深色深邃背景（纯黑或者透明度0.5-0.8的深色渐变）。如果不用图片时：`--bg: #111111;`
- **字体族**：`'General Sans', -apple-system, sans-serif`
- **默认文字主色**：多数是白字（反白设计），或者大黑字。
- **高亮文本**：金句、关键字使用颜色 `--accent` 或者特殊渐变。

## 3. 核心布局架构 (Standard DOM Structure)

**极度重要：层级遮挡控制。**
为了避免在浏览器内文字不呈现（opacity/transform渲染异常或z-index覆盖），所有的 Slide 必须使用极其严格与健壮的分层 HTML 结构（三层结构）：

```html
<section class="slide" id="slide-[id]" style="background: #000; padding: 0;">

    <!-- 1. 置底背景层 (z-index: 0) -->
    <!-- 带有图片缓慢缩放的入场动画 (reveal-zoom) -->
    <div class="slide-bg reveal-zoom" style="background-image: url('assets/images/[YOUR-IMG.png]'); z-index: 0; opacity: 0.85;"></div>

    <!-- 2. 中间遮罩层 (z-index: 1) -->
    <!-- 用来压暗背景，保证文字绝壁清晰 (Radial/Linear Gradient) -->
    <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.2) 60%, transparent 100%); z-index: 1; pointer-events: none;"></div>

    <!-- 3. 顶层内容容器 (z-index: 10) -->
    <!-- 使用 flex 控制内容的九宫格分布（例如左上对齐） -->
    <div class="slide-content-overlay" style="justify-content: flex-start; align-items: flex-start; padding: 12vh 8vw; z-index: 10;">
        
        <!-- 带有入场动画的文字块 (reveal-up) -->
        <div class="reveal-up delay-1" style="max-width: 800px; position: relative; z-index: 20;">
            <h1 style="font-size: clamp(3rem, 6vw, 4.5rem); color: #fff; font-weight: 800; border-left: 8px solid var(--accent); padding-left: 1.5rem;">
                核心大标题
            </h1>
            <p style="font-size: clamp(1.2rem, 3vw, 2rem); color: #fff; opacity: 0.95;">
                正文内容，高亮词汇：<span style="color: var(--accent); font-weight: 700;">重点词解</span>
            </p>
        </div>

    </div>
</section>
```

*(注意：对于页面第一次加载的首屏 Slide，务必要在 `<section class="slide visible">` 中提前写死 `visible`，防止 JS 初始化时的白页隐患。)*

## 4. 图文搭配版式 (Layout Patterns)

1. **封面/终页 (Hero Focus)**:
   - 全屏留白/纯色背景。文字绝对居中 (`text-align: center; justify-content: center; align-items: center;`)。
   - 标题字体做到巨大（6rem以上），利用 `text-gradient` 或 `text-shadow` 加强张力。

2. **名言/金句页面 (Quote Snapshot)**:
   - 左边配一张有视觉张力的图片（或者全背景压暗）。
   - 正文使用巨大的粗斜体，并且带有左侧大竖杠强调线 (`border-left: 15px solid var(--accent);`)。

3. **双栏对比结构 (Split/Versus)**:
   - 展现新旧对比（如：人工 VS AI）。
   - 外层使用 `display: grid; grid-template-columns: 1fr 1fr; gap: 4rem;`，配合 `backdrop-filter: blur(20px);` 实现多重 Glassmorphism 卡片设计。

4. **瀑布流/并排图表 (Bento Grid)**:
   - 用大模块拼出小模块（类似于Apple系统的桌面小组件卡片），适用于展现能力点。

## 5. 动画与交互引擎 (Animation & Interaction)

一切以不抢戏、有高级感为原则。
CSS 定义全局渐现渐变 Class，并通过统一的 JavaScript 脚本控制翻页与动画触发。

### 核心 CSS 动画规则

```css
.reveal-up { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease, transform 0.8s ease; }
.slide.active .reveal-up { opacity: 1; transform: translateY(0); }

.reveal-zoom { opacity: 0; transform: scale(1.1); transition: opacity 1.5s ease, transform 2.5s ease; }
.slide.active .reveal-zoom { opacity: 1; transform: scale(1); }
```

### 标准 JavaScript 交互逻辑

所有生成的 PPT 必须在 `</body>` 前包含以下逻辑（或引用 `assets/scripts/qingzhou-ppt.js`）：

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    let currentStep = 0;

    // 1. 初始化导航 UI
    const navDots = document.createElement('div');
    navDots.className = 'ppt-nav-dots';
    const progressBar = document.createElement('div');
    progressBar.className = 'ppt-progress';
    document.body.appendChild(navDots);
    document.body.appendChild(progressBar);

    slides.forEach((_, i) => {
        const dot = document.createElement('div');
        dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
        dot.onclick = () => goToSlide(i);
        navDots.appendChild(dot);
    });

    // 2. 翻页核心逻辑
    function goToSlide(index) {
        if (index < 0 || index >= slides.length) return;
        slides[currentStep].classList.remove('active');
        document.querySelectorAll('.nav-dot')[currentStep].classList.remove('active');
        
        currentStep = index;
        
        slides[currentStep].classList.add('active');
        document.querySelectorAll('.nav-dot')[currentStep].classList.add('active');
        progressBar.style.width = `${((currentStep + 1) / slides.length) * 100}%`;
        
        // 自动触发页面内的动画 (IntersectionObserver 的替代方案)
        slides[currentStep].querySelectorAll('.reveal-up, .reveal-zoom').forEach(el => {
            el.style.animation = 'none';
            el.offsetHeight; // trigger reflow
            el.style.animation = null;
        });
    }

    // 3. 键盘事件监听 (核心需求: 物理按键翻页)
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
            goToSlide(currentStep + 1);
        } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft' || e.key === 'Backspace') {
            goToSlide(currentStep - 1);
        }
    });

    // 4. 初始化第一页
    goToSlide(0);
});
```

## 6. 图片处理与文案原则

- **必出神图**：搭配高质量大片，拒绝白底网图。
- **减字**：把大段介绍缩减成一句话。
- **口语与深刻并存**：文案风格要求干脆利落。
- **指示器与进度条**：必须始终显示当前进度，让观众对流程有掌控感。
