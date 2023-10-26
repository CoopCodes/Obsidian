**Implementing a Drag and Drop `FlatList` in react native**

```tsx
<View>
	<FlatList 
		data={data}
		renderItem={({ item }) => (
			<View>
				<Text>@</Text> // This is the handle, where you will grab it and reorder the list
			</View>
			<Text>{ item }</Text> // Just a random number
		)}> // This will be the list that will be reordered
</View>
```

## `PanResponder` <span style="font-weight: 500; font-size: 1.5rem;">This is used to create event listeners for finger on screen.</span>
```tsx
import { PanResponder } from 'react/native';
...

_panResponder: PanResponderInstance;

const panResponder = React.useRef(  
	PanResponder.create({  
		// Ask to be the responder:  
		onStartShouldSetPanResponder: (evt, gestureState) => true,  
		onStartShouldSetPanResponderCapture: (evt, gestureState) =>  
		true,  
		onMoveShouldSetPanResponder: (evt, gestureState) => true,  
		onMoveShouldSetPanResponderCapture: (evt, gestureState) =>  
		true,  
		  
		onPanResponderGrant: (evt, gestureState) => {  
			// The gesture has started. Show visual feedback so the user knows  
			// what is happening!  
			// gestureState.d{x,y} will be set to zero now  
		},  
		onPanResponderMove: (evt, gestureState) => { // This is where we can do our logic
			 console.log(gestureState)
			// The most recent move distance is gestureState.move{X,Y}  
			// The accumulated gesture distance since becoming responder is  
			// gestureState.d{x,y}  
		},  
		onPanResponderTerminationRequest: (evt, gestureState) =>  
		false,  
		onPanResponderRelease: (evt, gestureState) => {  
			// The user has released all touches while this view is the  
			// responder. This typically means a gesture has succeeded  
		},  
		onPanResponderTerminate: (evt, gestureState) => {  
			// Another component has become the responder, so this gesture  
			// should be cancelled  
		},  
		onShouldBlockNativeResponder: (evt, gestureState) => {  
			// Returns whether this component should block native components from becoming the JS  
			// responder. Returns true by default. Is currently only supported on android.  
		return true;  
		},  
	}),  
).current;
```

Now inside the top code snippet:
```tsx
<View {...this._panResponder.panHandlers}><Text>@</Text></View> // 
```

Now we can make one the of the entries to the `FlatList` follow the cursor if a user hovers:
```tsx
<Animated.View>
	<Text>Hello</Text>
</Animated.View>
```
`Animated.View` is a sort of view that is good for animations.

Create a point variable:
```tsx
let point = new Animated.ValueXY() // Gives the current cursors X and Y values
```

Mapping the cursor position to the variable
```tsx
onPanResponderMove: (evt, gestureState) => { // This is where we can do our logic
	console.log(gestureState)
	Animated.event([{y: point.y}])({y: gestureState.moveY }) \
	// ^ Mapping gestureState.moveY to the 'point' variable.
	
	// The most recent move distance is gestureState.move{X,Y}  
	// The accumulated gesture distance since becoming responder is  
	// gestureState.d{x,y}  
},  
```

Now we can set the position to the point.
```tsx
state = {
	dragging: false,
}


onPanResponderGrant: (evt, gestureState) => {  
	this.setState({ dragging: true }); 
	// The gesture has started. Show visual feedback so the user knows  
	// what is happening!  
	// gestureState.d{x,y} will be set to zero now  
},  

const renderItem = ({ item }) => (
	<View>
		<Text>@</Text> // This is the handle, where you will grab it and reorder the list
	</View>
	<Text>{ item }</Text> // Just a random number
)

...
<Animated.View style={top: point.getLayout().top}>
	{renderItem({item: 3})}
</Animated.View>

<FlatList scrollEnabled={!dragging}>
	<FlatList renderItem={renderItem}></FlatList>
</FlatList>
```