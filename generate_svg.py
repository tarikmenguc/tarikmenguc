import random

width = 800
height = 300

nodes = []
layers = [50, 150, 250, 350, 450, 550, 650, 750]
for x in layers:
    for _ in range(random.randint(6, 10)):
        y = random.randint(20, 280)
        nodes.append({'x': x, 'y': y, 'layer': x})

svg = '''<svg width="800" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .node { fill: #E94560; animation: pulse 2s infinite alternate; }
      .link { stroke: #0F3460; stroke-width: 1.5; opacity: 0.8; animation: dash 5s linear infinite; stroke-dasharray: 4, 4; }
      @keyframes pulse {
        0% { r: 2; opacity: 0.5; }
        100% { r: 5; opacity: 1; filter: drop-shadow(0 0 6px #E94560); }
      }
      @keyframes dash {
        to { stroke-dashoffset: -20; }
      }
      .bg { fill: #050505; }
      .title { fill: #E94560; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 38px; font-weight: bold; text-anchor: middle; filter: drop-shadow(0 0 5px #E94560); }
      .subtitle { fill: #A8B2D1; font-family: 'Courier New', monospace; font-size: 16px; text-anchor: middle; letter-spacing: 4px; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg"/>
'''

for i, x in enumerate(layers[:-1]):
    next_x = layers[i+1]
    curr_nodes = [n for n in nodes if n['layer'] == x]
    next_nodes = [n for n in nodes if n['layer'] == next_x]
    for cn in curr_nodes:
        targets = random.sample(next_nodes, min(len(next_nodes), random.randint(2, 4)))
        for tn in targets:
            svg += f'  <line x1="{cn["x"]}" y1="{cn["y"]}" x2="{tn["x"]}" y2="{tn["y"]}" class="link"/>\n'

for n in nodes:
    delay = random.uniform(0, 2)
    svg += f'  <circle cx="{n["x"]}" cy="{n["y"]}" class="node" style="animation-delay: {delay}s"/>\n'

svg += '''
  <rect x="100" y="100" width="600" height="100" fill="#050505" opacity="0.85" rx="15"/>
  <text x="400" y="145" class="title">Muhammed Tarık Mengüç</text>
  <text x="400" y="175" class="subtitle">AI ENGINEER | NEURAL ARCHITECT</text>
</svg>'''

with open('c:/Users/tarik/Desktop/tarikmenguc-main/neural_network.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
