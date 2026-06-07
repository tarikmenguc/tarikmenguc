import math
import random

svg = '''<svg width="100%" height="150" viewBox="0 0 1000 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .wave {
        fill: none;
        stroke-width: 2.5;
        opacity: 0.8;
      }
      .w1 { stroke: #E94560; animation: flow1 3s linear infinite; stroke-dasharray: 20 10; filter: drop-shadow(0 0 4px #E94560); }
      .w2 { stroke: #0F3460; stroke-width: 4; animation: flow2 4s linear infinite; stroke-dasharray: 50 20; }
      .w3 { stroke: #66FCF1; stroke-width: 1.5; opacity: 0.5; animation: flow3 5s linear infinite; stroke-dasharray: 10 15; filter: drop-shadow(0 0 3px #66FCF1); }
      @keyframes flow1 { to { stroke-dashoffset: -60; } }
      @keyframes flow2 { to { stroke-dashoffset: -140; } }
      @keyframes flow3 { to { stroke-dashoffset: -50; } }
      .bg { fill: #050505; }
    </style>
  </defs>
  <rect width="100%" height="100%" class="bg" rx="10"/>
'''

def get_wave_path(amplitude, frequency, phase, points=100):
    path = "M -50 75 "
    for i in range(1, points + 1):
        x = (i / points) * 1100 - 50
        y = 75 + math.sin(x * frequency + phase) * amplitude
        path += f"L {x:.1f} {y:.1f} "
    return path

svg += f'  <path d="{get_wave_path(40, 0.008, 0)}" class="wave w1"/>\n'
svg += f'  <path d="{get_wave_path(60, 0.005, 2)}" class="wave w2"/>\n'
svg += f'  <path d="{get_wave_path(25, 0.012, 4)}" class="wave w3"/>\n'

# Adding floating data particles
for _ in range(40):
    x = random.randint(0, 1000)
    y = random.randint(50, 150)
    r = random.uniform(1, 2.5)
    duration = random.uniform(4, 9)
    delay = random.uniform(0, 5)
    color = random.choice(["#E94560", "#66FCF1", "#A8B2D1"])
    svg += f'''
  <circle cx="{x}" cy="{y}" r="{r}" fill="{color}">
    <animate attributeName="cy" from="{y}" to="-20" dur="{duration}s" begin="{delay}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;0.9;0" dur="{duration}s" begin="{delay}s" repeatCount="indefinite"/>
  </circle>'''

svg += '</svg>'

with open('c:/Users/tarik/Desktop/tarikmenguc-main/data_flow.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
