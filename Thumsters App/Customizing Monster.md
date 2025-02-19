A body part is comprised of a *node* and an *Image*. The node determines what position (In pixels) the origin of the body part is. As seen below:
![[Drawing 2023-09-21 10.01.31.excalidraw]]
# `BodyPart Class`
```tsx
export class BodyPart {
  node: [number, number]; // The Nodes position, this is where the body part connects to the body.
  image: ImageSourcePropType; // Image path
  constructor(node: [number, number], image: ImageSourcePropType) {
    this.node = node;
    this.image = image;
  }
}
```

All the body parts are then loaded in the bottom of the `global.ts` file.
```tsx
// Assets: right now it is loading only the first monster, but this needs to be changed so it is dynamic.
export const bodyParts: {[key: number]: {[key: string]: BodyPart}} = {
  1: {
    arm: new BodyPart([0, 0], arm),
    eye: new BodyPart([0, 0], eye),
    foot: new BodyPart([0, 0], foot),
    horn: new BodyPart([0, 0], horn),
    mouth: new BodyPart([0, 0], mouth),
  }
}
```

There is then a `Body` class, to store the information state of the current monsters body:
```tsx
export class Body {
  nodes: IBodyPartNodes;
  bodyImage: ImageSourcePropType | undefined;
  constructor(nodes: IBodyPartNodes = emptyBodyPartNodes, bodyImage: ImageSourcePropType | undefined) {
    this.nodes = nodes;
    this.bodyImage = bodyImage;
  }
}
```
- It holds the nodes, which is all the connection places that the body will have body parts.
![[Monster Customization]]
- `IBodyPartNodes` is declared in the following code:
```tsx
export type bodyPartInfo = {
  bodyPart: BodyPart,
  ref: Ref<Image> | undefined // User defined
}

export interface IBodyPartNodes {
  leftarm: bodyPartInfo;
  rightarm: bodyPartInfo;
  leftleg: bodyPartInfo;
  rightleg: bodyPartInfo;
  eyes: bodyPartInfo;
  mouth: bodyPartInfo;
}
```
- The actual *monster* component is going to be comprised of `<Image>` tags, holding each body part, and will be transformed according to its node with `StyleSheets`, thus the `ref` property. However, if the user has not chosen the body part yet, the ref will be undefined. 
- The `IBodyPartNodes` is just a list of all the connections that a body can have.
- When the `Monster` is created, on app initialization, the monster will be created in `App.tsx` with `new Body(undefined, undefined)` as the user has not chosen the body, or any body parts. And the `node` property will be defaulted to `emptyBodyPartNodes`, which is just an empty implementation of the `IBodyPartNodes` interface:
```tsx
const emptyBodyPartInfo: bodyPartInfo = {
  bodyPart: new BodyPart([0, 0], ImageNotImplemented),
  ref: undefined,
}
  
const emptyBodyPartNodes: IBodyPartNodes = {
  leftarm: emptyBodyPartInfo,
  rightarm: emptyBodyPartInfo,
  leftleg: emptyBodyPartInfo,
  rightleg: emptyBodyPartInfo,
  eyes: emptyBodyPartInfo,
  mouth: emptyBodyPartInfo,
}
```
- By default the body part will have a node of `[0, 0]`, and an `ImageNotImplemented` image, which is just a transparent image. So when the `Monster.tsx` component will be loaded, and the user hasn't picked all of the body parts, no part will be shown for the part not chosen.

Now a global state for the monster is implemented in `App.tsx` 
```tsx
  // Monster Logic TODO: change the way body is accessed
  type monsterAction = {
    bodyParts: IBodyPartNodes | undefined,
    bodyImage: ImageSourcePropType | undefined,
  }
  
  const monsterReducer = (state: Body, action: monsterAction) => {
    if (action.bodyParts)
      state.nodes = action.bodyParts;
    state.bodyImage = action.bodyImage;
    return state;
  }

  const [monster, monsterDispatch] = useReducer(monsterReducer, new Body(undefined, undefined));
```

These will be compiled in the `Monster.tsx` component:
```tsx
Props = {
	monsterBody: Body,
	mood: string,
}
...
// Initializing the Refs, so a transform can be applied
const leftArmRef = useRef(null); 
const rightArmRef = useRef(null);
const leftLegRef = useRef(null);
const rightLegRef = useRef(null);
const eyesRef = useRef(null);
const mouthRef = useRef(null);

// setting each bodyPart node.ref of the monsterBody prop to the ref previously created.
useEffect(() => {
	monsterBody.nodes.leftarm.ref = leftArmRef;
	monsterBody.nodes.rightarm.ref = rightArmRef;
	monsterBody.nodes.rightleg.ref = rightLegRef;
	monsterBody.nodes.leftleg.ref = leftLegRef;
	monsterBody.nodes.eyes.ref = eyesRef;
	monsterBody.nodes.mouth.ref = mouthRef;
}, [])

// Applying the transformations based on the nodes declared in global.ts file.
Object.values(monsterBody.nodes).map((bodypart) => {
	bodypart.ref.setNativeProps({
	style: {
		transform: [
			{ translateX: bodypart.coords.x },
			{ translateY: bodypart.coords.y },
		],
	},
	});
})

// Now creating the images, based on what body part, and its image.
return (
	<View>
		<Image ref={leftArmRef} source={monsterBody.nodes.leftarm.bodyPart.image}/>
		<Image ref={rightArmRef} source={monsterBody.nodes.rightarm.bodyPart.image}/>
		<Image ref={leftLegRef} source={monsterBody.nodes.leftleg.bodyPart.image} />
		<Image ref={rightLegRef} source={monsterBody.nodes.rightleg.bodyPart.image}/>
		<Image ref={eyesRef} source={monsterBody.nodes.eyes.bodyPart.image}/>
		<Image ref={mouthRef} source={monsterBody.nodes.mouth.bodyPart.image}/>
	</View>
)
```


Now that the customization for the monster is set up, we need to make a way to implement drag & drop of body parts from a list of body parts. 
First we need to detect when the user is holding an item over an item in the `bodypart` list.

-- DEPRECATED \ DECIDED NOT TO USE --

This can be implemented by creating a `bodypart` component, that will be rendered in a list of all the body parts that the user can choose:

```tsx
type Props: {
	bodypart: BodyPart,
}

const ListBodyPart = ({ bodypart: BodyPart }: Props, => {
  const pan = useRef(new Animated.ValueXY()).current;
  const [isDragging, setIsDragging] = useState(false);
  const [withinThreshold, setWithinThreshold] = useState<[boolean, Number[] | undefined]>([false, undefined]);

  const panResponder = useRef(
    PanResponder.create({
      onStartShouldSetPanResponder: () => true,
      onPanResponderGrant: () => {
        setIsDragging(true);
        // Set the initial position of the 
        // component to the finger position
        pan.setOffset({
          x: pan.x._value,
          y: pan.y._value
        });
        pan.setValue({ x: bodypart.nodes[0], y: bodypart.nodes[1] });
        // The above line positions the 
        // bodypart at the nodes position, under the finger.
        
        // Logic for detecting if it is close 
        // to another node, thus connecting it to the body:
      },
      onPanResponderMove: Animated.event(
        [
          null,
          { dx: pan.x, dy: pan.y }
        ],
        { useNativeDriver: false }
      ),
      onPanResponderRelease: () => {
        setIsDragging(false);
        // Revert the component to its original position
        pan.flattenOffset();
      }
    })
  ).current;

  return (
    <View style={{ flex: 1 }}>
      <Animated.View
        style={[
          {
            transform: [{ translateX: pan.x }, { translateY: pan.y }]
          },
          isDragging && { opacity: 0.8 }
        ]}
        {...panResponder.panHandlers}
      >
        {/* Your component content */}
      </Animated.View>
    </View>
  );
};
```

Now it can be rendered inside the parent, component, which will be the `LockerRoom`.
```tsx
const LockerRoom = () => {
  return (
    <View style={{ flex: 1 }}>
      {/* Other components */}
      <ListBodyPart/>
    </View>
  );
};
```

-- end comment --

Now we need to figure out how to render each body part in the list, enabling the user to choose **different categories**, such as Body, arm, legs, etc. the planned UI can be seen below.
![[Pasted image 20231018220644.png]]
To achieve this, we will have a `ScrollList` component holding all the displayed `BodyParts` with the selected condition. And the `ScrollList` will have a for loop, looping over a `useState` variable, holding all the displayed body parts (type: `BodyPart`) inside, and when the user switches conditions, a function will be called, changing the variable holding the desired body parts to be displayed. As seen below:

```tsx
// LockerRoom.tsx
...
const [displayBodyParts, setDisplayBodyParts] = useState<BodyPart[]>([]);

const categories = [
	'Bodys', 'Heads', 'Arms', 'Legs'
] as const;
type Categories = typeof afoo[number]
 
// Function when conditions are pressed
const categoryClick = (category: Categories) => {
	// Clearing the current array
	setDisplayBodyParts([]);
	// Getting all bodyparts, given the category, 
	// and updating the displayBodyParts array.
	displayBodyParts.filter((bodyPart: BodyPart) => 
		bodyPart.category === category)
		.map((bodyPart: BodyPart) => {
			setDisplayBodyParts([..., bodyPart])	
	});
}

const removeItem = (bodyPartToRemove: BodyPart) => {
	setDisplayBodyParts(displayBodyParts.filter(bodyPart => bodyPart !== bodyPartToRemove));
}

CategoryClick('Bodys'); // Calling function to actually show the bodyparts

return (
	<View>
		<Button 
			onPress={categoryClick('Heads')}>
			Head
		</Button>
	</View>
	<ScrollList> { 
			displayBodyParts.map((bodyPart) => {
				return (
					<ListBodyPart bodypart={bodyPart} RemoveSelf={removeItem(bodyPart)}/>
				)
			})
		}
	</ScrollList>
)
```

Now we need a way of checking if the body part the user is currently hovering, is within an `nodeThreshold` distance from a body node. We need to update the `Body` class in the `global.ts` file:

```tsx
const nodeOffset: number = 30;
// The distance the `room` component inside `App.tsx` is from the View Port top.
const nodeOffset: number = 150;

export class Body {
  bodypartnodes: IBodyPartNodes;
  bodypartnodesRelToViewport: IBodyPartNodes;
  nodes: IBodyNodes;
  width: number;
  height: number;
  bodyImage: ImageSourcePropType | undefined;
  transforms: ITransforms;
  
  constructor(bodypartnodes: IBodyPartNodes = emptyBodyPartNodes, nodes: IBodyNodes = emptyNodes, dimensions: Array<number>, transforms: ITransforms, bodyImage: ImageSourcePropType | undefined) {
	    this.bodypartnodes = bodypartnodes;
	    this.bodypartnodesRelToViewport = 
		    addOffset(this.bodypartnodes, nodeOffset);   
	    this.nodes = nodes;
	    this.bodyImage = bodyImage;
	    this.width = dimensions[0];
	    this.height = dimensions[1];
	    this.transforms = transforms;
    }

	private addOffset(nodes: IBodyPartNodes,
	 offset: number): IBodyPartNodes {
		let newObject: IBodyPartNodes= {... nodes};
		for(let key in newObject){
			if(newObject[key] && newObject[key].length>1){
				newObject[key][1] += offset;
			}
		}
		return newObject;
	}
}
```
Now inside the `ListBodyPart` component, within the event handler, we can check if the *body part* that the user is dragging is within `nodeThreshold` distance from the node. Additionally we will add a prop, `RemoveSelf: Callback` which will be declared in the `LockerRoom.tsx` component, and passed into each component to remove itself from the `ScrollList`:

```tsx
import { nodeThreshold } from './global.ts';

type Props: {
	bodypart: BodyPart,
	RemoveSelf: Callback,
}

...

const { monster, monsterDispatch } = useContext(MonsterContext);

onPanResponderGrant: () => {
	setIsDragging(true);
	// Set the initial position of the 
	// component to the finger position
	if (!withinThreshold[0]) {
		pan.setOffset({
		  x: pan.x._value,
		  y: pan.y._value
		});
		pan.setValue({ x: bodypart.nodes[0], y: bodypart.nodes[1] });
	} else {
		pan.setValue({ x: withinThreshhold[1][0], y: withinThreshhold[1][1] });
	}
	// The above line positions the 
	// bodypart at the nodes position, under the finger.	
	// Logic for detecting if it is close 
	// to another node, thus connecting it to the body:
	monster.monsterBody.bodypartnodesRelToViewport.map((node) => {
		for (nx = 0; nx <= nodeThreshold; nx++) { // x-axis
			for (ny = 0; ny <= nodeThreshold; ny++) { // y-axis
				// Checking if dragged bodypart is within 
				// threshold for each x and y value within threshold
				if (x === nx && y === ny) {
					setWithinThreshold([true, node]);
				} else {
					setWithinThreshold([false, undefined]);
				}
			}	
		}
	});
},
onPanResponderRelease: () => {
	if (!withinThreshold[0]) {
		setIsDragging(false);
		// Revert the component to its original position
		pan.flattenOffset();
	} else {
		RemoveSelf();
	}
}
...
```

I have the above configuration for a drag and drop item, however when it drags, it goes below 
How to get 


import React, { useState, useRef, useEffect, Ref, RefObject } from "react";

import {

  View,

  Image,

  Text,

  ImageSourcePropType,

  StyleSheet,

  findNodeHandle,

} from "react-native";

import { theme, Body, bodyPartInfo, bodysInfo } from "../global";

import node from "../assets/resources/Monsters/1/Nodenode.png";

import {

  GestureHandlerRootView,

  TouchableOpacity,

} from "react-native-gesture-handler";

  

interface Props {

  monsterBody: Body;

  mood: string;

  scaleFactor: number;

}

  

const Monster = ({ monsterBody, mood, scaleFactor = 0.3 }: Props) => {

  const leftArmRef = useRef();

  const rightArmRef = useRef();

  const leftLegRef = useRef();

  const rightLegRef = useRef();

  const eyesRef = useRef();

  const mouthRef = useRef();

  

  monsterBody.bodypartnodes.leftarm.ref = leftArmRef;

  monsterBody.bodypartnodes.rightarm.ref = rightArmRef;

  monsterBody.bodypartnodes.leftleg.ref = leftLegRef;

  monsterBody.bodypartnodes.rightleg.ref = rightLegRef;

  monsterBody.bodypartnodes.eyes.ref = eyesRef;

  monsterBody.bodypartnodes.mouth.ref = mouthRef;

  

  function checkBodyPart(part: string): boolean {

    return (

      part === "leftarm" ||

      part === "rightarm" ||

      part === "leftleg" ||

      part === "rightleg" ||

      part === "eyes" ||

      part === "head" ||

      part === "mouth"

    );

  }

  

  useEffect(() => {

    let i: number = 0;

    Object.values(monsterBody.bodypartnodes).map((bodypart: bodyPartInfo) => {

      if (

        bodypart !== undefined &&

        bodypart.ref !== undefined &&

        bodypart.ref !== null &&

        bodypart.bodyPart.node !== undefined &&

        typeof bodypart.ref === "object" &&

        bodypart.ref.current !== undefined

      ) {

        // if (checkBodyPart(potentialTitle)) {

        // }

        // Returning an array of the all the bodypart titles, as to match it with the current bodypart, and then finds the corresponding node that it should attach to on the body.

        const partTitle = Object.keys(bodysInfo[1].bodyparts)[i] as

          | "leftarm"

          | "rightarm"

          | "leftleg"

          | "rightleg"

          | "eyes"

          | "head"

          | "mouth";

  

        const node = bodysInfo[1].body[partTitle];

        const bodyNodeCoord: Array<number> = node !== undefined ? node : [0, 0];

  

        // bodypart.ref.current.setNativeProps({

        //   style: {

        //     transform: [

        //       {

        //         translateX:

        //           bodyNodeCoord[0] - 35 - bodypart.bodyPart.node[0] * 1,

        //       },

        //       {

        //         translateY:

        //           bodyNodeCoord[1] * 1 - bodypart.bodyPart.node[1] * 1,

        //       },

        //       { scaleX: bodypart.bodyPart.reflected ? -1 : 1 },

        //       {

        //         scale:

        //           bodypart.bodyPart.node[2] !== undefined

        //             ? bodypart.bodyPart.node[2]

        //             : 1,

        //       },

        //     ],

        //     width: bodypart.bodyPart.width,

        //     height: bodypart.bodyPart.height,

        //     zIndex: bodypart.bodyPart.zIndex,

        //   },

        // });

      }

      i++;

    });

  }, [monsterBody]);

  

  return (

    <View style={styles.room}>

        <View style={styles.body}>

          {monsterBody.bodyImage ? (

            <Image

              style={[

                styles.bodyImage,

                {

                  width: monsterBody.width * scaleFactor,

                  height: monsterBody.height * scaleFactor,

                  transform: [

                    { translateX: monsterBody.transforms.x * scaleFactor },

                    { translateY: monsterBody.transforms.y * scaleFactor },

                    { scale: monsterBody.transforms.scale },

                  ],

                },

              ]}

              source={monsterBody.bodyImage}

            />

          ) : null }

          {Object.values(monsterBody.bodypartnodes).map(

            (bodypart: bodyPartInfo, i: number) => {

              const partTitle = Object.keys(bodysInfo[1].bodyparts)[i] as

                | "leftarm"

                | "rightarm"

                | "leftleg"

                | "rightleg"

                | "eyes"

                | "head"

                | "mouth";

              const node = bodysInfo[1].body[partTitle];

              const bodyNodeCoord: Array<number> =

                node !== undefined ? node : [0, 0];

              if (bodypart)

                return (

                  <TouchableOpacity

                    style={[

                      styles.gestureHandler,

                      {

                        transform: [

                          {

                            translateX:

                              bodyNodeCoord[0] -

                              35 -

                              bodypart.bodyPart.node[0] * 1,

                          },

                          {

                            translateY:

                              bodyNodeCoord[1] * 1 -

                              bodypart.bodyPart.node[1] * 1,

                          },

                          { scaleX: bodypart.bodyPart.reflected ? -1 : 1 },

                          {

                            scale:

                              bodypart.bodyPart.node[2] !== undefined

                                ? bodypart.bodyPart.node[2]

                                : 1,

                          },

                        ],

                        width: bodypart.bodyPart.width,

                        height: bodypart.bodyPart.height,

                        zIndex: bodypart.bodyPart.zIndex,

                      },

                    ]}

                    onPress={() => {

                      // Executes the onPress function if it exists

                      if (bodypart.onPress != null)

                        bodypart.onPress(bodypart.bodyPart);

                      else {

                        return;

                      }

                    }}

                  >

                    <Image

                      ref={bodypart.ref}

                      style={styles.bodyPart}

                      source={bodypart.bodyPart.image}

                    />

                  </TouchableOpacity>

                );

              else return;

            }

          )}

        </View>

    </View>

  );

};

  

const styles = StyleSheet.create({

  bodyPart: {

    backgroundColor: "transparent",

    position: "absolute",

  },

  room: {

    height: "100%",

    flex: 1,

    justifyContent: 'center',

    alignContent: 'center',

    marginTop: 'auto',

  },

  body: {

    width: "100%",

    height: "100%",

    flex: 1,

  },

  bodyImage: {

    height: "100%",

    width: "100%",

  },

  gestureHandler: {

    height: "100%",

    width: "100%",

  },

  touchable: {

    backgroundColor: "black",

    width: "auto",

    height: 20,

    justifyContent: "center",

    alignItems: "center",

  },

});

  

export default Monster;