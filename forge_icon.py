from PIL import Image, ImageDraw

def create_tactical_icon():
    # Dimensionen (Standard für Windows Icons)
    size = (256, 256)
    
    # 1. Basis: Dunkler, taktischer Hintergrund (Fast Schwarz)
    img = Image.new('RGBA', size, color=(20, 20, 20, 255))
    draw = ImageDraw.Draw(img)
    
    # 2. Akzent: Die "Hot Corner" oben links (Signalrot)
    # Ein scharfes Dreieck, das die Funktion symbolisiert
    corner_points = [(0, 0), (120, 0), (0, 120)]
    draw.polygon(corner_points, fill=(255, 40, 40, 255))
    
    # 3. Rahmen: Subtiler Rand, damit es auf dunklen Wallpapern sichtbar bleibt
    draw.rectangle([(0,0), (255,255)], outline=(60, 60, 60, 255), width=2)
    
    # 4. Speichern als High-Res ICO (System-Einsatz)
    img.save("shadow.ico", format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    
    # 5. Export für Propaganda (PNG für Sharing/Social Media)
    # Das erlaubt dir, das Icon direkt als Bild zu teilen, ohne Screenshots machen zu müssen.
    img.save("shadow_preview.png", format='PNG')
    
    print("[SYSTEM] Insignie geschmiedet: shadow.ico & shadow_preview.png")

if __name__ == "__main__":
    try:
        create_tactical_icon()
    except ImportError:
        print("[ERROR] Pillow fehlt. Installiere es mit 'pip install pillow'")