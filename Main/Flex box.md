---
tags:
  - FrontEnd
---
___
# Flexbox
- EVERYONE USES FLEXBOX
- You usually set flex on the parent elements, and less on the children

## Alignment and justification
- To center a heading:
	- Use flex on the parent of the element.
	- Now you can align and justify center, and it is centered.
		- **Align - Y AXIS**
		- **Justify - X AXIS**

## Flex children
- You can manually set the order of the element in the flex. with: `order: num;`
- You can also change the alignment of the child in the flexbox. with: `align-self`


## Auto Margin
Example 1:
![[Pasted image 20231210151015.png]]
- Each card is using flex.
- Because the card is flex, we can select all the buttons, and set their margin-top to `auto`.
- This floats it to the bottom.
![[Pasted image 20231210151116.png]]

Example 2:
![[Pasted image 20231210151204.png]]
- How do we get the footer to always stay at the bottom?
	- Set the body to flex.
	- And on the footer section, set the margin-top to `auto`.

Example 3:
![[Pasted image 20231219155122.png]]
- How to make these tags wrap downwards?
	- Choose `flex-wrap: true;`
- 