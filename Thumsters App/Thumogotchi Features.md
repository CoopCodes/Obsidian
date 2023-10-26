
*The Thumogotchi app needs to be:*
- Playful UI
- Standard theme among the app
- Smart UX design, so users know where to press.
- Targeted towards children.
- Monster themed:
	- Food can be monster themed.
	- The monsters need to be cute, and interactive.

# Features
## Monster Attributes | [[Monster Attributes]]
- **Hunger** - This attribute will decrease over time.
	- Increased by: **Feeding**
	- Color: **<span style="color: #F3AD61;">#F3AD61</span>** 
- **Health** - Once the hunger attribute == 0, the health will start to decrease. There will be different points where the if the health attribute reaches them, the Thumogotchi will look sad, and even animate crying or something else.
	- Increased by: **Sleeping, Feeding**
	- Color: **<span style="color: #FF4848;">#FF4848</span>** 
- **Happiness** - Overtime this decreases, and can be increased by playing games. This as well will have points where the monster will start to look sad or bored.
	- Increased by: **Playing games**
	- Color: **<span style="color: #02D9A0;">#02D9A0</span>** 
- **Energy** - This attribute will slowly decrease as well, if the monster doesn't have enough energy, it cannot play games. 
	- Increased by: **Sleeping**
	- Color: **<span style="color: #fff82e; background-color: color:black;">#FFF82E</span>** 

## Rooms | (Make monster themed name) | [[Rooms]]
- **Bedroom** - The bedroom should be inside a cave, and have a playful illustrative style.
	- **Sleep**, the monster can sleep in their bed and **Regain energy.** 
	- **Closet**, the user can buy accessories for the monster. And change the monster.
		- **Customizing the monster**, There will be a list of monster parts, categorized by body parts, that can be bought with thumbs. Users can drag them onto nodes. Users can buy these body parts with thumbs, and possibly need to be unlocked with a level.
		![[Monster Customization]]
		- **Accessories**, users can buy accessories for their monster, such as hats, and glasses.
- **Bathroom** - Over time, the monster will get dirty, and will need to be cleaned.
	- **Scrubber** - users will wipe it over the monster, and it will scrub off the dirt, the monster should giggle during this, as it is being tickled.
	- brush teeth
		...
- **Game Room** - This is where the users can increase their monsters *happiness* attribute. There will be many different games, there should be some learning games, and it should be able to give in-game currency if you do well, so users can buy other things for the monster.
- **Office** - This is where the user can actually **talk** to their monster. This will be powered by Chat-GPT, and the user can speak through the microphone.
	- **Speech-To-Text** - Use the `whisper-1` model from `openai` to convert the users speech to text.
	- **Powered by Chat-GPT** - use the `openai` API to contact `gpt-3.5-turbo`, and enter the converted speech to text into the model, and use a text to speech model like `elevenlabs`.