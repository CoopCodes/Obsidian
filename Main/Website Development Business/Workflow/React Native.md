---
backlinks:
  - "[[Todo App]]"
  - "[[Drag & Drop]]"
  - "[[React Native Navigation]]"
---
___
[]
# Views, Text
- View: A view is like a div element in normal react to wrap different elements.
- Text: This element has to be used when outputting text, or else an error will be thrown.
```jsx
<View style={styles.container}>
	<Text>Open up App.js to start working on your app</Text>
<View>
```

# Text inputs
- By default the `TextInput` prop doesn't have any styling, so to get a border and other things, you have to use styled components to make one.
- In order to get a function to run every time the text changes in the input, you can do: `<TextInput onChangeText={foo()}/>`. Foo will have a parameter of `val` and this is the value of what the user typed in the input.
- You can change the type of keyboard for the user to have with `keyboardType='numeric'`

# Lists
- When having a list of different elements, objects, react requires that there be a `key` key inside the object, so it can keep track. The key will be passed in as a prop, so the key could just be the index of the object in the list.
```jsx
const [people, setPeople] = useState([
	{ name: 'shaun', key: '1' },
	...
])

return (
	<View>
		{ people.map((item) => {
			return (
				<View key={item.key}> // pass the key as a prop
					<Text>{item.name}</Text>
				</View>
			)
		})}
	</View>
)
```

![[Pasted image 20230904150000.png]]
Now the users need to be able to scroll, we can do this by replacing the `View` component with a `ScrollView` component, to enable users to scroll.

## FlatList
- Another way to output a list.
- Using `FlatList` to output lists disables the need to pass the `key` property as a prop, you only need to have the key in the object.
```jsx
{ name: 'shaun', key: '1' }
```

```jsx
...
return (
	<FlatList
		data={people} // Enter an array of data
		renderItem={({ item }) => ( // destructuring the 'people' object
			// return some jsx
			<Text>{item.name}</Text>
		)}
	/>
)
```
-  Using `FlatList` is better for performance, as it *lazy loads* the items, this can be useful for lists with over 100 items.
- If the object has a different name for `key`, for example `id` you can do the following:
```jsx
const people = [{ name: 'shaun', id: '1' }]
```

```jsx
...
return (
	<FlatList
		keyExtractor={(item) => item.id} // A function that returns the property in the object that is the key.
		data={people} // Enter an array of data
		renderItem={({ item }) => ( // destructuring the 'people' object
			// return some jsx
			<Text>{item.name}</Text>
		)}
	/>
)
```

- You can also pass an optional prop `numColumns`, and this, as the title says, changes the number of columns in the list.
```jsx
...
return (
	<FlatList
		numColumns={2}
		keyExtractor={(item) => item.id} 
		data={people} // Enter an array of data
		renderItem={({ item }) => ( // destructuring the 'people' object
			// return some jsx
			<Text>{item.name}</Text>
		)}
	/>
)
```

# Touchable Components
- In the above example, there is a list of items, now we want to make them interactive.
```jsx
import { TouchableOpacity } from 'react-native'
```

- Now you can surround any component that you want to be touchable with the `TouchableOpacity` component.
- To get an `OnPress` event, you can simply link a function.
```jsx
const pressHandler = (id) => {
	setPeople((prevPeople) => { 
		return prevPeople.filter(person => person.id != id)
	})
}

...
return (
	...
	<TouchableOpacity onPress={() => { pressHandler(item.id) }}>
		<Text>{ item.name }</Text>
	</TouchableOpacity>
)
```

# Alerts
- Alerts are helpful for telling the user they are doing something wrong, or alerting that there has been an error.
`Alert.alert(<alert title>: string, <message>: string, <buttons>: array[Dictionary<text: string, onPress: eventHandler])`

```jsx
import ( Alert ) from 'react/native';
```

```jsx
Alert.alert(
	'OOPS',
	'Todos must be over 3 chars long', [
		{ text: 'Understood', onPress: () => console.log('alert closed') }
	]
)
```

# Dismissing keyboard
- **Dismissing the keyboard when the keyboard is up, but user presses on something that is not the keyboard**
- Wrap the whole application in a `TouchableComponent`, specifically the `TouchableWithoutFeedback` component

```jsx
import { TouchableWithoutFeedback, Keyboard }
```

```jsx
return (
	<TouchableWithoutFeedback>
		<View>
			...
		</View>
	</TouchableWithoutFeedback>
)
```

Now we can setup the `onPress` handler to dismiss the keyboard.
```jsx
function dismissKeyboard() {
	Keyboard.dismiss();
	console.log('Dismissed keyboard');
}

return (
	<TouchableWithoutFeedback onPress={dismissKeyboard}>
		<View>
			...
		</View>
	</TouchableWithoutFeedback>
)
```

$$\frac{1}{1}$$