---
backlinks:
  - "[[Reacts Context API]]"
tags:
  - FrontEnd
---
___
# Hooks
- Manage states and rendering of UI when state changes.
- Provide access to your app's context
- Update components with an alternative to lifecycle methods.


## `useState`

- The most useful hook, it allows you to use react state in a function component.
```jsx
import React, { useState } from 'react';
function App() {
  const [ score, setScore ] = useState(0); // [0, ƒ]
  ...
}
```
- This creates a live variable, where you can access the variable with the `score` variable, and set the variable with `setScore`, the `useState()` function takes in a parameter, which is the initial value for the variable.

```jsx
// Accessing the state
import React, { useState } from 'react';
function App() {
  const [ score, setScore ] = useState(0);
  return <h1>{ score }</h1>;
}
```
- You can now access the variable.

```jsx
function App() {
  const [score, setScore] = useState(0);
  return (    
	<div className="App">      
		<header className="App-header">        
			<h1>{ score }</h1>
			<button onClick={() => \
				  setScore(score + 1)}> 
			      // Set the score + 1
			</button>
		</header>
		</div>  
	);
}
```
- When setting the state, you cannot use operations such as `variable += 1`, or `variable.push(foo)` you must set it `setVariable(variable + 1)`, or `setVariableList([...variableList, foo])`.

## `useEffect`
- [x] Completed?
	- [x] Content Finished?
	- [x] Quiz

- Using this function performs a *side effect*.
- The first parameter receives a *callback*, a function. Where you can perform any side effects.
```jsx
// The effect happens after render
useEffect(() => {    
	console.log('useEffect called!');  
}, []);
```
- The hook instructs React to do *something* after render, so it's called when the component first renders and after each subsequent re-render or update. If you run the code, '*useEffect called*' will be immediately be printed in the console. And it gets printed each time the `score` state changes.
- The second parameter is a list of *states* or *dependecies* that are usually used inside the *useEffect* function. For example:
```jsx
useEffect(() => {
	console.log(variableState);
}, [variableState])
```
- This means that instead of the callback running after every render, or state change, it will only run if the *useState* `variableState` has changed. This can increase performance.
- Again, passing `useEffect` an empty array as the second argument ensures that it runs only once after the component's initial render. In some cases, omitting the second array argument causes `useEffect()` to execute in an infinite loop, endlessly fetching data. This happens because you're modifying the component's state inside `useEffect()`, which triggers the effect again and again.
## Quiz: 
- [x] What is the first parameter of the *useEffect* hook? **A callback, that will be ran after the page renders**
- [x] What is the purpose of the `useEffect` hook in React? **To run a function after the page renders, this is useful for setInterval function, and fetching APIs, where there could be a possible delay, that could stop the page from rendering immediantly.**
- [x] How does the `useEffect` hook differ from other lifecycle methods in React? **It runs after the page loads**
- [x] What is the second parameter of the `useEffect` hook used for? **It is an array of UseState variables, and it tells the function to only run IF the variables have changed. It is also called dependencies.**
- [x] How can you ensure that the `useEffect` hook only runs once after the component's initial render? **By Entering an empty array `[]`**
- [x] What happens if you omit the second parameter of the `useEffect` hook? **React will throw an error** 
	<span style="color:red; font-weight: bold; text-decoration: none;">^Incorrect: If you omit the second parameter, the `useEffect` hook will run after every render, not just once after the component's initial render.</span>
- [x] Can you have multiple `useEffect` hooks in a single component? **Yes**
- [x] Can you use the `useState` hook inside the `useEffect` hook? **Yes**
- [x] How can you clean up side effects in the `useEffect` hook? **It does it automatically**
- [x] Can you use async/await inside the `useEffect` hook? **Yes**
- [x] How does the `useEffect` hook help with performance optimization? **It automates the mounting and unmounting of react**
### Quiz marks:
Format: `Q{question number}: **{mark (correct/incorrect)}**. {if incorrect, give reasoning}.
Q1: correct.
Q2: correct.
Q3: correct.
Q4: correct.
Q5: correct.
Q6: incorrect. If you omit the second parameter, the `useEffect` hook will run after every render, not just once after the component's initial render.
Q7: correct.
Q8: correct.
Q9: correct.
Q10: correct.
Q11: correct.

<hr class="__chatgpt_plugin">


# Demonstrating Project
*This project will demonstrate the use of `useState` and `useEffect` hooks by creating a GIF searcher, by contacting the Giphy API.*

## Declare the GIF Data State
- *Import the needed dependencies*:
```jsx
import React, { useState, useEffect } from 'react';
```

- Declare a `data` state and `setData` function to update the state. And set the default value to an empty array `[]`
```jsx
function App() {
	const [data, setData] = useState([]); // Declare state

	return (
		<>
			<div className="main-header">
				<div className="inner">
					<h1 className="main-title">GifSearch</h1>
					<SearchForm />
				</div>
			</div>
			<div className="main-content"></div>
		</>	
	)
}
```

- in the return statement, render the `GifList` component and pass it the `data` state.
```jsx
...
<div className="main-content">
	<GifList data={data}/>
</div>
```

## Fetch Data from the Giphy API
*When the `App` component renders, it should make a request to the Giphy API and display a set of gifs. We'll use axios to fetch the GIF data.*
- Create a `useEffect` hook, and use axios to retrieve the data.
```jsx
function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
      axios(`http://api.giphy.com/v1/gifs/search?
      q=${query}&limit=24&api_key=YOUR_API_KEY`)
	  .then(response => setData(response.data.data))
	  .catch(error => console.log('Error fetching and parsing data', error));
  }, []);
  return (...);
}
```

# Other hooks
There are a couple React Hooks apart from *useState, useEffect, and useContext*:
### `useReducer`
This hook allows you to manage state with a reducer function. It returns an array with the current state and a dispatch function to update it. **Similar to the useState hook.
`useReducer(<reducer>, <initialState>)`
The `reducer` function contains your custom state logic and the `initialState` can be simple value but generally with contain an object
The `useReducer` hook returns the current `state` and `dispatch` method

**Here is a simple example using `useState`, and then using `useReducer`:**
```jsx
function Counter({initialCount}) {
  const [count, setCount] = useState(initialCount);
  return (
    <>
      Count: {count}
      <button onClick={() => setCount(initialCount)}>Reset</button>
      <button onClick={() => setCount(prevCount => prevCount - 1)}>-</button>
      <button onClick={() => setCount(prevCount => prevCount + 1)}>+</button>
    </>
  );
}
```
- In this snippet a `useState` state is created to hold an integer, and it is incremented every time the *add* button is pressed, and decreased using the opposite button.
**Here's how it would be done using the `useReducer` hook:**
```jsx
const initialState = {count: 0};

function reducer(state, action) {
  switch (action.type) { 
  // Switch statement for whether action.type === 'decrement' | 'increment'
    case 'increment':
      return {count: state.count + 1};
    case 'decrement':
      return {count: state.count - 1};
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      Count: {state.count}
      <button onClick={() => dispatch({type: 'decrement'})}>-</button>
      <button onClick={() => dispatch({type: 'increment'})}>+</button>
    </>
  );
}
```
- This can be useful for more complex objects, where logic is having to be used.

### `useCallback`
This hook runs a callback when 1 or more `useState` dependencies change.
``useCallback(<callback>, <dependencies>);``
Example:
```jsx
const [randomState, setRandomState] = useState("something random?");

const memoizedCallback = useCallback(
	() => {
		console.log(randomState);
	},
	[randomState]
);
```
This sets `memoizedCallback` to the function, which was `console.log(randomState)`, so you could call the function with `memoizedCallBack()`


## `useRef`
- This hooks allows you to create a **reference** to a specific DOM element in your application. This reference can be used to manipulate the element's properties and values.
- For example, if you have a form with an input field, you can use the hook to create a reference to that input field. You can then use this reference to get the current value of the input field or change its value programmatically. Here's how to implement this:
```jsx
const inputRef = useRef(null); 

const handleSumbit = (event) => {
	event.preventDefault();
	console.log(inputRef.current.value)
}

return (
	<form onSubmit={handleSubmit}>
		<label>
			<input type="text" ref={inputRef}/>
		</label>
		<button type="submit">Submit</button>
	</form>
)
```

How do i transform an image using `useRef` in react native?

<hr class="__chatgpt_plugin">

role::assistant

In React Native, you can use the `useRef` hook to transform an image by accessing its `style` property. Here's an example:

```jsx
import React, { useRef } from 'react';
import { View, Image } from 'react-native';

const App = () => {
  const imageRef = useRef(null);

  const handleTransform = () => {
    imageRef.current.setNativeProps({
      style: {
        transform: [
          { rotate: '45deg' },
          { scale: 2 },
          { translateX: 100 },
          { translateY: 100 },
        ],
      },
    });
  };

  return (
    <View>
      <Image
        ref={imageRef}
        source={require('./path/to/image.png')}
        style={{ width: 200, height: 200 }}
      />
      <Button title="Transform" onPress={handleTransform} />
    </View>
  );
};

export default App;
```

In this example, we create a `ref` using the `useRef` hook and assign it to the `Image` component. We then define a `handleTransform` function that uses the `setNativeProps` method to update the `style` property of the image. We can apply various transformations such as rotation, scaling, translation, etc. by modifying the `transform` property.

When the "Transform" button is pressed, the `handleTransform` function is called, and the image will be transformed according to the specified properties.

Note: Make sure to import the necessary components (`View`, `Image`, `Button`) from the `react-native` package.

<hr class="__chatgpt_plugin">

role::user

