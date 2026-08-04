"""
Premium Design System for Emotion Detection & Learning Support Engine.
Inject apply_theme() at the top of every page to load all styles.
"""

import streamlit as st


def apply_theme():
    """Inject the full premium CSS design system into the Streamlit app."""
    st.markdown("""
        <style>
        /* ============================================================
           1. GOOGLE FONTS
        ============================================================ */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

        /* ============================================================
           2. CSS VARIABLES — Design Tokens
        ============================================================ */
        :root {
            /* Brand Colors */
            --clr-bg:           #060612;
            --clr-bg-2:         #0D0D1F;
            --clr-bg-3:         #12122A;
            --clr-surface:      rgba(255, 255, 255, 0.04);
            --clr-surface-2:    rgba(255, 255, 255, 0.07);
            --clr-border:       rgba(255, 255, 255, 0.08);
            --clr-border-2:     rgba(124, 58, 237, 0.35);

            /* Accent Palette */
            --clr-primary:      #7C3AED;
            --clr-primary-light:#9F67FF;
            --clr-primary-glow: rgba(124, 58, 237, 0.4);
            --clr-secondary:    #06B6D4;
            --clr-accent:       #F59E0B;
            --clr-success:      #10B981;
            --clr-danger:       #EF4444;
            --clr-warning:      #F59E0B;

            /* Emotion Colors */
            --clr-confused:     #60A5FA;
            --clr-frustrated:   #F87171;
            --clr-confident:    #34D399;
            --clr-bored:        #A78BFA;
            --clr-curious:      #FBBF24;

            /* Text */
            --clr-text-primary: #E2E8F0;
            --clr-text-secondary: #94A3B8;
            --clr-text-muted:   #64748B;

            /* Gradients */
            --grad-primary:     linear-gradient(135deg, #7C3AED 0%, #06B6D4 100%);
            --grad-card:        linear-gradient(135deg, rgba(124,58,237,0.15) 0%, rgba(6,182,212,0.05) 100%);
            --grad-hero:        linear-gradient(135deg, #7C3AED 0%, #A855F7 50%, #06B6D4 100%);
            --grad-glow:        radial-gradient(ellipse at center, rgba(124,58,237,0.15) 0%, transparent 70%);

            /* Spacing */
            --space-xs: 0.25rem;
            --space-sm: 0.5rem;
            --space-md: 1rem;
            --space-lg: 1.5rem;
            --space-xl: 2rem;
            --space-2xl: 3rem;

            /* Typography */
            --font-sans:  'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            --font-mono:  'JetBrains Mono', 'Fira Code', monospace;

            /* Radius */
            --radius-sm:  8px;
            --radius-md:  12px;
            --radius-lg:  16px;
            --radius-xl:  24px;
            --radius-full: 9999px;

            /* Shadows */
            --shadow-sm:    0 2px 8px rgba(0,0,0,0.4);
            --shadow-md:    0 4px 20px rgba(0,0,0,0.5);
            --shadow-lg:    0 8px 40px rgba(0,0,0,0.6);
            --shadow-glow:  0 0 30px rgba(124, 58, 237, 0.25);
            --shadow-glow-lg: 0 0 60px rgba(124, 58, 237, 0.35);

            /* Transitions */
            --ease-fast:  0.15s ease;
            --ease-base:  0.25s ease;
            --ease-slow:  0.4s ease;
            --ease-spring: 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        /* ============================================================
           3. BASE RESET & BODY
        ============================================================ */
        * {
            box-sizing: border-box;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--clr-bg) !important;
            font-family: var(--font-sans) !important;
            color: var(--clr-text-primary) !important;
        }

        [data-testid="stAppViewContainer"] {
            background-image: 
                radial-gradient(ellipse at 20% 10%, rgba(124, 58, 237, 0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 90%, rgba(6, 182, 212, 0.06) 0%, transparent 50%);
        }

        /* ============================================================
           4. CUSTOM SCROLLBAR
        ============================================================ */
        ::-webkit-scrollbar {
            width: 5px;
            height: 5px;
        }
        ::-webkit-scrollbar-track {
            background: var(--clr-bg-2);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--clr-primary);
            border-radius: var(--radius-full);
        }
        ::-webkit-scrollbar-thumb:hover {
            background: var(--clr-primary-light);
        }

        /* ============================================================
           5. TYPOGRAPHY
        ============================================================ */
        h1, h2, h3, h4, h5, h6 {
            font-family: var(--font-sans) !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em !important;
            color: var(--clr-text-primary) !important;
        }
        h1 { font-size: 2.25rem !important; line-height: 1.2 !important; }
        h2 { font-size: 1.6rem  !important; line-height: 1.3 !important; }
        h3 { font-size: 1.25rem !important; }

        p, span, label, div {
            font-family: var(--font-sans) !important;
        }

        code, pre {
            font-family: var(--font-mono) !important;
            background: var(--clr-bg-3) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-sm) !important;
            color: var(--clr-primary-light) !important;
        }

        /* ============================================================
           6. KEYFRAME ANIMATIONS
        ============================================================ */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to   { opacity: 1; }
        }
        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-30px); }
            to   { opacity: 1; transform: translateX(0); }
        }
        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(30px); }
            to   { opacity: 1; transform: translateX(0); }
        }
        @keyframes pulseGlow {
            0%, 100% { box-shadow: 0 0 20px rgba(124, 58, 237, 0.2); }
            50%       { box-shadow: 0 0 40px rgba(124, 58, 237, 0.5); }
        }
        @keyframes shimmer {
            0%   { background-position: -200% center; }
            100% { background-position: 200% center; }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50%       { transform: translateY(-8px); }
        }
        @keyframes spin {
            from { transform: rotate(0deg); }
            to   { transform: rotate(360deg); }
        }
        @keyframes gradient-shift {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes xp-pop {
            0%   { transform: scale(1); opacity: 1; }
            50%  { transform: scale(1.4); opacity: 1; }
            100% { transform: scale(1); opacity: 0; }
        }
        @keyframes streak-flame {
            0%, 100% { transform: scaleY(1) rotate(-2deg); }
            50%       { transform: scaleY(1.1) rotate(2deg); }
        }

        /* ============================================================
           7. GLASSMORPHISM COMPONENTS
        ============================================================ */

        /* Base glass card */
        .glass-card {
            background: var(--clr-surface) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-lg) !important;
            padding: var(--space-lg) !important;
            transition: all var(--ease-base) !important;
            animation: fadeInUp 0.4s ease both !important;
        }
        .glass-card:hover {
            border-color: var(--clr-border-2) !important;
            box-shadow: var(--shadow-glow) !important;
            transform: translateY(-2px) !important;
        }

        /* Elevated glass card */
        .glass-card-elevated {
            background: var(--clr-surface-2) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border: 1px solid rgba(124, 58, 237, 0.2) !important;
            border-radius: var(--radius-xl) !important;
            padding: var(--space-xl) !important;
            box-shadow: var(--shadow-lg), var(--shadow-glow) !important;
        }

        /* Gradient border card */
        .glass-card-gradient {
            background: var(--clr-surface) !important;
            border-radius: var(--radius-lg) !important;
            padding: 2px !important;
            background: linear-gradient(var(--clr-bg-3), var(--clr-bg-3)) padding-box,
                        var(--grad-primary) border-box !important;
            border: 2px solid transparent !important;
        }

        /* ============================================================
           8. SIDEBAR OVERRIDES
        ============================================================ */
        section[data-testid="stSidebar"] {
            background: var(--clr-bg-2) !important;
            border-right: 1px solid var(--clr-border) !important;
            padding-top: 0 !important;
        }
        section[data-testid="stSidebar"] > div {
            background: transparent !important;
        }

        /* Sidebar nav items */
        section[data-testid="stSidebar"] a {
            border-radius: var(--radius-md) !important;
            transition: all var(--ease-base) !important;
            padding: 0.6rem 1rem !important;
            margin: 2px 8px !important;
            display: block !important;
        }
        section[data-testid="stSidebar"] a:hover {
            background: var(--clr-surface-2) !important;
            color: var(--clr-primary-light) !important;
        }
        [data-testid="stSidebarNav"] a[aria-selected="true"],
        [data-testid="stSidebarNav"] a[data-active="true"] {
            background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(6,182,212,0.1)) !important;
            border-left: 3px solid var(--clr-primary) !important;
        }

        /* ============================================================
           9. BUTTON OVERRIDES
        ============================================================ */

        /* Primary button */
        div.stButton > button[kind="primary"],
        div.stButton > button:first-child[data-baseweb="button"] {
            background: var(--grad-primary) !important;
            color: #fff !important;
            border: none !important;
            border-radius: var(--radius-md) !important;
            font-weight: 700 !important;
            font-family: var(--font-sans) !important;
            font-size: 1rem !important;
            letter-spacing: 0.02em !important;
            padding: 0.8rem 2rem !important;
            min-height: 3rem !important;
            transition: all var(--ease-spring) !important;
            box-shadow: 0 4px 20px rgba(124, 58, 237, 0.45), 0 0 0 1px rgba(124,58,237,0.2) !important;
            background-size: 200% 200% !important;
            animation: gradient-shift 3s ease infinite !important;
        }
        div.stButton > button[kind="primary"]:hover {
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 10px 35px rgba(124, 58, 237, 0.65), 0 0 0 1px rgba(124,58,237,0.4) !important;
        }
        div.stButton > button[kind="primary"]:active {
            transform: translateY(-1px) scale(0.99) !important;
        }

        /* Secondary buttons */
        div.stButton > button:first-child {
            background: var(--clr-surface) !important;
            border: 1px solid var(--clr-border) !important;
            color: var(--clr-text-primary) !important;
            border-radius: var(--radius-md) !important;
            font-family: var(--font-sans) !important;
            transition: all var(--ease-base) !important;
        }
        div.stButton > button:first-child:hover {
            background: var(--clr-surface-2) !important;
            border-color: var(--clr-primary) !important;
            color: var(--clr-primary-light) !important;
            transform: translateY(-2px) !important;
            box-shadow: var(--shadow-sm) !important;
        }

        /* ============================================================
           10. METRIC CARDS
        ============================================================ */
        div[data-testid="metric-container"] {
            background: var(--clr-surface) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-lg) !important;
            padding: 1.25rem !important;
            backdrop-filter: blur(16px) !important;
            transition: all var(--ease-base) !important;
            animation: fadeInUp 0.4s ease both !important;
        }
        div[data-testid="metric-container"]:hover {
            border-color: var(--clr-border-2) !important;
            box-shadow: var(--shadow-glow) !important;
            transform: translateY(-3px) !important;
        }
        div[data-testid="metric-container"] [data-testid="stMetricValue"] {
            font-size: 2rem !important;
            font-weight: 800 !important;
            background: var(--grad-primary) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
        }
        div[data-testid="metric-container"] [data-testid="stMetricLabel"] {
            color: var(--clr-text-secondary) !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
        }
        div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
            font-size: 0.8rem !important;
        }

        /* ============================================================
           11. INPUT & FORM OVERRIDES
        ============================================================ */
        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
            background: var(--clr-bg-3) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-md) !important;
            color: var(--clr-text-primary) !important;
            font-family: var(--font-sans) !important;
            transition: border-color var(--ease-fast) !important;
        }
        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stTextArea"] textarea:focus {
            border-color: var(--clr-primary) !important;
            box-shadow: 0 0 0 3px var(--clr-primary-glow) !important;
            outline: none !important;
        }

        /* ============================================================
           12. PROGRESS BAR OVERRIDES
        ============================================================ */
        div[data-testid="stProgressBar"] > div > div > div {
            background: var(--grad-primary) !important;
            border-radius: var(--radius-full) !important;
            transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        div[data-testid="stProgressBar"] > div > div {
            background: var(--clr-bg-3) !important;
            border-radius: var(--radius-full) !important;
        }

        /* ============================================================
           13. TABS OVERRIDES
        ============================================================ */
        div[data-testid="stTabs"] button[role="tab"] {
            font-family: var(--font-sans) !important;
            font-weight: 500 !important;
            color: var(--clr-text-secondary) !important;
            border-radius: var(--radius-md) var(--radius-md) 0 0 !important;
            transition: all var(--ease-base) !important;
            padding: 0.6rem 1.2rem !important;
        }
        div[data-testid="stTabs"] button[role="tab"]:hover {
            color: var(--clr-text-primary) !important;
            background: var(--clr-surface) !important;
        }
        div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
            color: var(--clr-primary-light) !important;
            border-bottom: 2px solid var(--clr-primary) !important;
            background: var(--clr-surface) !important;
        }

        /* ============================================================
           14. CHAT MESSAGE OVERRIDES
        ============================================================ */
        div[data-testid="stChatMessage"] {
            background: var(--clr-surface) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-lg) !important;
            padding: var(--space-md) var(--space-lg) !important;
            animation: fadeInUp 0.3s ease both !important;
        }
        div[data-testid="stChatMessage"][data-testid*="user"] {
            border-color: rgba(124, 58, 237, 0.25) !important;
            background: linear-gradient(135deg, rgba(124,58,237,0.08), transparent) !important;
        }

        /* ============================================================
           15. ALERT / INFO BOXES
        ============================================================ */
        div[data-testid="stAlert"] {
            border-radius: var(--radius-md) !important;
            border-left-width: 3px !important;
            font-family: var(--font-sans) !important;
        }
        div.stSuccess {
            background: rgba(16, 185, 129, 0.1) !important;
            border-color: var(--clr-success) !important;
        }
        div.stWarning {
            background: rgba(245, 158, 11, 0.1) !important;
            border-color: var(--clr-warning) !important;
        }
        div.stError {
            background: rgba(239, 68, 68, 0.1) !important;
            border-color: var(--clr-danger) !important;
        }
        div.stInfo {
            background: rgba(6, 182, 212, 0.1) !important;
            border-color: var(--clr-secondary) !important;
        }

        /* ============================================================
           16. EXPANDER OVERRIDES
        ============================================================ */
        div[data-testid="stExpander"] {
            background: var(--clr-surface) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-lg) !important;
            overflow: hidden !important;
        }
        div[data-testid="stExpander"] summary {
            font-family: var(--font-sans) !important;
            font-weight: 600 !important;
            color: var(--clr-text-primary) !important;
            padding: var(--space-md) !important;
        }
        div[data-testid="stExpander"] summary:hover {
            color: var(--clr-primary-light) !important;
        }

        /* ============================================================
           17. DATAFRAME / TABLE
        ============================================================ */
        div[data-testid="stDataFrame"] {
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-lg) !important;
            overflow: hidden !important;
        }

        /* ============================================================
           18. TOP TOOLBAR / MAIN HEADER HIDE
        ============================================================ */
        #MainMenu { visibility: hidden; }
        footer    { visibility: hidden; }
        header    { visibility: hidden; }

        /* ============================================================
           19. MAIN CONTENT PADDING
        ============================================================ */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            max-width: 1200px !important;
        }

        /* ============================================================
           20. UTILITY CLASSES (used in HTML components)
        ============================================================ */

        /* Gradient text */
        .gradient-text {
            background: var(--grad-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Animated gradient text */
        .gradient-text-animated {
            background: linear-gradient(270deg, #7C3AED, #06B6D4, #A855F7, #7C3AED);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradient-shift 4s ease infinite;
        }

        /* Badge / pill */
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 10px;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.02em;
        }
        .badge-primary   { background: rgba(124,58,237,0.2);  color: var(--clr-primary-light); border: 1px solid rgba(124,58,237,0.3); }
        .badge-success   { background: rgba(16,185,129,0.15); color: #34D399; border: 1px solid rgba(16,185,129,0.3); }
        .badge-warning   { background: rgba(245,158,11,0.15); color: #FBBF24; border: 1px solid rgba(245,158,11,0.3); }
        .badge-danger    { background: rgba(239,68,68,0.15);  color: #F87171; border: 1px solid rgba(239,68,68,0.3); }
        .badge-cyan      { background: rgba(6,182,212,0.15);  color: #22D3EE; border: 1px solid rgba(6,182,212,0.3); }

        /* Emotion-specific badge colors */
        .badge-confused    { background: rgba(96,165,250,0.15);  color: #60A5FA; border: 1px solid rgba(96,165,250,0.3); }
        .badge-frustrated  { background: rgba(248,113,113,0.15); color: #F87171; border: 1px solid rgba(248,113,113,0.3); }
        .badge-confident   { background: rgba(52,211,153,0.15);  color: #34D399; border: 1px solid rgba(52,211,153,0.3); }
        .badge-bored       { background: rgba(167,139,250,0.15); color: #A78BFA; border: 1px solid rgba(167,139,250,0.3); }
        .badge-curious     { background: rgba(251,191,36,0.15);  color: #FBBF24; border: 1px solid rgba(251,191,36,0.3); }

        /* Stat card */
        .stat-card {
            background: var(--clr-surface);
            border: 1px solid var(--clr-border);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.5rem;
            text-align: center;
            transition: all var(--ease-base);
            animation: fadeInUp 0.4s ease both;
            cursor: default;
        }
        .stat-card:hover {
            border-color: var(--clr-border-2);
            box-shadow: var(--shadow-glow);
            transform: translateY(-4px);
        }
        .stat-card .stat-value {
            font-size: 2.2rem;
            font-weight: 800;
            background: var(--grad-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1.1;
            margin-bottom: 0.3rem;
        }
        .stat-card .stat-label {
            font-size: 0.8rem;
            color: var(--clr-text-secondary);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }
        .stat-card .stat-icon {
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
        }

        /* Feature card */
        .feature-card {
            background: var(--clr-surface);
            border: 1px solid var(--clr-border);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            transition: all var(--ease-base);
            animation: fadeInUp 0.5s ease both;
            height: 100%;
        }
        .feature-card:hover {
            background: var(--clr-surface-2);
            border-color: var(--clr-border-2);
            box-shadow: var(--shadow-glow);
            transform: translateY(-6px);
        }
        .feature-card .feature-icon {
            font-size: 2rem;
            margin-bottom: 0.75rem;
        }
        .feature-card .feature-title {
            font-size: 1rem;
            font-weight: 700;
            color: var(--clr-text-primary);
            margin-bottom: 0.5rem;
        }
        .feature-card .feature-desc {
            font-size: 0.875rem;
            color: var(--clr-text-secondary);
            line-height: 1.5;
        }

        /* Timeline item */
        .timeline-item {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            padding: 0.75rem 0;
            border-bottom: 1px solid var(--clr-border);
            animation: fadeInUp 0.3s ease both;
        }
        .timeline-item:last-child { border-bottom: none; }
        .timeline-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--clr-primary);
            margin-top: 5px;
            flex-shrink: 0;
            box-shadow: 0 0 8px var(--clr-primary-glow);
        }
        .timeline-content {
            flex: 1;
        }
        .timeline-title {
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--clr-text-primary);
        }
        .timeline-meta {
            font-size: 0.75rem;
            color: var(--clr-text-muted);
            margin-top: 2px;
        }

        /* Achievement badge */
        .achievement-badge {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
            padding: 1rem 0.75rem;
            background: var(--clr-surface);
            border: 1px solid var(--clr-border);
            border-radius: var(--radius-lg);
            transition: all var(--ease-base);
            text-align: center;
        }
        .achievement-badge.unlocked {
            border-color: rgba(245,158,11,0.4);
            background: rgba(245,158,11,0.06);
            box-shadow: 0 0 20px rgba(245,158,11,0.15);
        }
        .achievement-badge.locked {
            opacity: 0.4;
            filter: grayscale(0.8);
        }
        .achievement-badge .badge-icon  { font-size: 1.75rem; }
        .achievement-badge .badge-name  { font-size: 0.7rem; font-weight: 600; color: var(--clr-text-secondary); }

        /* XP bar container */
        .xp-bar-container {
            background: var(--clr-bg-3);
            border-radius: var(--radius-full);
            height: 8px;
            overflow: hidden;
            margin: 4px 0;
        }
        .xp-bar-fill {
            height: 100%;
            background: var(--grad-primary);
            border-radius: var(--radius-full);
            transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        .xp-bar-fill::after {
            content: '';
            position: absolute;
            top: 0; left: -200%;
            width: 200%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            animation: shimmer 2s infinite;
        }

        /* Emotion confidence ring — used via components.py HTML */
        .confidence-ring-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 1.5rem;
        }
        .confidence-value {
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--grad-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-top: -0.5rem;
        }
        .confidence-label {
            font-size: 0.75rem;
            color: var(--clr-text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-weight: 600;
        }

        /* Glow separator */
        .glow-separator {
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--clr-primary), var(--clr-secondary), transparent);
            margin: 1.5rem 0;
            opacity: 0.5;
        }

        /* Section header */
        .section-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.25rem;
        }
        .section-header-icon {
            font-size: 1.4rem;
        }
        .section-header-text {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--clr-text-primary);
        }
        .section-header-badge {
            margin-left: auto;
        }

        /* Spinner / loading shimmer */
        .skeleton-loader {
            background: linear-gradient(90deg, var(--clr-surface) 25%, var(--clr-surface-2) 50%, var(--clr-surface) 75%);
            background-size: 200% 100%;
            animation: shimmer 1.5s infinite;
            border-radius: var(--radius-md);
        }

        /* Step badge (for how-it-works) */
        .step-number {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--grad-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1rem;
            color: white;
            flex-shrink: 0;
            box-shadow: 0 4px 15px rgba(124,58,237,0.4);
        }

        /* Tech stack badge */
        .tech-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            background: var(--clr-surface);
            border: 1px solid var(--clr-border);
            border-radius: var(--radius-full);
            font-size: 0.8rem;
            font-weight: 500;
            color: var(--clr-text-secondary);
            transition: all var(--ease-base);
        }
        .tech-badge:hover {
            border-color: var(--clr-primary);
            color: var(--clr-primary-light);
            background: var(--clr-surface-2);
        }

        /* Card grid spacing */
        div[data-testid="column"] {
            animation: fadeInUp 0.4s ease both;
        }

        /* Hero gradient background overlay */
        .hero-gradient {
            position: relative;
            padding: 4rem 2rem;
            text-align: center;
            overflow: hidden;
        }
        .hero-gradient::before {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(ellipse at center, rgba(124,58,237,0.12) 0%, transparent 60%);
            animation: float 6s ease-in-out infinite;
            pointer-events: none;
        }

        /* Notification / toast style */
        .xp-toast {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            background: linear-gradient(135deg, rgba(124,58,237,0.3), rgba(6,182,212,0.2));
            border: 1px solid rgba(124,58,237,0.4);
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--clr-primary-light);
            animation: fadeInUp 0.3s ease both, xp-pop 1.5s ease 0.5s both;
        }

        /* Selectbox dropdown */
        div[data-baseweb="popover"] ul {
            background: var(--clr-bg-2) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-md) !important;
        }
        div[data-baseweb="popover"] ul li:hover {
            background: var(--clr-surface-2) !important;
        }

        /* Checkbox */
        div[data-testid="stCheckbox"] label {
            font-family: var(--font-sans) !important;
            font-size: 0.9rem !important;
        }
        div[data-testid="stCheckbox"] span[aria-checked="true"] {
            background-color: var(--clr-primary) !important;
            border-color: var(--clr-primary) !important;
        }

        /* Radio buttons */
        div[data-testid="stRadio"] label {
            font-family: var(--font-sans) !important;
        }

        /* Staggered animation delays for children */
        div[data-testid="column"]:nth-child(1) { animation-delay: 0.0s; }
        div[data-testid="column"]:nth-child(2) { animation-delay: 0.1s; }
        div[data-testid="column"]:nth-child(3) { animation-delay: 0.2s; }
        div[data-testid="column"]:nth-child(4) { animation-delay: 0.3s; }

        /* Divider line */
        hr {
            border: none !important;
            height: 1px !important;
            background: var(--clr-border) !important;
            margin: 1.5rem 0 !important;
        }

        /* ============================================================
           21. PLOTLY CHART BACKGROUND FIX
        ============================================================ */
        .js-plotly-plot .plotly .bg {
            fill: transparent !important;
        }
        div[data-testid="stPlotlyChart"] {
            background: var(--clr-surface) !important;
            border: 1px solid var(--clr-border) !important;
            border-radius: var(--radius-lg) !important;
            padding: 0.5rem !important;
        }

        </style>
    """, unsafe_allow_html=True)


# ── Plotly default config (transparent background, matching theme) ──────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#94A3B8"),
    margin=dict(t=40, b=20, l=20, r=20),
    title_font=dict(size=14, color="#E2E8F0", family="Inter"),
    xaxis=dict(
        gridcolor="rgba(255,255,255,0.05)",
        showgrid=True,
        zerolinecolor="rgba(255,255,255,0.08)",
    ),
    yaxis=dict(
        gridcolor="rgba(255,255,255,0.05)",
        showgrid=True,
        zerolinecolor="rgba(255,255,255,0.08)",
    ),
    colorway=["#7C3AED", "#06B6D4", "#10B981", "#F59E0B", "#EF4444"],
)

# Emotion → colour map used across charts and badges
EMOTION_COLORS = {
    "Confused":   "#60A5FA",
    "Frustrated": "#F87171",
    "Confident":  "#34D399",
    "Bored":      "#A78BFA",
    "Curious":    "#FBBF24",
}

# Emotion → emoji map
EMOTION_EMOJI = {
    "Confused":   "😕",
    "Frustrated": "😤",
    "Confident":  "🎉",
    "Bored":      "😑",
    "Curious":    "🤩",
}
