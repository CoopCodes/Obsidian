---
tags:
  - FrontEnd
---
___
Base Html
```html
<div>
	<p>
		bla bla
	</p>
</div>
```

Now we can begin to add properties using `className` in the html:
```html
<div className="h-screen bg-green-400 flex items-center justify-center">
	<p>
		bla bla
	</p>
</div>
```

#### Responsive design in tailwind:
![[Pasted image 20231116160032.png]]
This can be implemented by:
```html
<img className="w-16 md:w-32"> %% this will change to w-32 when size is md %%
 ```

#### Customization:
Inside `tailwind.config.js` we can create color themes:
```js
theme: {
	colors: {
		"color-name": "#hexcode"
	}
}
...
<div class="bg-color-name"></div>
```

##### Custom CSS
Additionally, you can add custom CSS inside your `index.css` file
Tailwind has 3 different layers:
```css
@tailwind base; /* This is if you want to apply styles to every h2 for example */
@tailwind components; /* For react components */
@tailwind utilities; /* For css features that tailwind does not include, such as animations */

@layer components { /* Now you can write like normal css */
	.card {
		background-color: theme("colors.color-name") /* getting color from theme */
	} 
	
	/* you can also apply tailwind class names without having to use css in css*
	.card-2 {
		@apply flex items-center justify-center
	}
}

@layer utilities {

}
```