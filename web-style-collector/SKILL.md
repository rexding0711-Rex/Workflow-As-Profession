---
name: web-style-collector
description: >
  Collect, analyze, and document the visual design system of any website into a
  structured markdown report that can be copy-pasted to Kimi to replicate the style.
  Use when the user wants to: (1) capture a website's design style, look & feel,
  or visual identity, (2) analyze a site's colors, typography, layout, spacing,
  components, and interactions, (3) save a website's design tokens for later reference
  or replication, (4) build a copy-pasteable design spec from a URL, (5) document a
  competitor's or inspiration site's visual system, (6) extract CSS/design patterns
  from a live website. Keywords: capture style, collect design, analyze website,
  design tokens, copy style, replicate design, design system, visual identity,
  website inspiration, save layout, color palette, typography, spacing, component
  library, UI analysis, style report, design spec, look and feel, 排版风格,
  收集网站风格, 分析网站设计, 复制网站样式, 设计系统提取, 配色分析.
---

# Web Style Collector

Collect the complete visual design system of any website and produce a structured,
copy-pasteable markdown report. The user can paste this report into a new Kimi
conversation and request: "Build me a landing page using this design system."

## Workflow

### Step 1: Fetch the Page

Use `kimi_fetch_v2` to retrieve the raw HTML content of the target URL. Pass the
full URL exactly as the user provided it. If the site is JS-heavy (SPA, React/Vue/Angular
rendered), note that inline CSS may be limited and the initial HTML may not reflect
the fully rendered DOM. Mention this limitation in the report.

### Step 2: Capture Visual Snapshot (Optional but Recommended)

If `kimi-webbridge` is available and the user wants a more accurate visual analysis,
use WebBridge to open the URL, take a full-page screenshot, and note any dynamic
styles, animations, or responsive behaviors that static HTML cannot capture.

### Step 3: Extract Design Tokens

From the fetched HTML/CSS (and screenshot if available), extract and document:

1. **Color Palette**
   - Primary / Secondary / Accent colors (with hex codes)
   - Background colors (page, sections, cards)
   - Text colors (headings, body, muted, links)
   - Any gradients or special color treatments

2. **Typography**
   - Font families (with fallback stacks)
   - Heading hierarchy (H1-H6 sizes, weights, line-heights)
   - Body text specs (size, weight, line-height, color)
   - Special text styles (captions, labels, code, quotes)

3. **Layout & Spacing**
   - Max content width / container constraints
   - Grid system (if detectable)
   - Section padding / vertical rhythm
   - Card/item spacing and gaps

4. **Components & UI Patterns**
   - Buttons (primary, secondary, ghost, sizes)
   - Forms (inputs, labels, focus states)
   - Navigation patterns
   - Cards / tiles / containers
   - Icons (style, size, usage)

5. **Interactions & Motion**
   - Hover states (if visible in CSS or screenshot)
   - Transitions / animations (duration, easing)
   - Scroll behaviors (parallax, sticky elements)
   - Micro-interactions

6. **Overall Aesthetic**
   - Design philosophy (minimalist, brutalist, corporate, playful, etc.)
   - Visual density ( airy vs. information-dense )
   - Photography / illustration style
   - Rounding / shadows / borders (soft vs. sharp)

### Step 4: Write the Report

Produce a markdown report in this exact structure:

```markdown
# Design System: [Site Name]

## Source
- URL: [original URL]
- Date analyzed: [today]
- Method: HTML fetch + CSS extraction [+ WebBridge screenshot if used]

## Color Palette
| Token | Hex | Usage |
|-------|-----|-------|
| ...   | ... | ...   |

## Typography
| Level | Font | Size | Weight | Line-Height | Color |
|-------|------|------|--------|-------------|-------|
| ...   | ...  | ...  | ...    | ...         | ...   |

## Layout & Spacing
- ...

## Component Patterns
- ...

## Interactions & Motion
- ...

## Overall Aesthetic
- ...

## How to Replicate This Style
When you paste this report into a new Kimi conversation, use this prompt:

> "Build me a [page type] using the exact design system above. 
> Match the colors, typography, spacing, and component styles precisely."
```

### Step 5: Save and Deliver

Save the report to the workspace and provide the file path. Also paste the full
report content in the conversation so the user can copy-paste it immediately.

## Pitfalls

- **JS-rendered sites**: Static HTML fetch may miss dynamically injected styles.
  Always note this limitation and recommend WebBridge for SPAs.
- **CSS-in-JS / styled-components**: Inline CSS may not show up in the raw HTML.
  Extract what you can and flag the limitation.
- **Responsive variations**: The fetched HTML represents one breakpoint. Note the
  likely responsive behavior based on media queries if visible.
- **Fonts**: Custom web fonts may not be available for replication. Suggest Google
  Font equivalents if exact matches are unavailable.
