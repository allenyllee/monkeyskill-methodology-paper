# Restore right click & copy

## Goal

Restore the browser context menu, text selection, copying, cutting,
pasting, and dragging on pages that intentionally block those native
interactions.

## Safety constraints

- Never make network requests.
- Never read cookies, storage, form values, or clipboard contents.
- Never modify links, form submission, navigation, or left-click handlers.
- Do not run on Chrome internal pages or the Chrome Web Store.

## Validated implementation constraint (excerpt)

For a real drag whose selection is cleared on release, synchronously clone
the live, non-collapsed range in a pointerup/mouseup capture listener before
page release handlers can clear it. Restore from that saved clone at a later
macrotask checkpoint. Do not use selectionchange or a release timer as the
only snapshot point. Scope this state to the active drag; ordinary page
clicks and control clicks must discard the stale range.

## Success criteria (excerpt)

- [criterion:context-menu] A real user right-click can open the native
  context menu on ordinary elements, inputs, images, overlays, and
  CSS-background elements.
- [criterion:no-network] The implementation makes no network requests.
