# Implementing in React
*This can be implemented by creating a `useReducer` state variable for each monster Attribute, and then creating a `ContextAPI` object to pass it to all components who need to access it.*
```tsx
'''App.tsx'''
...
const attributesInitial = {
	health: 100,
	hunger: 100,
	happiness: 100,
	energy: 100,
}

const reducer = (state, action) => {
		const updatedAttribute = eval(
		``${attributesInitial[action.attribute]
		${action.operation} ${action.perk}`` 
		) 
		// The above adds/subtracts the initial value of the attribute,
		// to the additor. For example, "100 - 1". This would be run every 
		// so often, to slowly decrease the hunger attribute for example.
		
		if (action.attribute === 'health') {
			// Here we can add checkpoints to change the monsters appearance
			if (action.attribute <= 100 && action.attribute > 60) {
				// Do something
			}
		} // This can continue for all/any other attributes
		
		return updatedAttribute;
	}
}

const [attributes, attributesDispatch] = useReducer(reducer, attributesInitial)

```

Now we can create a new file named `./Contexts/AttributesContext.ts` and inside:
```tsx
import { createContext } from 'react';

export const AttributeContext = createContext({}) // This creates the context, and in other components state variables can be added to this context.
```

Now inside the `App.tsx` file:
```tsx
'''App.tsx'''
import { LoginContext } from './Contexts/AttributesContext.ts';

...
const attributesInitial = {
	health: 100,
	hunger: 100,
	happiness: 100,
	energy: 100,
}

const reducer = (state, action) => {
		// action.attribute, action.operator, action.perk
		const updatedAttribute = eval(
		``${attributesInitial[action.attribute]
		${action.operation} ${action.perk}`` 
		) 
		// The above adds/subtracts the initial value of the attribute,
		// to the additor. For example, "100 - 1". This would be run every 
		// so often, to slowly decrease the hunger attribute for example.
		
		if (action.attribute === 'health') {
			// Here we can add checkpoints to change the monsters appearance
			if (action.attribute <= 100 && action.attribute > 60) {
				// Do something
			}
		} // This can continue for all/any other attributes
		
		return updatedAttribute;
	}
}

const [attributes, attributesDispatch] = useReducer(reducer, attributesInitial)

return (
	...
	<LoginContext.Provider value={ attributes }> {/* 
		This passes the LoginContext to the children
		with the 'attributes' useReducer state.
	*/}
		... (all rooms)
	</LoginContext.Provider>
)
```

To set an attribute:
```tsx
attributesDispatch({ 'hunger', '+', 5 })
```
This adds 5 to hunger. And would be when the user feeds the monster.

## Implementing Attributes to the main App Component
The whole application will be wrapped in the main App component, this component will contain all the global variables. **And will contain the attribute values** so that no-matter what room the user is in, it is visible.
```tsx
'''App.tsx'''
import { LoginContext } from './Contexts/AttributesContext.ts';

...
const attributesInitial = {
	health: 100,
	hunger: 100,
	happiness: 100,
	energy: 100,
}

const reducer = (state, action) => {
		const updatedAttribute = eval(
		``${attributesInitial[action.attribute]
		${action.operation} ${action.perk}`` 
		) 
		// The above adds/subtracts the initial value of the attribute,
		// to the additor. For example, "100 - 1". This would be run every 
		// so often, to slowly decrease the hunger attribute for example.
		
		if (action.attribute === 'health') {
			// Here we can add checkpoints to change the monsters appearance
			if (action.attribute <= 100 && action.attribute > 60) {
				// Do something
			}
		} // This can continue for all/any other attributes
		
		return updatedAttribute;
	}
}

const [attributes, attributesDispatch] = useReducer(reducer, attributesInitial)

return (
	<Attributes className="attributes">
          <Attribute 
	          attrName="health" 
	          imagePath='./resources/images/heart.png'
	          progress={attributes.health}/>
	          ... Rest of the attributes
    </Attributes>
	
	<LoginContext.Provider value={ attributes }> {/* 
		This passes the LoginContext to the children
		with the 'attributes' useReducer state.
	*/}
		... (all rooms)
	</LoginContext.Provider>
)
```

