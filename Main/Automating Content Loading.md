This app should be build with python.
I am thinking:
- The function should take in 2 **lists** of images:
	1. A list of images that should be executed (either pressed or entered text into), that are within the iteration
- The list should be in order of first press, to last.
- There should be a naming convention:
	- If the image is corresponding to a **button**, that the function should **press**, it should have naming convention of:  `x_anything.png`
		- The `x` means button.
	- If the image is corresponding to a **text input**, that the function should **enter text** into, it should have the naming convention of: `i_{selector}.png`
		- Where, `selector` is the CSS selector that the function should **copy** on the corresponding page.
		- The `i` means input.
- **Web scraping:**
	- There should be a variable named `title`, and it will be the title of the current page, if this is from an Umbraco page, it can be found with `document.querySelectorAll('#nameField > div:nth-child(1) > p')[0].innerHTML`
	- The function should find the corresponding page on the **old site**, using **Selenium**, and get the html from that.