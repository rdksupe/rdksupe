<div align="center">

<!-- ☁️☁️☁️  RAINFALL + MEOWING CAT  ☁️☁️☁️ -->

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 160" width="600" style="background:#222129; border-radius: 8px;">

  <!-- rain drops -->
  <style>
    @keyframes fall {
      0%   { transform: translateY(-20px); opacity: 0; }
      10%  { opacity: 0.7; }
      90%  { opacity: 0.7; }
      100% { transform: translateY(150px); opacity: 0; }
    }
    .rain { animation: fall linear infinite; fill: #6a9ec7; }
    .rain1 { animation-duration: 1.2s; animation-delay: 0.0s; }
    .rain2 { animation-duration: 1.5s; animation-delay: 0.3s; }
    .rain3 { animation-duration: 1.0s; animation-delay: 0.6s; }
    .rain4 { animation-duration: 1.8s; animation-delay: 0.1s; }
    .rain5 { animation-duration: 1.3s; animation-delay: 0.8s; }
    @keyframes meow {
      0%, 100% { opacity: 0.7; }
      50%      { opacity: 1; }
    }
    .speech { animation: meow 2s ease-in-out infinite; }
    @keyframes tail {
      0%, 100% { transform: rotate(0deg); }
      50%      { transform: rotate(8deg); }
    }
    .tail { animation: tail 1.5s ease-in-out infinite; transform-origin: 320px 108px; }
  </style>

  <!-- background glow -->
  <rect x="0" y="0" width="600" height="160" rx="8" fill="#222129"/>

  <!-- clouds -->
  <ellipse cx="80"  cy="28" rx="60" ry="18" fill="#3a3945" opacity="0.6"/>
  <ellipse cx="110" cy="24" rx="40" ry="14" fill="#3a3945" opacity="0.6"/>
  <ellipse cx="520" cy="30" rx="55" ry="16" fill="#3a3945" opacity="0.6"/>
  <ellipse cx="490" cy="26" rx="38" ry="12" fill="#3a3945" opacity="0.6"/>

  <!-- rain drops (columns) -->
  <!-- col 1 -->
  <line class="rain rain1" x1="40"  y1="50" x2="38" y2="62" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain2" x1="70"  y1="55" x2="68" y2="67" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain3" x1="100" y1="48" x2="98" y2="60" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 2 -->
  <line class="rain rain4" x1="140" y1="52" x2="138" y2="64" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain5" x1="170" y1="60" x2="168" y2="72" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 3 -->
  <line class="rain rain1" x1="200" y1="45" x2="198" y2="57" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain3" x1="230" y1="58" x2="228" y2="70" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 4 -->
  <line class="rain rain2" x1="270" y1="50" x2="268" y2="62" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain5" x1="300" y1="55" x2="298" y2="67" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 5 -->
  <line class="rain rain4" x1="340" y1="48" x2="338" y2="60" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain1" x1="370" y1="62" x2="368" y2="74" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 6 -->
  <line class="rain rain3" x1="410" y1="52" x2="408" y2="64" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain2" x1="440" y1="58" x2="438" y2="70" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 7 -->
  <line class="rain rain5" x1="480" y1="46" x2="478" y2="58" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain4" x1="510" y1="60" x2="508" y2="72" stroke-width="1.5" stroke-linecap="round"/>
  <!-- col 8 -->
  <line class="rain rain1" x1="550" y1="50" x2="548" y2="62" stroke-width="1.5" stroke-linecap="round"/>
  <line class="rain rain3" x1="580" y1="54" x2="578" y2="66" stroke-width="1.5" stroke-linecap="round"/>

  <!-- puddle at bottom -->
  <ellipse cx="300" cy="148" rx="180" ry="8" fill="#6a9ec7" opacity="0.12"/>

  <!-- ====== CAT ====== -->
  <!-- body -->
  <ellipse cx="300" cy="108" rx="42" ry="30" fill="#FFA86A"/>
  <!-- head -->
  <circle cx="300" cy="72" r="28" fill="#FFA86A"/>
  <!-- ears -->
  <polygon points="280,52 275,28 293,48" fill="#FFA86A"/>
  <polygon points="320,52 325,28 307,48" fill="#FFA86A"/>
  <polygon points="282,50 278,34 291,48" fill="#bc8d6b"/>
  <polygon points="318,50 322,34 309,48" fill="#bc8d6b"/>
  <!-- eyes -->
  <ellipse cx="290" cy="70" rx="5" ry="6" fill="#222129"/>
  <ellipse cx="310" cy="70" rx="5" ry="6" fill="#222129"/>
  <!-- eye shine -->
  <circle cx="292" cy="68" r="1.8" fill="#fff"/>
  <circle cx="312" cy="68" r="1.8" fill="#fff"/>
  <!-- nose -->
  <ellipse cx="300" cy="78" rx="3" ry="2.2" fill="#bc8d6b"/>
  <!-- mouth (meowing - open) -->
  <ellipse cx="300" cy="85" rx="5" ry="4" fill="#222129"/>
  <ellipse cx="300" cy="86" rx="3.5" ry="2" fill="#bc8d6b"/>
  <!-- whiskers -->
  <line x1="278" y1="76" x2="260" y2="72" stroke="#bc8d6b" stroke-width="1"/>
  <line x1="278" y1="80" x2="260" y2="84" stroke="#bc8d6b" stroke-width="1"/>
  <line x1="322" y1="76" x2="340" y2="72" stroke="#bc8d6b" stroke-width="1"/>
  <line x1="322" y1="80" x2="340" y2="84" stroke="#bc8d6b" stroke-width="1"/>
  <!-- tail -->
  <g class="tail">
    <path d="M342 108 Q370 90 365 60 Q363 52 358 56" fill="none" stroke="#FFA86A" stroke-width="5" stroke-linecap="round"/>
  </g>
  <!-- front paws -->
  <ellipse cx="282" cy="132" rx="10" ry="6" fill="#FFA86A"/>
  <ellipse cx="318" cy="132" rx="10" ry="6" fill="#FFA86A"/>
  <!-- back paws -->
  <ellipse cx="268" cy="134" rx="9" ry="5" fill="#FFA86A"/>
  <ellipse cx="332" cy="134" rx="9" ry="5" fill="#FFA86A"/>

  <!-- speech bubble -->
  <g class="speech">
    <rect x="358" y="38" width="90" height="36" rx="12" fill="#222129" stroke="#FFA86A" stroke-width="1.5"/>
    <polygon points="360,68 370,68 355,80" fill="#222129" stroke="#FFA86A" stroke-width="1"/>
    <text x="403" y="61" text-anchor="middle" fill="#FFA86A" font-family="monospace" font-size="16" font-weight="bold">meow~!</text>
  </g>
</svg>

<br>

<sub style="color: #bc8d6b;">☂️ raining on my profile since forever 💧</sub>

</div>

---

## Hi there 👋

🌐 [rdksupe.bearblog.dev](https://rdksupe.bearblog.dev) — Rdk's Super Weird Musings

<!--
**rdksupe/rdksupe** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I'm currently working on ...
- 🌱 I'm currently learning ...
- 👯 I'm looking to collaborate on ...
- 🤔 I'm looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
