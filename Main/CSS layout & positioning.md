---
tags:
  - FrontEnd
---
___
# Intro to HTML 
*HTML is just a bunch of tags that you can use to built a site, and they define what type of content is inside it.*

# Intro to CSS 
**C**ascading **S**tyle **S**heets - **CSS**
- There are properties for everything that let you control style.
![[Pasted image 20231204122145.png]]

- One change to this styling, changes all `h2` tags.


# Display Properties
## Block:
- Block elements like text, sections, stack on top of each other, and they take full width of their parent element, by default.

## Flexbox:
- Great for justifying and aligning content visually along one 1 axis.
If we want these elements to be centered:
![[Pasted image 20231207173148.png]]
- We grab the parent, and enable flex, and align and justify it to center
- **1 dimensional layouts**

## Grid:
- **2 Dimensional layouts**
- You can set columns and rows on the parent element, and child elements can go within them.
- Children will automatically take up the next available cell.
- Each child automatically takes up 1 grid, but you can change this.

## Inline-Block:
- like *block* but the element sits inline, sit next to each other on the same line
![[Pasted image 20231207174030.png]]
- And when they hit the end of the container, they wrap. 
- All text is `display: inline-block`

## Inline:
- Behave just like text, but unlike inline block, they don't respect spacing and sizing rules.
- Examples:
	- **Text link**

## None:
- Stops the element rendering, alike just removing it from the html


# Intro to the Box Model
1. Everything can be expressed as boxes
2. By default, those boxes behave like a text document:
![[Pasted image 20231204120430.png]]
- The reason it is like this, because things don't look good on all devices if everything was static.
3. All the boxes, you can control them.

# Spacing
- Padding - The space inside an element
- Margin - The space outside an element

## Horizontally centering something
- Auto Margin:
![[Pasted image 20231210101954.png]]
To center it just press 'auto' for both sides of the margin.
- If you want to vertically center something that has a **fixed** width, you can use **auto** margin on the top and bottom.
- If not, use flexbox and **justify** it center.

## Negative Margin
- You can use negative margin to achieve overlapping.


## Use cases
- Should we use padding and margin to position everything? **Probably Not:
	- Things may not be responsive.

# Size
- By default, elements are sized by the **content inside of it**.

## Size units
- **Pixels** - The default for most dimensions. 
	- If we have a container holding some things, and we set the width to for example 400.
	- The stuff inside the block automatically sized.
	- If we set the things inside the block to be a fixed size, things can overflow, **try not to explicitly set sizes**
- **Percentages**
	- If we set something to be 25% width, that means that the element is 25% as wide as the parent element
- **Ems and Rems** - `1em` is `16px`.
	- **Ems** - based on the font size of the selected element
		- If we set a container width to be `5em`, and we change the font size of an element inside, The element adapts to match that change, shrinks with it.
		- Proportional padding
			- Lets say we have a button, and we set the padding to be `16px`, as the font size grows, the padding stays the same.
			- If we set the padding to be `1em`, Changing the font size, means that the padding scales with the font size.
			- `1em` is always equal to the font size that it is set on, or being inherited by the element.
			- ![[Pasted image 20231210104305.png]]
	- **Rems** - Bypass all the math that Ems have to do. They look straight to the root html page. **Based on the html page settings.**
<button style="
			font-size: 50px;
			margin: auto;
			padding: 1em;
		"
		>Hello?</button>
- **View Port Sizes (`vh & vw & vmin & vmax`)**
	- `100vw` is 100% of the viewport width.
	- A percentage is based on the parent element. Viewport units are based on the device viewport.
	- `vmin & vmax`:
		- With `vmin`, we're basing things off whichever viewport dimension is smaller
		- With `vmax`, that bases off the larger dimensions.
		- If set something to `50vmin`, its 50% of the smaller viewport dimension, which on desktop would be the vertical, but on mobile it would be the horizontal.
		- If we set something to `50vmax`, its 50% of the larger viewport dimension.
- **Fractional units `fr`** - work inside anything that is set to `display: grid;`.
	- If we have 4 elements inside a grid, by default they're width & height is set to `1fr`. If there are 4 columns each `fr` is set to $\frac{1}{4th}$.
	- You can change these values, so we can change the first column to `2fr`
	- ![[Pasted image 20231210105055.png]]
	- In CSS this is:
```css
/* With 2fr for 1 column */
.div-block {
  display: grid;
  grid-auto-columns: 1fr;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  grid-template-columns: ==2fr== 1fr 1fr;
  grid-template-rows: auto auto;
}

/* Without 2fr for 1 column */
.div-block {
  display: grid;
  grid-auto-columns: 1fr;
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto auto;
}
```

 - **Character Units `ch`** 
	- If we have a paragraph, and we set the width to `10ch`
	- The width is being calculated as **10 times the width of the number *0* of any font is being used.**

## Minimums & Maximums
- Lets say we set the width of something to be `50%`.
- As we resize the viewport, it scales down, what if we want a limit to this.
- **Minimum** - If we never want this smaller than `200px`, we set the `min-width: 200px`.
- **Max** - If we never want this bigger than `500px`, we set the `max-width: 500px`.
- Now when we resize, it will never get bigger than `500px`, nor smaller than `200px`.
<img style="width: 50%; min-width: 200px; max-width: 500px" src="data:image/jpeg;base64,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"/>
- An example of this is if there is a section you want to be 100% of the view height, instead of setting the height to `100vh`, which would make it overlay the below content if the windows height is reduced. You can set the height to `auto`, and the Min Height to `100vh`, which means it can be bigger than 100 view port.
- Same when making a section a fixed height with pixels, as the window size decreases it overflow, instead you can set the fixed height on the min height.

## Overflow
- Overflow happens automatically
![[Pasted image 20231210131306.png]]
- When there is a **fixed width & height** on the div block, there is no place for the text to go so it overflows.
- By default the overflow is visible, but you can change it to different properties:
	- Hide - hides the content
	- Scroll - Displays a scrollbar, so people can scroll through it.
	- Auto - Only shows as scrollbar if there is content overflowing.

## Object-fit
- **To use object-fit**: 
	- You need to set an explicit height and width on the parent element
	- We need to set the image height and width to be `100%`.

# CSS position
## `position: static;`
- The default value.
- Things stack on top of each other.

## `position: relative;`
- Just like a static element, but you can move it around from its default place.
	- When you do move it around, it does not effect other elements in the document flow.
![[Pasted image 20231210132601.png]]
### `z-index`
- By default sibling elements, things that come after another are on top of the one before it.
- `!static` elements stop on top of static elements
- It is **not global**. If we have two elements, (each element has children), z-index will control stacking for the parent elements. But if element A has a higher z-index than element B, **The children of element B will NEVER overlap any part of element EVEN if the z-index is `3,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000`**.

## `position: absolute;`
- Elements with this are NO LONGER apart of the document flow
- **Absolute positioning looks up the element hierarchy, and looks for the first parent element that is NOT STATIC, and positions itself aruond THAT.**
- Here we have a div block:
![[Pasted image 20231210133531.png]]
- The div block inside, the 3 dots, is `position: static;` currently.
- Now if we set the top and right to 0, it will be at the top right of the body.
![[Pasted image 20231210133654.png]]
- Now if we want to to go to the top right of the PARENT, we can select the parent.
- And set `position: relative;`:
![[Pasted image 20231210133753.png]]
- Now we can use absolute positioning on a lot of things, and position it relative to the parent by setting the parent to relative.



## `position: fixed;`
- Elements set to this are relative the the VIEWPORT, not the closest non-relative parent.
- Just like absolute positioning, the element is no longer apart of the document flow.
- Now as you scroll, it doesn't move, it sticks to the viewport.
- This is useful for things like a banner, that you want to always show.
- This is also useful for popup.

## `position: sticky;`
- When you make an element sticky, you have to give a value to how far the user has to scroll until it sticks to the page.
- They still take up space on the page alike a static.
- This value can be defined with the `top bottom left right` values.
- If the top is `0`, then when the element is `0px` away from the viewport top, it will stick.
- And if the element is a child, it will only stick when the parent container is in view. 

## Floats and clears
### Floats
- Here we have some text and an image. If we want the image to **float** to the left of the page:
	- `float: left;`
![[Pasted image 20231210145809.png]]
- Now the text wraps AROUND everything
- If an element has a float on it, **It only wraps things around it IF those elements are AFTER the thing that's floating.**
### Clears
- If a clear is applied to an element that is next to a floating element, it doesn't wrap around the element, it clears it.
