---
tags:
  - art
---
___

# Episode 1: Monkey
Shift+A to add element.
![[Pasted image 20240814112212.png]]

Under *Mesh* are your "primitives", which you use to start a model. E.g. you would use a Cylinder to start a chair, the chair leg, and go from there.

Middle + Mouse Move = Orbit
Scroll = Zoom

Under primitives, press Monkey:
![[Pasted image 20240814112608.png]]
To get started.
- This current view is a lightweight view, that you use in designing.
- But you can make a final render for graphics to be good.
- Rendering Mode:
![[Pasted image 20240814112750.png]]

Shift + Middle Click + Mouse Move = Pan

With an object selected, press *g* to move around the selected object. And right click to cancel, and left click to confirm. 
- If dragging while pressing, you can press axis letter like *y*, and it will drag only on the y-axis.
- Or Middle click to snap.

*F12* to render image, and you can save a picture from the camera. View the camera with *Number pad 0*

To lock camera to view:
1. View the camera.
2. Press *n*
3. *View* tab
4. Then *Lock* and press *Camera to View*

Properties section:
![[Pasted image 20240814113620.png]]
Adding colors to monkey:
- Select monkey
- Go to appearance tab.
- Change the color.
![[Pasted image 20240814113716.png]]

*S* = Scale

# Episode 2: Basic Modelling
Add Torus to scene.
![[Pasted image 20240814114205.png]]

Torus properties.
![[Pasted image 20240814114233.png]]

If you accidentally deselect it, press *F9* to go back to the properties.

- Don't turn the resolution up too much.
	- Slow to render
	- It's easier to add resolution later on, than to take it later on.
- If you want to make the resolution better, right click on the donut:
![[Pasted image 20240814114608.png]]
- Shade Smooth.
![[Pasted image 20240814114626.png]]
 

 To further remove rigid surfaces:
 ![[Pasted image 20240814114909.png]]
 GPU Rendering if not working.

- This subdivision modifier adds resolution.
- 1 face => 4 Face => 8 Face => etc.
![[Pasted image 20240814115055.png]]

**DONUT TOO PERFECT**
## Adding variation
You're currently in object mode, where you can select and create objects.
![[Pasted image 20240814115258.png]]
*Object dependent*
- Change to *Edit mode*.
![[Pasted image 20240814115331.png]]
Alike object mode:
- Select a vertex, and press *g* to move it around:
![[Pasted image 20240814115433.png]]
It changes the shape of the donut.

## Proportional Editing
Instead of moving each vertex individually if you want to create a bunch of movements, you can use proportional editing.
![[Pasted image 20240816134610.png]]

Now you will be able to see a circle, and with an object selected, you can hold *g* and drag the vertices under the circle. 
- Scroll to make the circle bigger, or *PGUP* or *PGDOWN*
![[Pasted image 20240816134814.png]]
This makes it more natural.
Press *Tab* to go to "Edit" mode.

### Edge select
Hold *Alt*, and press on an edge, and it will select all the other vertices on that axis:
![[Pasted image 20240816135205.png]]

Then hold *s* to scale, and drag in, this will make the donut more flat:
![[Pasted image 20240816135256.png]]

## Saving file
Press the Save, you must save it before you finish.

# Part 3: Modelling the Icing
Press *Shift + D* to duplicate, then *ESC* to cancel movement.
Press *F2* to rename.
To select THROUGH a mesh, press the x-ray mode.
![[Pasted image 20240816135920.png]]
Then *Delete* the vertices.

## Solidify Modifier
![[Pasted image 20240816140113.png]]
- This adds a thickness.
- Change the offset to 1.0
- And the thickness 0.025
**Make the icing have little drops around the side:**
- Go into edit mode
![[Pasted image 20240816140354.png]]
- You can pull the points down with the proportional editing tool.
![[Pasted image 20240816140857.png]]
- However it doesn't stick to the surface of the donut.-
![[Pasted image 20240816140944.png]]
- And press the dropdown as well, and change the snap to *Face Project*.
- Before you pull it down, however, you need to increase the subdivisions, as it still clips to the donut.
- Add the *Subdivision* modifier, to add geometry.
![[Pasted image 20240816141329.png]]
- Now there are more faces.
![[Pasted image 20240816141517.png]]
- However if you set the circle too large, it will pull the whole icing under the donut.
- We can fix this by hiding the vertices we don't want to move.
Start by selecting the inner ring, *Alt* click edge.
![[Pasted image 20240816141817.png|300]]
Press *Ctrl + (+)*, and it selects upwards.
![[Pasted image 20240816141857.png|300]]
Do this until the top:
![[Pasted image 20240816141954.png|300]]
Press *H* to hide those vertices
![[Pasted image 20240816142014.png|300]]
Press *Alt + H* to unhide all if needed.

Now you can extrude the icing downwards.
- Press *g* to pull it down, and hold the middle button to snap it to an axis.

Now we need to fix:
![[Pasted image 20240816142357.png]]
Generate a subdivision surface.