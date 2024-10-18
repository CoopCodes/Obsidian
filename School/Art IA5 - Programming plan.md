---
tags:
  - art
---
___
Split each paragraph into divs.

```
for div inside container
	divRect = $(div).getboundingclientrect()
	if (divRect.top > 0vw && divRect.top < 50vw)
		divRect.attr('data-focus', true);
	
	else divRect.attr('data-focus', false);
```

On scroll end, it checks whether the focused paragraph has .bottom bigger than (>) `vh(100) - 50`, if yes:
	It moves up or down until the condition has been satisfied
Else check if it has a bottom less than (<) `vh(100) - 50` if yes:
	It moves up or down until the condition has been satisfied

keep changing scroll position until right