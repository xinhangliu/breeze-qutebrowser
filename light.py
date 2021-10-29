class P:
    bg1 = '#fcfcfc'
    bg2 = '#eff0f1'
    bg3 = '#bdc3c7'
    bg4 = '#95a5a6'
    bg5 = '#7f8c8d'
    fg1 = '#232629'
    fg2 = '#31363b'
    fg3 = '#4d4d4d'

    blue1 = '#2980b9'
    blue2 = '#3498db'
    red1 = '#da4453'
    red2 = '#e74c30'
    green1 = '#27ae60'
    green2 = '#2ecc71'
    purple1 = '#8e44ad'
    purple2 = '#9b59b6'
    yellow1 = '#f39c1f'
    yellow2 = '#fdbc4b'
    orange1 = '#f67400'
    orange2 = '#f47750'

    hover = '#93cee9'


# Background color of the completion widget category headers.
c.colors.completion.category.bg = P.bg3

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = P.fg3

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = P.fg3

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = P.blue1

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = P.bg1

# Text color of the completion widget.
c.colors.completion.fg = P.fg1

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = P.hover

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = P.hover

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = P.hover

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = P.fg1

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = P.blue1

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = P.blue2

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = P.bg2

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = P.bg2

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = P.bg3

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = P.bg3

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = P.fg3

# Background color of the context menu.
c.colors.contextmenu.menu.bg = P.bg3

# Foreground color of the context menu.
c.colors.contextmenu.menu.fg = P.fg1

# Background color of the context menu’s selected item.
c.colors.contextmenu.selected.bg = P.hover

# Foreground color of the context menu’s selected item.
c.colors.contextmenu.selected.fg = P.fg1

# Background color for the download bar.
c.colors.downloads.bar.bg = P.bg3

# Background color for downloads with errors.
c.colors.downloads.error.bg = P.red2

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = P.fg1

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = P.bg2

# Color gradient start for download text.
c.colors.downloads.start.fg = P.fg1

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = P.hover

# Color gradient end for download text.
c.colors.downloads.stop.fg = P.fg1

# Color gradient interpolation system for download backgrounds.
c.colors.downloads.system.bg = 'none'

# Color gradient interpolation system for download text.
c.colors.downloads.system.fg = 'none'

# Background color for hints.
c.colors.hints.bg = P.hover

# Font color for hints.
c.colors.hints.fg = P.fg1

# Font color for the matched part of hints.
c.colors.hints.match.fg = P.blue1

c.hints.border = f'1px solid {P.blue1}'

# Background color of the keyhint widget.
c.colors.keyhint.bg = P.bg2

# Text color for the keyhint widget.
c.colors.keyhint.fg = P.fg1

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = P.blue1

# Background color of an error message.
c.colors.messages.error.bg = P.red2

# Border color of an error message.
c.colors.messages.error.border = P.red1

# Foreground color of an error message.
c.colors.messages.error.fg = P.fg1

# Background color of an info message.
c.colors.messages.info.bg = P.blue2

# Border color of an info message.
c.colors.messages.info.border = P.blue1

# Foreground color of an info message.
c.colors.messages.info.fg = P.fg1

# Background color of a warning message.
c.colors.messages.warning.bg = P.yellow2

# Border color of a warning message.
c.colors.messages.warning.border = P.yellow1

# Foreground color of a warning message.
c.colors.messages.warning.fg = P.fg1

# Background color for prompts.
c.colors.prompts.bg = P.bg3

# Border used around UI elements in prompts.
c.colors.prompts.border = '1px solid ' + P.fg3

# Foreground color for prompts.
c.colors.prompts.fg = P.fg1

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = P.hover

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = P.fg1

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = P.orange2

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = P.fg1

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = P.yellow2

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = P.fg1

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = P.bg3

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = P.fg1

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = P.purple2

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = P.fg1

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = P.hover

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = P.fg1

# Background color of the statusbar.
c.colors.statusbar.normal.bg = P.bg3

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = P.fg1

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = P.purple2

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = P.fg1

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = P.bg3

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = P.fg1

# Background color of the progress bar.
c.colors.statusbar.progress.bg = P.fg1

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = P.red1

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = P.fg1

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = P.blue2

# Foreground color of the URL in the statusbar on successful load (http).
c.colors.statusbar.url.success.http.fg = P.blue1

# Foreground color of the URL in the statusbar on successful load (https).
c.colors.statusbar.url.success.https.fg = P.blue1

# Foreground color of the URL in the statusbar when there’s a warning.
c.colors.statusbar.url.warn.fg = P.orange1

# Background color of the tab bar.
c.colors.tabs.bar.bg = P.bg2

# Background color of unselected even tabs.
c.colors.tabs.even.bg = P.bg3

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = P.fg2

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = P.red1

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = P.fg3

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = P.green1

# Color gradient interpolation system for the tab indicator.
c.colors.tabs.indicator.system = 'rgb'

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = P.bg3

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = P.fg2

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = P.bg3

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = P.blue1

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = P.bg3

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = P.blue1

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = P.bg1

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = P.blue1

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = P.bg1

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = P.blue1

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = P.bg1

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = P.fg1

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = P.bg1

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = P.fg1

# Background color for webpages if unset (or empty to use the theme’s color).
# c.colors.webpage.bg

# Which algorithm to use for modifying how colors are rendered with darkmode.
# c.colors.webpage.darkmode.algorithm

# Contrast for dark mode.
# c.colors.webpage.darkmode.contrast

# Render all web contents using a dark theme.
# c.colors.webpage.darkmode.enabled

# Render all colors as grayscale.
# c.colors.webpage.darkmode.grayscale.all

# Desaturation factor for images in dark mode.
# c.colors.webpage.darkmode.grayscale.images

# Which images to apply dark mode to.
# c.colors.webpage.darkmode.policy.images

# Which pages to apply dark mode to.
# c.colors.webpage.darkmode.policy.page

# Threshold for inverting background elements with dark mode.
# c.colors.webpage.darkmode.threshold.background

# Threshold for inverting text with dark mode.
# c.colors.webpage.darkmode.threshold.text

# Value to use for prefers-color-scheme: for websites.
# c.colors.webpage.preferred_color_scheme
