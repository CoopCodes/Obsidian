---
tags:
  - FrontEnd
---

___
- In CSS Grid, things are **automatically positioned**
- By default, things take up the available cells, and wrap to the next line automatically.
- Elements added to a grid by default, are AUTOMATICALLY positioned.
- **Grids are non-destructive**, removing a row or column does not remove the content inside it.

## Auto position
- You can align and justify children inside the grid. If you align it center, the child element will be aligned to the center of that individual grid boundaries.
- Object-fit:
	- Set the width and height to 100%, and set object-fit to be **Cover**
- If we remove the fixed width from the grid container itself, everything disappears.
- But because we set the image height and width to be 100%, it only takes up as much as the rows and columns are.

## Manual positioning
In grid, when setting the height/width of a row/column, if we set it to **auto**, it will only be as tall/wide as the content inside.

## Reusable Layouts
You can set labels on sections, and reuse them.

## Responsive design
- If you have a manually positioned item, you'll have to manually move them.


