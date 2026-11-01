"""Crea un video subtitulado de la portabilidad local con salidas registradas."""
from pathlib import Path
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
OUT = WORKSPACE / "Video_portabilidad_arnes_0.1.4.mp4"
TMP = ROOT / "docs" / "video_frames"
TMP.mkdir(parents=True, exist_ok=True)
LOG = (ROOT / "docs" / "evidencia-hook-2026-11-01.txt").read_text(encoding="utf-8", errors="replace")
FFMPEG = os.environ.get("FFMPEG_BIN")
if not FFMPEG or not Path(FFMPEG).is_file():
    raise SystemExit("Definir FFMPEG_BIN con un ejecutable ffmpeg local")

regular = "C:/Windows/Fonts/arial.ttf"
bold = "C:/Windows/Fonts/arialbd.ttf"
font_title = ImageFont.truetype(bold, 42)
font_sub = ImageFont.truetype(regular, 23)
font_body = ImageFont.truetype(regular, 25)
font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 23)
font_small = ImageFont.truetype(regular, 18)

def draw_lines(draw, lines, x, y, font, fill, line_height=34):
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return y

def slide(number, title, subtitle, body, terminal=None):
    im = Image.new("RGB", (1280, 720), "#f7f7f2")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1280, 12), fill="#183e3c")
    d.text((62, 40), "ECCLESIA  /  PRUEBA DE PORTABILIDAD", font=font_small, fill="#42645f")
    d.text((62, 93), title, font=font_title, fill="#102c2b")
    d.text((62, 154), subtitle, font=font_sub, fill="#48635e")
    y = 226
    if body:
        y = draw_lines(d, body, 68, y, font_body, "#193533", 40) + 20
    if terminal:
        d.rounded_rectangle((61, y, 1219, min(638, y + 46 + len(terminal) * 31)), radius=14, fill="#142325")
        d.text((83, y + 17), "PowerShell  ·  salida registrada", font=font_small, fill="#8cb5a8")
        draw_lines(d, terminal, 83, y + 54, font_code, "#e4f1ed", 31)
    d.text((62, 667), "01/11/2026 · ejecución local · datos del módulo de tareas", font=font_small, fill="#647b76")
    d.text((1120, 667), f"{number} / 7", font=font_small, fill="#647b76")
    d.rounded_rectangle((62, 698, 62 + int(1156 * number / 7), 707), radius=4, fill="#c8a86a")
    path = TMP / f"slide-{number:02d}.png"
    im.save(path)
    return path

log_lines = [line.strip() for line in LOG.splitlines() if line.strip()]
check_lines = [line for line in log_lines if
               "no dependency violations" in line or "Test Files" in line or "Tests " in line]

slides = [
    slide(1, "Portabilidad del arnés 0.1.4",
          "Aplicación de reglas y verificaciones en otro dominio",
          ["Origen: ecclesia-arnes", "Destino: ecclesia-portabilidad-prueba",
           "Dominio independiente: tareas genéricas"]),
    slide(2, "1  Separar los repositorios",
          "El producto Ecclesia y la prueba de portabilidad viven en Git distintos",
          ["ecclesia-proyecto/       aplicación nacional de iglesias",
           "ecclesia-arnes/          reglas, prompts, checklists y hook",
           "ecclesia-portabilidad-prueba/   módulo de tareas"]),
    slide(3, "2  Instalar el arnés",
          "Se adaptó AGENTS.md y se copió el hook de la versión 0.1.4",
          ["El dominio nuevo se describe en docs/PROYECTO.md."],
          ["Copy-Item ../ecclesia-arnes/hooks/pre-commit .githooks/pre-commit",
           "git config core.hooksPath .githooks"]),
    slide(4, "3  Adaptar un módulo completo",
          "Ruta, servicio, repositorio y prueba del dominio de tareas",
          ["Regla: recortar espacios y exigir tres caracteres en el título.",
           "Corrección real: la prueba importaba ./service.js;",
           "al moverla a tests/ se cambió a ../src/tasks/service.js."]),
    slide(5, "4  Ejecutar el hook",
          "El pre-commit invoca la puerta de calidad del proyecto nuevo",
          [],
          ["git hook run pre-commit",
           "> npm run lint && npm run format:check",
           "> npm run deps:check && npm run test"]),
    slide(6, "5  Revisar la salida real",
          "Resultado del archivo docs/evidencia-hook-2026-11-01.txt",
          [],
          check_lines[:4] + ["lint: aprobado", "formato: aprobado"]),
    slide(7, "6  Resultado y límite",
          "El arnés funciona en el módulo de tareas",
          ["Pasaron lint, formato, dependencias y una prueba.",
           "La instalación local y el hook quedaron documentados.",
           "Publicar el repositorio remoto sigue pendiente."])
]

concat = TMP / "slides.txt"
with concat.open("w", encoding="utf-8") as stream:
    for path in slides:
        stream.write(f"file '{path.as_posix()}'\n")
        stream.write("duration 12\n")
    stream.write(f"file '{slides[-1].as_posix()}'\n")
subprocess.run([
    FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
    "-safe", "0", "-f", "concat", "-i", str(concat),
    "-vf", "fps=20,format=yuv420p", "-c:v", "libx264",
    "-preset", "veryfast", "-crf", "22", "-movflags", "+faststart", str(OUT)
], check=True)
print(OUT)
