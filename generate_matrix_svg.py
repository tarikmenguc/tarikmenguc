import random

svg = '''<svg width="100%" height="300" viewBox="0 0 1000 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg { fill: #000000; }
      .matrix-text { fill: #00FF41; font-family: 'Courier New', Courier, monospace; font-size: 18px; font-weight: bold; opacity: 0; filter: drop-shadow(0 0 4px #00FF41); }
      @keyframes fall {
        0% { transform: translateY(-400px); opacity: 0; }
        10% { opacity: 1; }
        80% { opacity: 1; }
        100% { transform: translateY(350px); opacity: 0; }
      }
      .title-box { fill: #000000; opacity: 0.85; }
      .title { fill: #00FF41; font-family: 'Courier New', Courier, monospace; font-size: 42px; font-weight: bold; text-anchor: middle; filter: drop-shadow(0 0 8px #00FF41); }
      .subtitle { fill: #ffffff; font-family: 'Courier New', Courier, monospace; font-size: 18px; text-anchor: middle; letter-spacing: 5px; opacity: 0.9; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="10"/>
  <g>
'''

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
for x in range(10, 1000, 25):
    delay = random.uniform(0, 5)
    duration = random.uniform(4, 8)
    column_text = ''.join([f'<tspan x="{x}" dy="20">{random.choice(chars)}</tspan>' for _ in range(20)])
    svg += f'    <text class="matrix-text" style="animation: fall {duration}s linear {delay}s infinite;">{column_text}</text>\n'

svg += '''  </g>
  <rect x="150" y="100" width="700" height="100" class="title-box" rx="10"/>
  <text x="500" y="145" class="title">Muhammed Tarık Mengüç</text>
  <text x="500" y="175" class="subtitle">AI ENGINEER | WAKE UP NEO...</text>
</svg>'''

with open('c:/Users/tarik/Desktop/tarikmenguc-main/matrix_banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
