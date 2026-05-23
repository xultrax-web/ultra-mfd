# ULTR[A] · MFD

> Phosphor amber on iron. The MFD chrome you've been missing in VS Code.

A phosphor-amber multi-function-display theme for VS Code. Iron `#0F0E0C` base, warm phosphor `#FFAE3B` foreground, dense monospace layout. Reads as a cockpit MFD rather than a corporate IDE — without sacrificing legibility on long sessions.

Five operator-pick accent variants — amber, phosphor green, cyan, magenta, rust — for envelope-matching in different working contexts.

---

## Install

1. **Install the theme** from the VS Code marketplace, or `code --install-extension xultrax-web.ultra-mfd`.
2. **Install [Apc Customize UI++](https://marketplace.visualstudio.com/items?itemName=drcika.apc-extension)** (declared as an extension dependency, should auto-prompt).
3. **Reload VS Code.**
4. **Pick a theme**: `Cmd/Ctrl + K, Cmd/Ctrl + T` → search "ULTR[A]" → pick a variant.

### Enable the workbench chrome (the MFD character)

The theme JSON paints colors. The Apc CSS adds the phosphor glow on chrome panels, L-bracket section headers, square corners, dense padding, and the glowing cursor. Without Apc you get the colors but lose the chrome character.

Add to your VS Code `settings.json`:

```jsonc
{
  "apc.imports": ["vscode-file://vscode-app/path/to/extension/apc/ultra-mfd.css"],
}
```

The exact path resolves via the marketplace install location. After install, run `Developer: Open Webview Developer Tools` to copy the resolved extension path, or use the Apc command palette helpers.

---

## Eight themes · four envelopes × two accents

Four primary phosphor envelopes. Each ships in two flavors — the pure envelope, and the same envelope with white keyword/string accents for higher contrast.

| Envelope            | Pure                  | With white accents                   |
| ------------------- | --------------------- | ------------------------------------ |
| **Amber** (default) | ULTR[A] · MFD · Amber | ULTR[A] · MFD · Amber + White Accent |
| **Green**           | ULTR[A] · MFD · Green | ULTR[A] · MFD · Green + White Accent |
| **Cyan**            | ULTR[A] · MFD · Cyan  | ULTR[A] · MFD · Cyan + White Accent  |
| **Rust**            | ULTR[A] · MFD · Rust  | ULTR[A] · MFD · Rust + White Accent  |

Body phosphor values:

| Envelope | Body      | Bright (pure variant) | Bright (white-accent variant) |
| -------- | --------- | --------------------- | ----------------------------- |
| Amber    | `#FFAE3B` | `#FFB81E`             | `#F0E8D5`                     |
| Green    | `#9FE633` | `#B8FF3D`             | `#F0E8D5`                     |
| Cyan     | `#6BCFE8` | `#3DD6FF`             | `#F0E8D5`                     |
| Rust     | `#E0704A` | `#FF8050`             | `#F0E8D5`                     |

Iron base (`#0F0E0C`), the bad semaphore (`#FF6A3D`), and the caution semaphore (`#E8B020`) stay constant across all eight themes for accessibility.

---

## What's in the box

- **5 color themes** — full workbench coverage (editor, sidebar, status bar, terminal, panels, badges, lists, peek view, diff editor, git decorations, breadcrumbs, all hover states)
- **Apc workbench CSS** — phosphor glow on chrome panels (status bar, breadcrumbs, sidebar headers, activity bar), square panel corners, 8×8 L-bracket section header decorations, dense 22px sidebar header height, phosphor cursor with glow
- **Semantic highlighting** support
- **No telemetry** — pure local config
- **No bundled fonts** — declares a `IBM Plex Mono` → `Cascadia Code` → `Consolas` → `monospace` fallback stack; install [IBM Plex Mono](https://github.com/IBM/plex) for the brand match

---

## Recommended font

[**IBM Plex Mono**](https://github.com/IBM/plex). Stencil-cut, slightly wide, reads as instrument-panel typography rather than UI font.

Set in VS Code:

```jsonc
{
  "editor.fontFamily": "'IBM Plex Mono', 'Cascadia Code', Consolas, monospace",
  "editor.fontSize": 13,
  "editor.fontWeight": "400",
  "editor.fontLigatures": false,
}
```

Ligatures off because Drake doctrine: utility over decoration.

---

## Design philosophy

This theme started as "what does a working operator want to look at all day." Three rules from the start:

1. **Editor body code never gets a text-shadow.** Phosphor glow is reserved for chrome panels (status bar, breadcrumbs, sidebar headers). Code reads as code, not as a Sci-Fi prop.
2. **Square panel corners.** No rounded chrome. Hero surfaces (quick-open, dropdowns) get 4px max.
3. **Status bar at full opacity.** Operational truth — git branch, line/col, encoding, problems count — never muted to chrome decoration.

These come from professional dev-tool history (VS Code's own status bar, tmux modelines, the IBM Plex monospace terminal tradition) combined with aviation MFD conventions (multi-function displays — the cockpit screens pilots have used since the 1970s).

---

## Roadmap

**v0.2** — opt-in CRT character:

- Save-pulse keyframe (brief amber border pulse on file save)
- Subtle scanline overlay on chrome panels (off by default)
- CRT flicker (off by default, `prefers-reduced-motion` aware)

**v0.3** — daylight envelope:

- Light-mode counterpart following the same MFD chrome geometry
- Stencil-cream `#F0E8D5` background with deep-amber ink

**v1.0** — file icon theme + product icon theme for full chrome coverage

---

## License

MIT. Use it for whatever.

---

## Author

[@xultrax-web](https://github.com/xultrax-web) · part of the xULTRAx family. Built for operator-grade developer environments.

If you find a workbench element that doesn't pick up theme tokens cleanly, open an issue with a screenshot.
