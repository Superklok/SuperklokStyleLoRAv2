import os

# Path to your exact style dataset folder
dataset_folder = os.path.join("dataset", "20_SuperklokStyle")
trigger_word = "SuperklokStyle"

# Master prompt data pulled directly from your generation workflow
style_description = (
    "Extreme macro industrial photograph of an 1980s retro-computer motherboard background canvas. "
    "The board is heavily cluttered and densely packed with highly concentrated mechanical hardware geometry spanning the entire frame. "
    "Symmetrical matrices of narrow, linear luminescent power veins and glowing conventional PCB traces weave tightly through an abundance "
    "of glossy cylindrical capacitors, miniature copper resistors, and solid integrated circuit chips. The entire composition utilizes a cohesive, "
    "variable color palette that shifts naturally without forcing any single hardcoded hue. Vintage CRT television monitor hardware filter overlay applied. "
    "Sharp analog horizontal scanlines, glowing color phosphor bleeding boundaries, high-density aperture grille sub-pixel layout, deep analog contrast, "
    "immersive hardware design, extreme color saturation, glowing luminescent traces, deep rich blacks, high dynamic range, intense analog contrast, ultra-vivid electronics,"
)

# This description isolates the text so the letters don't permanently bake into your style
text_protection_caption = (
    "The absolute only words written on this graphic are 'Superklok Labs'. "
    "The lettering is rendered in a razor-sharp, glowing multi-hued phosphor retro-terminal font with a bold black shadow outline. "
    "The text is tightly nested directly into the dense motherboard assembly, showcasing an ultra-tight, contour-hugging placement "
    "where physical chips, capacitors, and resistors crowd immediately around the edges of the font characters. The components are packed "
    "with zero gap clearances, sitting extremely close to the lettering without structurally overlapping, obscuring, or deforming the text. "
    "Text spelling accuracy is critical, do not alter or deform the characters 'Superklok Labs'. The letters emit high-intensity neon backlighting "
    "that blooms cleanly outward, looking as if it is actively fueled by the linear electrical power veins running directly out of the adjacent tightly packed hardware,"
)

if not os.path.exists(dataset_folder):
    print(f"Error: The directory '{dataset_folder}' does not exist. Please check your folder path.")
else:
    count = 0
    # Loop over all files in the directory
    for filename in os.listdir(dataset_folder):
        if filename.lower().endswith('.png'):
            # Strip the .png extension to match the base name exactly
            base_name = filename[:-4]
            txt_filename = f"{base_name}.txt"
            txt_path = os.path.join(dataset_folder, txt_filename)
            
            # Combine your new brand trigger word, the style context, and the text protection caption
            full_style_caption = f"{trigger_word}, {style_description}, {text_protection_caption}"
            
            # Write a fresh text file with the complete dataset template
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(full_style_caption)
            count += 1
            
    print(f"Success! Generated {count} text sidecar files with high-density master prompts for '{trigger_word}'.")