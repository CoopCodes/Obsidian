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

This can be implemented by creating a `bodypart` component, that will be rendered in a list of all the body parts that the user can choose:

```tsx
interface Props {
	bodypart: BodyPart,
}

const ListBodyPart = ({ bodypart: BodyPart }: Props, => {
  const pan = useRef(new Animated.ValueXY()).current;
  const [isDragging, setIsDragging] = useState(false);

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

Now we need to figure out how to render each body part in the list, enabling the user to choose **different categories**, such as Body, arm, legs, etc. the planned UI can be seen below.
![[Pasted image 20231018220644.png]]
To achieve this, we will have a `ScrollView` component holding all the displayed `BodyParts` with the selected condition. And the `ScrollView` will have a for loop, looping over a `useState` variable, holding all the displayed body parts (type: `BodyPart`) inside, and when the user switches conditions, a function will be called, changing the variable holding the desired body parts to be displayed. As seen below:

```tsx
...
const [displayBodyParts, setDisplayBodyParts] = useState<>([]);

const categories = [
	'Bodys', 'Heads', 'Arms', 'Legs'
] as const;
type Categories = typeof categories[number]
 
// Function when conditions are pressed
const CategoryClick = (category: Categories) => {
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

CategoryClick('Bodys'); // Calling function to actually show the bodyparts

return (
	<View>
		<Button 
			onPress={CategoryClick('Heads')}>
			Head
		</Button>
	</View>
	<ScrollView> { 
			displayBodyParts.map((bodyPart) => {
				return (
					<ListBodyPart bodypart={bodyPart}/>
				)
			})
		}
	</ScrollView>
)
```

Now we need a way of checking if the body part the user is currently hovering, is within an `nodeThreshold` distance from a body node. We need to update the `Body` class in the `global.ts` file:

```tsx
// The distance the `room` component inside `App.tsx` is from the View Port top.
const roomDistanceFromVPTop: number = 150;

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
    
    this.nodes = nodes;
    this.bodyImage = bodyImage;
    this.width = dimensions[0];
    this.height = dimensions[1];
    this.transforms = transforms;
  }
}
```