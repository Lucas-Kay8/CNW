import re

file_path = '/Users/lucas/.gemini/antigravity/brain/13c90a78-a56d-48ea-89a4-6ae42edf646b/模块一_逐页大纲.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split the content by '## Page '
parts = re.split(r'## Page (\d+)：', content)

new_content = parts[0]

new_page_2 = """## Page 2：你的生态位：2026年企业AI人才的三轴星图

* **幻灯片版面排版结构**：
  * **整体结构：金字塔或三层阶梯递进式图表**。
  * **排版层级**：从底向上的三级阶梯，颜色由浅入深，代表影响层级的跃升。
    * **底层（银灰色，点）**：标题“AI管理师（单兵）”。文案：“聚焦点：个人提效。武器：对话框里的提示词。”
    * **中层（发光的主题蓝，线）**：标题“AI训练师（工序）”。文案：“聚焦点：团队流程固化与自动化。武器：RAG知识库+Workflow工作流。” 本层必须用发光框高亮，旁边加上“👉 你在这里 (YOU ARE HERE)”的醒目标记。
    * **顶层（暗金/深紫色，面）**：标题“AI架构师（全局）”。文案：“聚焦点：颠覆商业模式与组织重组。武器：系统级规划。”
  * **整体背景**：深色星空或企业大厦的抽象线框底图。

* **幻灯片主干文字**：
  * 标题：坐标定调：你在企业AI人才地图的哪一层？
  * 讲师核心主张：“如果你只会写一段让AI帮你润色邮件的提示词，你随时可以被替代。本课程的目标，是把你拔高到工厂的‘流程规划师’，打造发给团队一键使用的超级工具。”

---

"""

# Reassemble and bump numbers
for i in range(1, len(parts), 2):
    page_num = int(parts[i])
    page_content = parts[i+1]
    
    if page_num == 1:
        new_content += f"## Page 1：{page_content}"
        new_content += new_page_2
    else:
        new_page_num = page_num + 1
        new_content += f"## Page {new_page_num}：{page_content}"

# Additionally, fix the image caption references if there are any (e.g. "模块一第二页配图" -> "模块一第三页配图")
import itertools
def replace_number_words(match):
    text = match.group(0)
    mapping = {
        '第二页': '第三页',
        '第三页': '第四页',
        '第四页': '第五页',
        '第五页': '第六页',
        '第六页': '第七页',
        '第七页': '第八页',
        '第八页': '第九页',
        '第九页': '第十页',
        '第十页': '第十一页'
    }
    for k, v in mapping.items():
        if k in text:
            return text.replace(k, v)
    return text

new_content = re.sub(r'!\[模块一第(二|三|四|五|六|七|八|九|十)页配图\]', replace_number_words, new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("done")
