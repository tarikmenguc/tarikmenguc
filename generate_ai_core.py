import math
import random

svg = '''<svg width="100%" height="450" viewBox="0 0 1000 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg { fill: #000000; }
      .ring { fill: none; stroke-width: 1.5; transform-origin: 500px 225px; opacity: 0.8; }
      .r1 { animation: spin 12s linear infinite; stroke: #66FCF1; stroke-dasharray: 5 15; }
      .r2 { animation: spin-rev 18s linear infinite; stroke: #A8B2D1; stroke-dasharray: 20 10; }
      .r3 { animation: spin 24s linear infinite; stroke: #E94560; stroke-dasharray: 40 30; }
      .r4 { animation: spin-rev 30s linear infinite; stroke: #0F3460; stroke-width: 3; stroke-dasharray: 100 50; }
      @keyframes spin { 100% { transform: rotate(360deg); } }
      @keyframes spin-rev { 100% { transform: rotate(-360deg); } }
      .core { fill: #E94560; animation: pulse 2s infinite alternate; filter: drop-shadow(0 0 20px #E94560); }
      @keyframes pulse { 0% { r: 15; opacity: 0.7; } 100% { r: 35; opacity: 1; filter: drop-shadow(0 0 35px #E94560); } }
      .data { fill: #66FCF1; font-family: 'Courier New', monospace; font-size: 14px; opacity: 0; animation: flash 6s infinite; }
      @keyframes flash { 0%, 100% { opacity: 0; } 50% { opacity: 0.6; } }
      .hex { fill: none; stroke: #E94560; stroke-width: 1.5; opacity: 0.3; transform-origin: 500px 225px; animation: scaleUp 6s infinite alternate; }
      @keyframes scaleUp { 0% { transform: scale(0.7) rotate(0deg); opacity: 0.1; } 100% { transform: scale(1.3) rotate(30deg); opacity: 0.5; } }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="15"/>
'''

for i in range(1, 22):
    r = 45 + i * 15
    cls = random.choice(['r1', 'r2', 'r3', 'r4'])
    svg += f'  <circle cx="500" cy="225" r="{r}" class="ring {cls}"/>\n'

for i in range(120):
    x = random.randint(20, 980)
    y = random.randint(20, 430)
    delay = random.uniform(0, 6)
    duration = random.uniform(4, 10)
    text = ''.join(random.choices(['0', '1', 'AI', 'NN', 'DL', '##'], k=4))
    svg += f'  <text x="{x}" y="{y}" class="data" style="animation-delay: {delay}s; animation-duration: {duration}s;">{text}</text>\n'

for i in range(4):
    size = 100 + i * 60
    points = []
    for j in range(6):
        angle_deg = 60 * j - 30
        angle_rad = math.pi / 180 * angle_deg
        hx = 500 + size * math.cos(angle_rad)
        hy = 225 + size * math.sin(angle_rad)
        points.append(f"{hx},{hy}")
    pts = " ".join(points)
    svg += f'  <polygon points="{pts}" class="hex" style="animation-delay: {i}s;"/>\n'

svg += '  <circle cx="500" cy="225" class="core"/>\n'
svg += '</svg>'

with open('c:/Users/tarik/Desktop/tarikmenguc-main/ai_core.svg', 'w') as f:
    f.write(svg)
