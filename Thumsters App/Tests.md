# Feature Content
The **Feature Layout** layout has not disabled the text-overflow property in the *summary* rich-text input, thus if the content isn't manually spaced apart with `\Enter` characters, it will overflow, going behind the feature image/video, and if long enough, beyond it, as seen in *Figure 1*. When the website is Phone size, the rest of the website is downscaled to account for the overflowing text, as seen in *Figure 2*. 

![[Pasted image 20230914105607.png]] *Above, Figure 1*

![[Pasted image 20230914105641.png]] 
*Above, Figure 2*

In the other layouts such as the *Call to action Accordion*, the problem isn't apparent.
This can be fixed with: 
```css
overflow-wrap: break-word;
```
![[Pasted image 20230914115659.png]]![[Pasted image 20230914115827.png]]
# Buttons
The button has the same issue as above, perhaps a character limit could be added, i doubt anyone would put more than a reasonable amount of characters for a button.
![[Pasted image 20230914110539.png]]
