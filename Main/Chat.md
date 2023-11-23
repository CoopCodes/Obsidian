Please write a simple typescript script to fetch an API of URL `https://www.koben.dev.com.au/BallparkEstimator/id?${parameter}`.
The API should return JSON in the following format:
```json
"question": {
	"title": "", // string
	"description": "", // string
	"questionType": "", // string
	"questionOptions": [{
		"title": "", // string
		"description": "", // string
		"linkingQuestion": "" // int (it is an Id)
	}],
	"questionIcon": "" // image url link
}
```

please break all of these values into their own variable in typescript.

<hr class="__chatgpt_plugin">

role::assistant

Sure! Here's a simple TypeScript script that fetches the API and breaks down the JSON response into separate variables:

```typescript
import axios from 'axios';

async function fetchAPI(parameter: string): Promise<void> {
  try {
    const url = `https://www.koben.dev.com.au/BallparkEstimator/id?${parameter}`;
    const response = await axios.get(url);

    const { question } = response.data;
    const { title, description, questionType, questionOptions, questionIcon } = question;

    console.log('Title:', title);
    console.log('Description:', description);
    console.log('Question Type:', questionType);
    console.log('Question Options:', questionOptions);
    console.log('Question Icon:', questionIcon);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Usage
const parameter = 'exampleParameter';
fetchAPI(parameter);
```

Make sure to install the `axios` package by running `npm install axios` before running the script. This script uses `axios` to make the HTTP request and handles any errors that may occur during the request.

<hr class="__chatgpt_plugin">

role::user

