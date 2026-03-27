from PIL import Image
import os

source_path = "/Users/lucas/.gemini/antigravity/brain/ffd0124c-4d43-4a3e-88db-dcc822570286/ai_level_icons_set_1769933066738.png"
output_dir = os.path.dirname(source_path)

try:
    img = Image.open(source_path)
    img = img.convert("RGBA")  # Convert to RGBA for transparency
    
    datas = img.getdata()
    new_data = []
    
    # Simple transparency filter: Turn white-ish pixels to transparent
    for item in datas:
        # Check if pixel is white-ish (R>240, G>240, B>240)
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    w, h = img.size
    w_third = w // 3

    # Icon 1: Foundation (Purple)
    icon1 = img.crop((0, 0, w_third, h))
    path1 = os.path.join(output_dir, "icon_basic_foundation.png")
    icon1.save(path1, "PNG")
    print(f"Saved transparent: {path1}")

    # Icon 2: Core (Blue)
    icon2 = img.crop((w_third, 0, w_third * 2, h))
    path2 = os.path.join(output_dir, "icon_must_have_core.png")
    icon2.save(path2, "PNG")
    print(f"Saved transparent: {path2}")

    # Icon 3: High Value (Gold)
    icon3 = img.crop((w_third * 2, 0, w, h))
    path3 = os.path.join(output_dir, "icon_high_value.png")
    icon3.save(path3, "PNG")
    print(f"Saved transparent: {path3}")

except Exception as e:
    print(f"Error: {e}")
