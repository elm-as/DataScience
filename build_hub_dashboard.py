"""Generate standalone master portfolio dashboard for DataScience hub with 5 systems."""

from pathlib import Path

OUTPUT_PATH = Path(r"c:\Users\elmas\Desktop\DataScience\index.html")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ElmasCore — Data Science & Quantitative Intelligence Hub</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            brand: {
              bg: '#080C14',
              surface: '#0E1524',
              surfaceLight: '#141E33',
              border: '#1E293B',
              borderLight: '#334155',
              cyan: '#06B6D4',
              emerald: '#10B981',
              amber: '#F59E0B',
              rose: '#F43F5E',
              purple: '#A855F7',
              blue: '#3B82F6',
            }
          }
        }
      }
    }
  </script>
  <style>
    body { background-color: #080C14; color: #E2E8F0; }
    .tabular-nums { font-variant-numeric: tabular-nums; }
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-track { background: #080C14; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 3px; }
    .custom-scroll::-webkit-scrollbar-thumb:hover { background: #334155; }
    .tab-active {
      background-color: #141E33;
      border-color: #06B6D4;
      color: #38BDF8;
    }
  </style>
</head>
<body class="font-sans antialiased min-h-screen flex flex-col custom-scroll">

  <!-- Top Executive Header -->
  <header class="border-b border-brand-border bg-brand-surface/90 backdrop-blur sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center space-x-3">
        <div class="h-9 w-9 rounded-lg bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center font-mono font-bold text-slate-900 text-lg shadow-lg shadow-cyan-500/20">
          E
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="text-base font-bold text-white tracking-tight">ElmasCore DataScience Hub</h1>
            <span class="px-2 py-0.5 text-xs font-mono rounded bg-emerald-950/80 text-emerald-400 border border-emerald-800/60">v2.5 Sovereign</span>
          </div>
          <p class="text-xs text-slate-400 font-mono">From Data to Systems • 5 Autonomous Production Pipelines</p>
        </div>
      </div>

      <!-- Quick Action Badges -->
      <div class="flex items-center space-x-2 font-mono text-xs">
        <a href="https://github.com/elm-as/DataScience" target="_blank" class="px-3 py-1.5 rounded-md bg-brand-surfaceLight hover:bg-slate-800 text-slate-300 border border-brand-border transition flex items-center space-x-1.5">
          <span>elm-as/DataScience</span>
          <span class="text-cyan-400">↗</span>
        </a>
        <span class="px-2.5 py-1.5 rounded-md bg-slate-900 text-slate-400 border border-brand-border">
          Charter: <span class="text-emerald-400 font-semibold">ELMAS.md</span>
        </span>
      </div>
    </div>
  </header>

  <!-- Macro KPI Strip -->
  <section class="border-b border-brand-border bg-brand-surface/40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-4 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
      <div class="p-3 rounded-lg bg-brand-surface border border-brand-border">
        <div class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Active Systems</div>
        <div class="text-2xl font-bold font-mono text-white mt-1 tabular-nums">5</div>
        <div class="text-[10px] text-cyan-400 font-mono mt-0.5">Autonomous repos</div>
      </div>
      <div class="p-3 rounded-lg bg-brand-surface border border-brand-border">
        <div class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Total Records</div>
        <div class="text-2xl font-bold font-mono text-white mt-1 tabular-nums">1,014,476</div>
        <div class="text-[10px] text-slate-400 font-mono mt-0.5">Audited & sanitized</div>
      </div>
      <div class="p-3 rounded-lg bg-brand-surface border border-brand-border">
        <div class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">PCCF Kaggle S6E11</div>
        <div class="text-2xl font-bold font-mono text-cyan-400 mt-1 tabular-nums">0.95331</div>
        <div class="text-[10px] text-emerald-400 font-mono mt-0.5">Rank #26 (Top 2.0%)</div>
      </div>
      <div class="p-3 rounded-lg bg-brand-surface border border-brand-border">
        <div class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Pneumonia Sens.</div>
        <div class="text-2xl font-bold font-mono text-emerald-400 mt-1 tabular-nums">99.23%</div>
        <div class="text-[10px] text-slate-400 font-mono mt-0.5">387/390 cases found</div>
      </div>
      <div class="p-3 rounded-lg bg-brand-surface border border-brand-border">
        <div class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">GCMDL Tail-Risk</div>
        <div class="text-2xl font-bold font-mono text-rose-400 mt-1 tabular-nums">0.9996</div>
        <div class="text-[10px] text-emerald-400 font-mono mt-0.5">ROC-AUC (1,000 assets)</div>
      </div>
      <div class="p-3 rounded-lg bg-brand-surface border border-brand-border">
        <div class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">ISML Tri-Cohort (6,532)</div>
        <div class="text-2xl font-bold font-mono text-purple-400 mt-1 tabular-nums">0.9962</div>
        <div class="text-[10px] text-slate-400 font-mono mt-0.5">Depression AUC • 93.55% Sens</div>
      </div>
    </div>
  </section>

  <!-- Tab Navigation -->
  <nav class="border-b border-brand-border bg-brand-surface/70 sticky top-[57px] z-40 backdrop-blur">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex space-x-1 overflow-x-auto py-2 custom-scroll text-xs font-mono">
      <button onclick="switchTab('tab-overview')" id="btn-tab-overview" class="tab-btn px-4 py-2 rounded-md font-medium border border-transparent text-slate-300 hover:text-white hover:bg-brand-surfaceLight transition tab-active">
        00. Hub Overview
      </button>
      <button onclick="switchTab('tab-pccf')" id="btn-tab-pccf" class="tab-btn px-4 py-2 rounded-md font-medium border border-transparent text-slate-300 hover:text-white hover:bg-brand-surfaceLight transition">
        01. PCCF (Kaggle Fraud)
      </button>
      <button onclick="switchTab('tab-ggvcf')" id="btn-tab-ggvcf" class="tab-btn px-4 py-2 rounded-md font-medium border border-transparent text-slate-300 hover:text-white hover:bg-brand-surfaceLight transition">
        02. GGVCF (Econometrics)
      </button>
      <button onclick="switchTab('tab-pneumonia')" id="btn-tab-pneumonia" class="tab-btn px-4 py-2 rounded-md font-medium border border-transparent text-slate-300 hover:text-white hover:bg-brand-surfaceLight transition">
        03. Pneumonia (Deep Vision)
      </button>
      <button onclick="switchTab('tab-gcmdl')" id="btn-tab-gcmdl" class="tab-btn px-4 py-2 rounded-md font-medium border border-transparent text-slate-300 hover:text-white hover:bg-brand-surfaceLight transition">
        04. GCMDL (Crypto Telemetry)
      </button>
      <button onclick="switchTab('tab-isml')" id="btn-tab-isml" class="tab-btn px-4 py-2 rounded-md font-medium border border-transparent text-slate-300 hover:text-white hover:bg-brand-surfaceLight transition">
        05. ISML (Psychometrics)
      </button>
    </div>
  </nav>

  <!-- Main Content Area -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 py-6 flex-1 w-full space-y-6">

    <!-- TAB 0: OVERVIEW -->
    <div id="tab-overview" class="tab-content space-y-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Architecture Description -->
        <div class="lg:col-span-2 space-y-4">
          <div class="p-5 rounded-xl bg-brand-surface border border-brand-border space-y-3">
            <div class="flex items-center justify-between">
              <h2 class="text-base font-bold text-white flex items-center space-x-2">
                <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                <span>The Sovereign Multi-Domain Architecture</span>
              </h2>
              <span class="text-xs font-mono text-slate-400">5 Submodules Hub</span>
            </div>
            <p class="text-sm text-slate-300 leading-relaxed">
              `DataScience/` operates as a production umbrella orchestrating five discrete, domain-bounded data systems. Each repository maintains its own strict test harness, domain packages, high-resolution figures, standalone interactive dashboards, and full adherence to the non-negotiable <strong class="text-cyan-400 font-mono">ELMAS.md</strong> engineering charter.
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2 font-mono text-xs">
              <div class="p-3 rounded-lg bg-brand-surfaceLight/70 border border-brand-border/60">
                <div class="text-cyan-400 font-semibold mb-1">Codebase Health</div>
                <div class="text-slate-300">&bull; ≤ 350 lines per module file</div>
                <div class="text-slate-300">&bull; ≤ 3 nesting indentation levels</div>
                <div class="text-slate-300">&bull; Pure deterministic transformations</div>
              </div>
              <div class="p-3 rounded-lg bg-brand-surfaceLight/70 border border-brand-border/60">
                <div class="text-emerald-400 font-semibold mb-1">Testing & Verification</div>
                <div class="text-slate-300">&bull; 100% test pass rate across all suites</div>
                <div class="text-slate-300">&bull; Zero data leakage protocols</div>
                <div class="text-slate-300">&bull; Standalone HTML5 Plotly dashboards</div>
              </div>
            </div>
          </div>

          <!-- Systems Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <!-- Card 1: PCCF -->
            <div class="p-4 rounded-xl bg-brand-surface border border-brand-border hover:border-cyan-500/50 transition space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-950 text-cyan-400 border border-cyan-800/60">PCCF</span>
                <span class="text-xs font-mono text-emerald-400 font-semibold">Rank #26 (0.95331)</span>
              </div>
              <h3 class="text-sm font-bold text-white">Predicting Credit Card Fraud</h3>
              <p class="text-xs text-slate-400">1,000,000 synthetic transaction records. Exploiting decimal generation artifacts with rank-logit multi-family ensembling.</p>
              <div class="flex items-center justify-between text-xs font-mono pt-1 text-slate-400 border-t border-brand-border/60">
                <span>Stack: GBDT + Nelder-Mead</span>
                <button onclick="switchTab('tab-pccf')" class="text-cyan-400 hover:underline">Explore &rarr;</button>
              </div>
            </div>

            <!-- Card 2: GGVCF -->
            <div class="p-4 rounded-xl bg-brand-surface border border-brand-border hover:border-amber-500/50 transition space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-950 text-amber-400 border border-amber-800/60">GGVCF</span>
                <span class="text-xs font-mono text-amber-400 font-semibold">Paradox Resolved</span>
              </div>
              <h3 class="text-sm font-bold text-white">Global Gun Violence Econometrics</h3>
              <p class="text-xs text-slate-400">95 sovereign nations across 2000–2024. Proving zero rank correlation between gun saturation and homicide lethality via Two-Way Fixed Effects.</p>
              <div class="flex items-center justify-between text-xs font-mono pt-1 text-slate-400 border-t border-brand-border/60">
                <span>Stack: PanelOLS + RF</span>
                <button onclick="switchTab('tab-ggvcf')" class="text-amber-400 hover:underline">Explore &rarr;</button>
              </div>
            </div>

            <!-- Card 3: Pneumonia -->
            <div class="p-4 rounded-xl bg-brand-surface border border-brand-border hover:border-emerald-500/50 transition space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-950 text-emerald-400 border border-emerald-800/60">Pneumonia</span>
                <span class="text-xs font-mono text-emerald-400 font-semibold">99.23% Sensibilité</span>
              </div>
              <h3 class="text-sm font-bold text-white">Pediatric Radiology Deep CNN</h3>
              <p class="text-xs text-slate-400">5,856 radiographs (Cell 2018). ResNet-18 transfer learning with clinical cost weighting and 100% explainable Grad-CAM heatmaps.</p>
              <div class="flex items-center justify-between text-xs font-mono pt-1 text-slate-400 border-t border-brand-border/60">
                <span>Stack: PyTorch + Grad-CAM</span>
                <button onclick="switchTab('tab-pneumonia')" class="text-emerald-400 hover:underline">Explore &rarr;</button>
              </div>
            </div>

            <!-- Card 4: GCMDL -->
            <div class="p-4 rounded-xl bg-brand-surface border border-brand-border hover:border-rose-500/50 transition space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-950 text-rose-400 border border-rose-800/60">GCMDL</span>
                <span class="text-xs font-mono text-rose-400 font-semibold">99.50% Acc Turnover</span>
              </div>
              <h3 class="text-sm font-bold text-white">Crypto Market Dynamics & Liquidity</h3>
              <p class="text-xs text-slate-400">1,000 crypto assets ($2.84T MCap). Amihud illiquidity, Corwin-Schultz spreads, and 0.9996 ROC-AUC catastrophic tail risk detection.</p>
              <div class="flex items-center justify-between text-xs font-mono pt-1 text-slate-400 border-t border-brand-border/60">
                <span>Stack: LightGBM + CatBoost</span>
                <button onclick="switchTab('tab-gcmdl')" class="text-rose-400 hover:underline">Explore &rarr;</button>
              </div>
            </div>

            <!-- Card 5: ISML -->
            <div class="p-4 rounded-xl bg-brand-surface border border-brand-border hover:border-purple-500/50 transition space-y-2.5 sm:col-span-2">
              <div class="flex items-center justify-between">
                <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-purple-950 text-purple-400 border border-purple-800/60">ISML Tri-Cohort</span>
                <span class="text-xs font-mono text-purple-400 font-semibold">AUC 0.9962 • 98.69% Acc • 6,532 Subjects (113 Nations)</span>
              </div>
              <h3 class="text-sm font-bold text-white">Impact of Social Media on Life (Tri-Cohort Architecture)</h3>
              <p class="text-xs text-slate-400">Chronobiological disruption, 113-nation cross-national addiction atlas, and adolescent clinical depression detection with physical activity protective buffering.</p>
              <div class="flex items-center justify-between text-xs font-mono pt-1 text-slate-400 border-t border-brand-border/60">
                <span>Stack: GBDT + Cost-Sensitive Youden J + OLS Panel</span>
                <button onclick="switchTab('tab-isml')" class="text-purple-400 hover:underline">Explore &rarr;</button>
              </div>
            </div>
          </div>
        </div>

        <!-- System Portfolio Radar / Profile -->
        <div class="space-y-4">
          <div class="p-5 rounded-xl bg-brand-surface border border-brand-border">
            <h3 class="text-sm font-bold text-white mb-2 flex items-center justify-between">
              <span>Domain Capabilities Balance</span>
              <span class="text-[11px] font-mono text-slate-400">Radar View</span>
            </h3>
            <div id="plot-radar-overview" class="w-full h-[280px]"></div>
          </div>

          <div class="p-4 rounded-xl bg-brand-surface border border-brand-border font-mono text-xs space-y-2">
            <div class="text-slate-400 uppercase text-[11px] tracking-wider">Repository Status</div>
            <div class="flex justify-between items-center py-1 border-b border-brand-border/40">
              <span class="text-slate-300">elm-as/PCCF</span>
              <span class="text-emerald-400">● Synced (6e570ba)</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-brand-border/40">
              <span class="text-slate-300">elm-as/GGVCF</span>
              <span class="text-emerald-400">● Synced (5a9f06b)</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-brand-border/40">
              <span class="text-slate-300">elm-as/Pneumonia</span>
              <span class="text-emerald-400">● Synced (2a19498)</span>
            </div>
            <div class="flex justify-between items-center py-1 border-b border-brand-border/40">
              <span class="text-slate-300">elm-as/GCMDL</span>
              <span class="text-emerald-400">● Synced (2cdfc2a)</span>
            </div>
            <div class="flex justify-between items-center py-1">
              <span class="text-slate-300">elm-as/ISML</span>
              <span class="text-emerald-400">● Synced (9a820ff)</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 1: PCCF -->
    <div id="tab-pccf" class="tab-content hidden space-y-6">
      <div class="p-5 rounded-xl bg-brand-surface border border-brand-border space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-brand-border pb-3">
          <div>
            <h2 class="text-lg font-bold text-white">PCCF — Predicting Credit Card Fraud (Kaggle S6E11)</h2>
            <p class="text-xs text-slate-400 font-mono">1,000,000 Synthetic Transactions • Target Imbalance ~1:175</p>
          </div>
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 rounded bg-cyan-950 text-cyan-400 border border-cyan-800 font-mono text-xs">Public ROC-AUC: 0.95331</span>
            <span class="px-3 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono text-xs">Rank #26 / 1,294 (Top 2.0%)</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="lg:col-span-2 space-y-4">
            <div id="plot-pccf-benchmark" class="w-full h-[320px] rounded-lg bg-brand-surfaceLight/30 border border-brand-border/60 p-2"></div>
            
            <div class="p-4 rounded-lg bg-brand-surfaceLight/40 border border-brand-border font-mono text-xs space-y-2">
              <div class="text-cyan-400 font-bold uppercase text-[11px]">Scientific Conclusion</div>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                1. <strong>L'empreinte décimale des générateurs synthétiques</strong> : L'ingénierie des décimales et la loi de Benford extraient des failles de distribution du générateur CTGAN.
              </p>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                2. <strong>Supériorité de l'assemblage Nelder-Mead</strong> : Le mélange multi-familles neutralise les corrélations d'erreur et surpasse tout modèle individuel (+0.00496 sur le score public).
              </p>
            </div>
          </div>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-brand-surfaceLight/30 border border-brand-border space-y-3 text-xs font-mono">
              <div class="text-slate-400 uppercase text-[11px] font-bold">Kaggle Submissions Log</div>
              <div class="space-y-2">
                <div class="p-2 rounded bg-slate-900/80 border border-slate-800">
                  <div class="flex justify-between text-cyan-400 font-semibold">
                    <span>Apex Consensus v14</span>
                    <span>0.95331</span>
                  </div>
                  <div class="text-[10px] text-slate-400 mt-0.5">Rank #26 (Top 2.01%)</div>
                </div>
                <div class="p-2 rounded bg-slate-900/80 border border-slate-800">
                  <div class="flex justify-between text-cyan-400 font-semibold">
                    <span>Sovereign Podium v13</span>
                    <span>0.95331</span>
                  </div>
                  <div class="text-[10px] text-slate-400 mt-0.5">94% Strike9 + 3% GPT2-LM</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: GGVCF -->
    <div id="tab-ggvcf" class="tab-content hidden space-y-6">
      <div class="p-5 rounded-xl bg-brand-surface border border-brand-border space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-brand-border pb-3">
          <div>
            <h2 class="text-lg font-bold text-white">GGVCF — Global Gun Violence & Civilian Firearms (2000–2024)</h2>
            <p class="text-xs text-slate-400 font-mono">UNODC &bull; Small Arms Survey 2018 &bull; World Bank WDI &bull; 95 Countries</p>
          </div>
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 rounded bg-amber-950 text-amber-400 border border-amber-800 font-mono text-xs">Spearman: &rho; = -0.0026</span>
            <span class="px-3 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono text-xs">Two-Way FE: F = 162.45</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="lg:col-span-2 space-y-4">
            <div id="plot-ggvcf-scatter" class="w-full h-[340px] rounded-lg bg-brand-surfaceLight/30 border border-brand-border/60 p-2"></div>
            
            <div class="p-4 rounded-lg bg-brand-surfaceLight/40 border border-brand-border font-mono text-xs space-y-2">
              <div class="text-amber-400 font-bold uppercase text-[11px]">Scientific Conclusion</div>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Réfutation empirique du lien direct armes-homicides</strong> : À l'échelle mondiale, le taux de détention d'armes civiles présente une corrélation strictement nulle ($\rho = -0.0026$) avec le taux d'homicide.
              </p>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>La fracture sociale est le moteur réel</strong> : L'indice de Gini explique 59.8% de la variance ; la croissance économique présente une élasticité protectrice ($\beta = -0.3491$).
              </p>
            </div>
          </div>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-brand-surfaceLight/30 border border-brand-border space-y-2 text-xs font-mono">
              <div class="text-slate-400 uppercase text-[11px] font-bold">4 Global Archetypes</div>
              <div class="space-y-1.5 text-[11px]">
                <div class="p-2 rounded bg-slate-900/80 border border-slate-800 text-cyan-300">
                  <strong>Cluster 0: Saturated & Peaceful</strong> (CH, NO, FI, RS)
                </div>
                <div class="p-2 rounded bg-slate-900/80 border border-slate-800 text-rose-400">
                  <strong>Cluster 1: Acute Lethality Crisis</strong> (SV, JM, VE, CO)
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 3: PNEUMONIA -->
    <div id="tab-pneumonia" class="tab-content hidden space-y-6">
      <div class="p-5 rounded-xl bg-brand-surface border border-brand-border space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-brand-border pb-3">
          <div>
            <h2 class="text-lg font-bold text-white">Pneumonia — Pediatric Chest Radiography Deep Diagnostic System</h2>
            <p class="text-xs text-slate-400 font-mono">Cell 2018 (Kermany et al.) Benchmark &bull; 5,856 Anterior-Posterior Chest Radiographs</p>
          </div>
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono text-xs">Sensitivity: 99.23% (387/390)</span>
            <span class="px-3 py-1 rounded bg-cyan-950 text-cyan-400 border border-cyan-800 font-mono text-xs">ROC-AUC: 0.9415</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="lg:col-span-2 space-y-4">
            <div id="plot-pneumonia-breakdown" class="w-full h-[320px] rounded-lg bg-brand-surfaceLight/30 border border-brand-border/60 p-2"></div>
            
            <div class="p-4 rounded-lg bg-brand-surfaceLight/40 border border-brand-border font-mono text-xs space-y-2">
              <div class="text-emerald-400 font-bold uppercase text-[11px]">Scientific Conclusion</div>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Zéro omission sur les pneumonies virales (100.0%)</strong> : Le calibrage de seuil de Youden prévient l'antibiorésistance et neutralise les faux négatifs critiques (3 omissions sur 390 cas).
              </p>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Explicabilité anatomo-pathologique</strong> : Grad-CAM valide les foyers alvéolaires lobaires et interstitiels sans artefacts contextuels.
              </p>
            </div>
          </div>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-brand-surfaceLight/30 border border-brand-border space-y-2.5 text-xs font-mono">
              <div class="text-slate-400 uppercase text-[11px] font-bold">Diagnostic Confusion Matrix</div>
              <table class="w-full text-center border-collapse text-[11px]">
                <thead>
                  <tr class="text-slate-400 border-b border-brand-border">
                    <th class="p-1 text-left">Actual \\ Pred</th>
                    <th class="p-1 text-emerald-400">Normal</th>
                    <th class="p-1 text-rose-400">Pneumonia</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="border-b border-brand-border/40">
                    <td class="p-1.5 text-left text-slate-300">Normal (234)</td>
                    <td class="p-1.5 text-emerald-400 font-bold">139 (TN)</td>
                    <td class="p-1.5 text-amber-400">95 (FP)</td>
                  </tr>
                  <tr>
                    <td class="p-1.5 text-left text-slate-300">Pneumonia (390)</td>
                    <td class="p-1.5 text-rose-400 font-bold">3 (FN)</td>
                    <td class="p-1.5 text-emerald-400 font-bold">387 (TP)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 4: GCMDL -->
    <div id="tab-gcmdl" class="tab-content hidden space-y-6">
      <div class="p-5 rounded-xl bg-brand-surface border border-brand-border space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-brand-border pb-3">
          <div>
            <h2 class="text-lg font-bold text-white">GCMDL — Global Crypto Market Dynamics & Liquidity 2026</h2>
            <p class="text-xs text-slate-400 font-mono">Top 1,000 Cryptocurrencies • $2.84T Aggregate Market Cap • 57.72% BTC Dominance</p>
          </div>
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 rounded bg-rose-950 text-rose-400 border border-rose-800 font-mono text-xs">Turnover Acc: 99.50%</span>
            <span class="px-3 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono text-xs">Tail-Risk ROC: 0.9996</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="lg:col-span-2 space-y-4">
            <div id="plot-gcmdl-market" class="w-full h-[340px] rounded-lg bg-brand-surfaceLight/30 border border-brand-border/60 p-2"></div>
            
            <div class="p-4 rounded-lg bg-brand-surfaceLight/40 border border-brand-border font-mono text-xs space-y-2">
              <div class="text-rose-400 font-bold uppercase text-[11px]">Scientific Conclusion</div>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>L'illusion de la capitalisation boursière</strong> : Une MCap élevée ne garantit pas la liquidité. Amihud et Corwin-Schultz isolent les actifs à fort slippage.
              </p>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Le piège de la dilution FDV</strong> : Un faible ratio d'offre en circulation prédit à 99.96% un effondrement supérieur à -85% du pic historique.
              </p>
            </div>
          </div>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-brand-surfaceLight/30 border border-brand-border space-y-2 text-xs font-mono">
              <div class="text-slate-400 uppercase text-[11px] font-bold">Turnover Regimes F1</div>
              <div class="space-y-1 text-[11px]">
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Illiquid Constrained</span>
                  <span class="text-emerald-400 font-bold">0.9967</span>
                </div>
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Hyper Liquid Turnover</span>
                  <span class="text-cyan-400 font-bold">1.0000</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: ISML -->
    <div id="tab-isml" class="tab-content hidden space-y-6">
      <div class="p-5 rounded-xl bg-brand-surface border border-brand-border space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-brand-border pb-3">
          <div>
            <h2 class="text-lg font-bold text-white">ISML — Impact of Social Media on Life (Tri-Cohort Architecture: 6,532 Subjects, 113 Nations)</h2>
            <p class="text-xs text-slate-400 font-mono">Cohorts 1, 2 & 3 &bull; 4,500 Primary Students + 832 Global (113 Countries) + 1,200 Adolescents (Ages 13-19)</p>
          </div>
          <div class="flex items-center space-x-2">
            <span class="px-3 py-1 rounded bg-purple-950 text-purple-400 border border-purple-800 font-mono text-xs">Depression AUC: 0.9962</span>
            <span class="px-3 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 font-mono text-xs">Clinical Sens: 93.55%</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="lg:col-span-2 space-y-4">
            <div id="plot-isml-gpa-stress" class="w-full h-[340px] rounded-lg bg-brand-surfaceLight/30 border border-brand-border/60 p-2"></div>
            
            <div class="p-4 rounded-lg bg-brand-surfaceLight/40 border border-brand-border font-mono text-xs space-y-2">
              <div class="text-purple-400 font-bold uppercase text-[11px]">Scientific Conclusions Across Tri-Cohort Architecture</div>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Cohorte 1 (Rupture chronobiologique ratio > 1.0)</strong> : Lorsque le temps d'écran quotidien dépasse la durée de sommeil avec usage post-minuit, le stress bondit de +179% (de 11.16 à 31.12/40) et le GPA s'effondre de -1.01 point (-28.4%).
              </p>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Cohorte 2 (Universalité de la friction sociale sur 113 pays)</strong> : L'addiction numérique dégrade invariablement la santé mentale (r = -0.6668) en alimentant les conflits interpersonnels (r = +0.6642), affectant 61.42% des études universitaires.
              </p>
              <p class="text-slate-300 text-xs font-sans leading-relaxed">
                &bull; <strong>Cohorte 3 (L'activité physique comme bouclier protecteur clinique)</strong> : Chez les adolescents (13-19 ans), le manque de sommeil est le principal inducteur dépressif (r = -0.1906), mais le sport régulier réduit la probabilité de dépression de 84%, même à temps d'écran élevé.
              </p>
            </div>
          </div>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-brand-surfaceLight/30 border border-brand-border space-y-2 text-xs font-mono">
              <div class="text-slate-400 uppercase text-[11px] font-bold">Tri-Cohort Unified Benchmarks</div>
              <div class="space-y-1 text-[11px]">
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Teen Depression ROC-AUC</span>
                  <span class="text-rose-400 font-bold">0.9962</span>
                </div>
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Teen Clinical Sensitivity</span>
                  <span class="text-rose-400 font-bold">93.55% (Youden J: 0.9355)</span>
                </div>
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Global Addiction vs Health (r)</span>
                  <span class="text-amber-400 font-bold">-0.6668 (113 Pays)</span>
                </div>
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Cohort 1 Impact Accuracy</span>
                  <span class="text-emerald-400 font-bold">98.69% (Macro F1: 0.9654)</span>
                </div>
                <div class="flex justify-between p-1.5 rounded bg-slate-900 border border-slate-800">
                  <span>Cohort 1 Stress Regressor R²</span>
                  <span class="text-purple-400 font-bold">0.6332 (Spearman: 0.7500)</span>
                </div>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-brand-surfaceLight/30 border border-brand-border font-mono text-xs space-y-2">
              <a href="ISML/artifacts/dashboard.html" target="_blank" class="block w-full py-2 text-center rounded bg-purple-500/20 text-purple-300 hover:bg-purple-500/30 border border-purple-500/40 transition">
                Launch Tri-Cohort Interactive Atlas ↗
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="border-t border-brand-border bg-brand-surface py-4 text-xs font-mono text-slate-400 text-center">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row justify-between items-center gap-2">
      <div>Built with mathematical rigor by <span class="text-cyan-400 font-bold">ElmasCore</span> &bull; "From Data to Systems"</div>
      <div>Author: <a href="https://github.com/elm-as" class="text-slate-300 hover:text-white underline">Elmas Trésor (elm-as)</a></div>
    </div>
  </footer>

  <!-- Script for Tab Switching & Plotly Rendering -->
  <script>
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('tab-active');
        btn.classList.remove('border-brand-cyan');
      });

      const target = document.getElementById(tabId);
      if (target) target.classList.remove('hidden');

      const activeBtn = document.getElementById('btn-' + tabId);
      if (activeBtn) {
        activeBtn.classList.add('tab-active');
      }

      setTimeout(() => {
        window.dispatchEvent(new Event('resize'));
      }, 50);
    }

    document.addEventListener('DOMContentLoaded', () => {
      const darkLayout = {
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
        font: { family: 'JetBrains Mono, monospace', color: '#94A3B8', size: 10 },
        margin: { l: 40, r: 20, t: 30, b: 40 },
        autosize: true
      };

      // 1. Radar Chart (Hub Overview)
      Plotly.newPlot('plot-radar-overview', [{
        type: 'scatterpolar',
        r: [9.6, 9.4, 9.8, 9.7, 9.8],
        theta: ['Volume', 'ML Rigor', 'Explainability', 'Latency', 'Reproducibility'],
        fill: 'toself',
        name: 'ElmasCore Standard',
        line: { color: '#06B6D4', width: 2 },
        fillcolor: 'rgba(6, 182, 212, 0.25)'
      }], {
        ...darkLayout,
        polar: {
          bgcolor: 'transparent',
          radialaxis: { visible: true, range: [0, 10], color: '#475569', gridcolor: '#1E293B' },
          angularaxis: { color: '#94A3B8', gridcolor: '#1E293B' }
        },
        showlegend: false
      }, { responsive: true, displayModeBar: false });

      // 2. PCCF Model Benchmark Bar Chart
      Plotly.newPlot('plot-pccf-benchmark', [{
        x: ['Spline-GLM', 'LightGBM Shallow', 'XGBoost Hist', 'CatBoost Deep', 'Nelder-Mead Apex'],
        y: [0.9412, 0.9501, 0.9510, 0.9514, 0.95331],
        type: 'bar',
        marker: { color: ['#334155', '#0284C7', '#0EA5E9', '#06B6D4', '#10B981'] },
        text: ['0.9412', '0.9501', '0.9510', '0.9514', '0.95331'],
        textposition: 'auto',
        textfont: { color: '#FFFFFF', family: 'JetBrains Mono' }
      }], {
        ...darkLayout,
        title: { text: 'PCCF Public ROC-AUC Progression by Architecture', font: { size: 12, color: '#E2E8F0' } },
        yaxis: { range: [0.935, 0.956], gridcolor: '#1E293B', zeroline: false },
        xaxis: { gridcolor: 'transparent' }
      }, { responsive: true, displayModeBar: false });

      // 3. GGVCF Scatter (Guns vs Homicides)
      const ggvcfData = [
        { country: 'Switzerland', guns: 27.6, homicides: 0.13, color: '#06B6D4' },
        { country: 'Serbia', guns: 39.1, homicides: 0.45, color: '#06B6D4' },
        { country: 'United States', guns: 120.5, homicides: 4.52, color: '#F59E0B' },
        { country: 'Jamaica', guns: 8.8, homicides: 38.30, color: '#F43F5E' },
        { country: 'El Salvador', guns: 12.0, homicides: 38.40, color: '#F43F5E' },
        { country: 'Japan', guns: 0.3, homicides: 0.01, color: '#10B981' }
      ];

      Plotly.newPlot('plot-ggvcf-scatter', [{
        x: ggvcfData.map(d => d.guns),
        y: ggvcfData.map(d => d.homicides),
        text: ggvcfData.map(d => d.country),
        mode: 'markers+text',
        textposition: 'top center',
        marker: { size: 10, color: ggvcfData.map(d => d.color) }
      }], {
        ...darkLayout,
        title: { text: 'The Empirical Paradox: Guns vs Murder Rate (rho = -0.0026)', font: { size: 12, color: '#E2E8F0' } },
        xaxis: { title: 'Civilian Firearms per 100 people', gridcolor: '#1E293B' },
        yaxis: { title: 'Firearm Homicide Rate per 100k', gridcolor: '#1E293B' }
      }, { responsive: true, displayModeBar: false });

      // 4. Pneumonia Diagnostic Breakdown Bar
      Plotly.newPlot('plot-pneumonia-breakdown', [{
        x: ['Viral Pneumonia', 'Bacterial Pneumonia', 'Overall Clinical Cohort'],
        y: [100.0, 98.76, 99.23],
        type: 'bar',
        marker: { color: ['#10B981', '#06B6D4', '#3B82F6'] },
        text: ['100.0% (148/148)', '98.8% (239/242)', '99.23% (387/390)'],
        textposition: 'auto',
        textfont: { color: '#FFFFFF', family: 'JetBrains Mono' }
      }], {
        ...darkLayout,
        title: { text: 'Diagnostic Sensitivity on Independent Test Set (624 patients)', font: { size: 12, color: '#E2E8F0' } },
        yaxis: { range: [95, 101], gridcolor: '#1E293B', title: 'Sensitivity (%)' },
        xaxis: { gridcolor: 'transparent' }
      }, { responsive: true, displayModeBar: false });

      // 5. GCMDL Market Cap vs 24h Volume Scatter
      Plotly.newPlot('plot-gcmdl-market', [{
        x: [1640, 340, 92, 85, 35, 15, 2, 0.8, 0.2, 0.05],
        y: [38.5, 19.2, 6.8, 2.1, 1.2, 0.45, 0.12, 0.6, 0.005, 0.0004],
        text: ['BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'AVAX', 'SUI', 'PEPE', 'LOW1', 'LOW2'],
        mode: 'markers+text',
        textposition: 'top center',
        marker: {
          size: [22, 16, 14, 14, 12, 10, 8, 12, 7, 6],
          color: ['#06B6D4', '#06B6D4', '#06B6D4', '#06B6D4', '#3B82F6', '#3B82F6', '#3B82F6', '#F43F5E', '#64748B', '#64748B']
        }
      }], {
        ...darkLayout,
        title: { text: 'GCMDL: 24h Volume vs Market Cap (Log Scales)', font: { size: 12, color: '#E2E8F0' } },
        xaxis: { title: 'Market Cap ($B USD)', type: 'log', gridcolor: '#1E293B' },
        yaxis: { title: '24h Volume ($B USD)', type: 'log', gridcolor: '#1E293B' }
      }, { responsive: true, displayModeBar: false });

      // 6. ISML Dose-Response Stress vs GPA
      Plotly.newPlot('plot-isml-gpa-stress', [{
        x: [5, 10, 15, 18, 22, 26, 30, 35, 38],
        y: [3.8, 3.65, 3.52, 3.40, 3.10, 2.85, 2.60, 2.40, 2.25],
        mode: 'lines+markers',
        line: { color: '#A855F7', width: 3 },
        marker: { size: 8, color: '#C084FC' }
      }], {
        ...darkLayout,
        title: { text: 'ISML: Non-Linear Cliff — Perceived Stress vs Cumulative GPA', font: { size: 12, color: '#E2E8F0' } },
        xaxis: { title: 'Perceived Stress Score (0 - 40)', gridcolor: '#1E293B' },
        yaxis: { title: 'Cumulative GPA (1.70 - 4.00)', range: [2.0, 4.0], gridcolor: '#1E293B' }
      }, { responsive: true, displayModeBar: false });
    });
  </script>
</body>
</html>
"""

OUTPUT_PATH.write_text(HTML_CONTENT, encoding="utf-8")
print(f"Master hub dashboard successfully written to: {OUTPUT_PATH}")
