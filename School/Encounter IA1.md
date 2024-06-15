---
tags:
  - encounter
---
___
___
# Introduction 
"Hell is one of the most misunderstood concepts of Christian theology, both by those within the religion, and by those outside of it. This misrepresentation of Hell not only does damage to the image of the Christian Church, but also causes some of the faithful, themselves, to fall away from what they perceive to be a monstrous God." (_What You Know about Hell Is Wrong_, 2022). Hell is a massively misrepresented part of Christianity. This misrepresentation derives from the money-driven Roman Catholics, and is this outdated, manipulated belief is something a lot of non-Christian people think. And, in fact it is one of the biggest obstacle that stops people from wanting to believe in God.


# My opinion
This is something i have been tackling with for weeks now. *How can a loving God send people to Hell, to be tortured for eternity?* 
1 John 4:7; It states that *God is love*, which a majority of Christians believe, and in 1 Corinthians 13 it states:

<div style="font-size: .7em">
Love is patient, love is kind. It does not envy, it does not boast, it is not proud. <br>
5 It does not dishonor others, it is not self-seeking, it is not easily angered, it keeps no record of wrongs. <br>
6 Love does not delight in evil but rejoices with the truth. <br>
7 It always protects, always trusts, always hopes, always perseveres.<br>
</div>

If God is Love, and love keeps no record of wrongs, and love is kind, and love **always** perseveres (Always tries to make us right), then God could not send us to an *eternal hell* for the following reasons:
- He must always try to persevere and save us, Samuel 1:9 <span style="font-size: .7em">14 Like water spilled on the ground, which cannot be recovered, so we must die. But that is not what God desires; rather, he devises ways so that a banished person does not remain banished from him.</span>
	- He devises ways to return a banished person from him.

# What does the Bible say about Hell
In a perfect world, the Bible would just say one thing about hell, and that is it. However the truth is that the bible often contradicts itself, 

Against Hell:
1 John 2:1-2
1 Corinthians 15:22

For Hell:
Matthew 7:13 [Matthew 7:13 - Εἰσέλθατε 5657 διὰ... - Interlinear Study Bible (studylight.org)](https://www.studylight.org/interlinear-study-bible/greek/matthew/7-13.html)
Matthew 13:50 [Matthew 13:50 - καὶ βαλοῦσιν 5692... - Interlinear Study Bible (studylight.org)](https://www.studylight.org/interlinear-study-bible/greek/matthew/13-50.html)

"Precisely. You can't save this world. That's what we did."











# Bibliography

| Citation                                                                                                                                                  | In-text Citation                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| _What You Know About Hell is Wrong_. (2022, July 27). Beliefnet.com. https://www.beliefnet.com/faiths/christianity/what-you-know-about-hell-is-wrong.aspx | (_What You Know about Hell Is Wrong_, 2022) |






```js
const filterOffset(curOffsetX, curOffsetY, image) {
  	let offsetX = curOffsetX;
  	let offsetY = curOffsetY;
  
    let percentWidth = 100 * image.width() / image.offsetParent().width();  
  	
    let xBounds = {
    	"left": percentWidth / 2,
      "right": 100 - (percentWidth / 2)
    }
    
    let percentHeight = Math.round(100 * image.height() / image.offsetParent().height());  
  	
    let yBounds = {
    	"top": percentHeight / 2,
      "bottom": 100 - (percentHeight / 2)
    }
    
  	offsetX = (offsetX < xBounds["left"]) ? xBounds["left"]
    	: (offsetX > xBounds["right"]) ? xBounds["right"] : offsetX;
	
	offsetY = (offsetY < yBounds["top"]) ? yBounds["top"]
    	: (offsetY > yBounds["bottom"]) ? yBounds["bottom"] : offsetY;
  }
```























