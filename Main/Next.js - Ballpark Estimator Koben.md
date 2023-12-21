---
tags:
  - FrontEnd
---
___
Back end is complete  
I need to program the front end in react, I can get started on this now. Unknown if there is a design, i will just create a basic layout with image on top.
## Question Component
### Props with references:
```tsx
type questionType: "Single-Choice" | "Multi-Choice" | "Text-Input" // This should be declared in Umbraco, this is for examples sake

interface QuestionOption {
	title: string;
	description?: string; // Text explanation of the option, can be null
	linkingQuestion?: int; // This will be the ID, and will be passed into the parent, and then into API to get the questions information
}

type GetNextQuestion(id: int): void;

interface Props {
	title: string;
	description: string;
	questionType: QuestionType;
	questionOptions: QuestionOption[];
	questionId: int,
	questionIcon: Image;
	NextQuestion: GetNextQuestion;
}
```

### Text explanation of what the component should do
The component should be able to **render** all the different types of questions, this can be implemented through an if statement looping through all the type of questions there could be, and styling it accordingly. 
It should add functionality to the component. There should be an event listener to when any of the buttons get pressed. 
The event function should take in the question information, and execute the an API call to get the next question in line. if the `linkingQuestion` parameter of the question is undefined, it should get the current `questionId` and add 1. 
If the `linkingQuestion` is not undefined, it should call the API, and enter in the `linkingQuestion` id.
It function should then call `NextQuestion` passing in the next ID, whatever that may be.

### Implementation
```tsx
function Question({ title, description, questionType, questionOptions, questionId, questionIcon, NextQuestion }: Props) {
	function getNextQuestionId(questionId: int, questionOption: QuestionOption) {
		const nextQuestionId = 0
		if (questionOption.linkingQuestion === undefined) {
			nextQuestionId = questionId + 1;
		} else {
			nextQuestionId = questionOption.linkingQuestion;
		}
		NextQuestion(nextQuestionId);
	}
	// Do the markup in another program
}
```

## BallparkEstimator Page:
### Implementation:
```tsx
const [questions, setQuestions] = useState<Question>([]);

function NextQuestion(id: int) {
	const url = `https://www.koben.dev.com.au/BallparkEstimator/id?${id}`;
	const response = await axios.get(url);
	const { question } = response.data;
	const { title, description, questionType, questionOptions, questionIcon } = question;
	setQuestions([...questions, (
		<Question 
			title={title} 
			description={description} 
			questionType={questionType} 
			questionOptions={questionOptions} 
			questionId={questionId} 
			questionIcon={questionId} 
			NextQuestion={NextQuestion}
		/>
	)])
}
```



# Questions:
- Where do i create the Ballpark estimator page?
- Where do i create components (the Question Component)?
- Do we have a design for the page?
- NPM authentication problem
- How do i get access to all the question types
    // "@fortawesome/fontawesome-pro": "^6.2.1",