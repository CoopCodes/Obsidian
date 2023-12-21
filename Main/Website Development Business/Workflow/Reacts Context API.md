---
tags:
  - FrontEnd
---

*A more efficient and maintainable way to pass data to all components in a react app using **the context API***
- In the typical react app dataflow, components pass data through props.
![[Pasted image 20230830182532.png]]
- When a component nested several layers down, needs to access data from a grand-parent component, you traditionally would pass a prop down every component layer to the child. 
- This is called **Prop drilling** - The cascade of props that get data to parts of the React Component Tree.

**React Context API** - *Provides a way to pass data down to components without having to pass props manually at every level*;

# Example
A simple login application, where when you enter your username and password, it displays the username, 
![[Pasted image 20230830183630.png]]
```javascript
...
const [username, setUsername] = useState("");
const [showProfile, setShowProfile] = useState(false);
return (
	<input 
		type="text"
		placeholder="username..."
		onChange={(event) => {
			setUsername(event.target.value);
		}}
	/>
	<input type="text" placeholder="password..."/>
	<button onClick={() => {
		setShowProfile(true)
	}}>LOGIN</button>
	{showProfile && <h1>{username}</h1>}
)
```
- If we want to create a new profile page, and pass in the username, we can do this with **Reacts Context API**
- Create a profile component:
```javascript
...
return (
	<>
		<h1>Profile</h1>
		<h2>Username: </h2>
)
```
- Move the `showProfile` state to the main *App* component:
![[Pasted image 20230830184444.png]]
- Create a *Context* folder, and a *LoginContext.js* file inside:
![[Pasted image 20230830184617.png]]
Inside the file:
```javascript
import { createContext } from 'react';

export const LoginContext = createContext({}) // This creates the context
```

Now inside the parent component of both the *Login* page and the *Profile* component, (The *App* component).
```javascript
import { LoginContext } from './Contexts/LoginContext';
// Now you wrap the components that you wish to use the state in the LoginContext:
...
const [showProfile, setShowProfile] = useState(false);
const [username, setUsername] = useState("");
return (
	<LoginContext.Provider value={ username, setUsername }> // value?={**List of objects/states that you are wanting the children to access**}
		{ showProfile ? <Profile/> : <Login/> }
	</LoginContext.Provider>	
)
```
Now inside the children, *Login.js* we can import `useContext`:
```javascript
import React, { useState, useContext } from "react";
import { LoginContext } from './Context/LoginContext'

function Login() {
	const { setUsername } = useContext(LoginContext); 
	// This grabs the setUsername state from the object passed into the LoginContext provider
	...
}
```
Now when we run the project, and enter a username:
![[Pasted image 20230830185950.png]]
And press the login button:
![[Pasted image 20230830190015.png]]
It keeps track of the username, and since the `showProfile` state changed, it removed the `Login.js` component, and showed the `Profile.js`  component.