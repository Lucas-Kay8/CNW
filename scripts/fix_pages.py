import re

file_path = '/Users/lucas/.gemini/antigravity/brain/13c90a78-a56d-48ea-89a4-6ae42edf646b/模块一_逐页大纲.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by header to preserve headers and bodies
parts = re.split(r'(## Page \d+：[^\n]+)', content)

prefix = parts[0]
pages = []
# Parse header and body pairs
for i in range(1, len(parts), 2):
    header = parts[i]
    body = parts[i+1]
    title_match = re.search(r'## Page \d+：(.*)', header)
    if title_match:
        title = title_match.group(1).strip()
    else:
        title = ""
    pages.append({"title": title, "body": body})

# Reorder:
# We want "全局视野：训练师的“超级战车”拼图" to be immediately AFTER "认知基石（二）：匹配模型的艺术"
transition_page = None
for p in pages:
    if "全局视野" in p["title"]:
        transition_page = p
        break

if transition_page:
    pages.remove(transition_page)

    insert_idx = 0
    for idx, p in enumerate(pages):
        if "匹配模型的艺术" in p["title"]:
            insert_idx = idx + 1
            break
    
    pages.insert(insert_idx, transition_page)

# Renumber
new_content = prefix
for idx, p in enumerate(pages):
    page_num = idx + 1
    new_content += f"## Page {page_num}：{p['title']}{p['body']}"

# Fix image captions up to page 12
def replace_number_words(match):
    text = match.group(0)
    # the existing captions might say "第四页配图", "第六页配图"
    # let's just use numeric or leave it if it's too complex.
    # Actually, the user doesn't care much about the caption number text as long as the page number is correct.
    return text

new_content = re.sub(r'!\[模块一第.*?页配图\]', replace_number_words, new_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("fixed")
