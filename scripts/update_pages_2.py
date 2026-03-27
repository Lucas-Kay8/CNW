import re

file_path = '/Users/lucas/.gemini/antigravity/brain/13c90a78-a56d-48ea-89a4-6ae42edf646b/模块一_逐页大纲.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split the content by '## Page '
parts = re.split(r'## Page (\d+)：', content)

new_content = parts[0]

new_page_5 = """## Page 5：全局视野：训练师的“超级战车”拼图

*(注：本页为承上启下的核心架构图，向学员展示接下来学习的各项技能如何组装成一个完整的智能体应用)*

* **幻灯片版面排版结构**：
  * **整体结构：中心辐射型/方程式爆炸视图**。
  * **视觉重心**：正中央放置一个闪光的“AI Agent (超级战车)” 虚拟投影。
  * **四周图层（四个带引线的发光模块卡片）**：
    1. **底座模块（底盘）**：标明“大模型引擎 (System 1/2)”。（旁白：刚才我们已经学会了怎么选发动机）。
    2. **控制模块（方向盘）**：标明“高阶Prompt约束”。
    3. **记忆模块（副油箱/雷达）**：标明“RAG专属知识库”。
    4. **流程模块（传动履带）**：标明“Workflow自动化工作流”。
  * **视觉连线**：四个模块用流动的光线连接到中央的智能体投影上，体现它们不可分割的组装关系。

* **幻灯片主干文字**：
  * 标题：总成蓝图：四位一体的工程架构
  * 核心论点：“定好了模型引擎（大脑）只是第一步。要让它成为不翻车的企业级应用，我们接下来必须亲自为它装上‘方向盘（Prompt）’、‘外部记忆库（RAG）’，最后铺设一条‘标准铁轨（Workflow）’。”

---

"""

# Reassemble and bump numbers
for i in range(1, len(parts), 2):
    page_num = int(parts[i])
    page_content = parts[i+1]
    
    # We already have page 1, 2, 3, 4
    if page_num <= 4:
        new_content += f"## Page {page_num}：{page_content}"
        # We want to insert the new page right AFTER page 4
        if page_num == 4:
            new_content += new_page_5
    else:
        # Bump the rest
        new_page_num = page_num + 1
        new_content += f"## Page {new_page_num}：{page_content}"

# Additionally, fix the image caption references if there are any that need bumping past 4
# Actually, the user currently has images for Page 2, Page 3, Page 5 (wait, old 4 was 5?). 
# Let's dynamically fix text that might say "模块一第五页配图" to "第六页配图"
def replace_number_words(match):
    text = match.group(0)
    mapping = {
        '第五页': '第六页',
        '第六页': '第七页',
        '第七页': '第八页',
        '第八页': '第九页',
        '第九页': '第十页',
        '第十页': '第十一页',
        '第十一页': '第十二页'
    }
    for k, v in mapping.items():
        if k in text:
            return text.replace(k, v)
    return text

new_content = re.sub(r'!\[模块一第(五|六|七|八|九|十|十一)页配图\]', replace_number_words, new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("done")
