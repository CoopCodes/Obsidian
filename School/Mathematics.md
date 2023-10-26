---
tags:
  - "#mathematics"
---
Find $f'(x)$ where $f(x)=\frac{1}{x-1}$ using first principles, specifically the formula:
$$\frac{f(x+h)-f(x)}{h}$$


<hr class="__chatgpt_plugin">

role::assistant

To find $f'(x)$ using first principles, we need to evaluate the limit of the difference quotient as $h$ approaches $0$. 

First, let's find $f(x+h)$:
$$f(x+h) = \frac{1}{x+h-1}$$

Now, let's substitute $f(x+h)$ and $f(x)$ into the difference quotient formula:
$$\frac{f(x+h)-f(x)}{h} = \frac{\frac{1}{x+h-1}-\frac{1}{x-1}}{h}$$

To simplify this expression, we need to find a common denominator:
$$\frac{\frac{1}{x+h-1}-\frac{1}{x-1}}{h} = \frac{(x-1)-(x+h-1)}{(x+h-1)(x-1)h}$$

Simplifying the numerator:
$$\frac{(x-1)-(x+h-1)}{(x+h-1)(x-1)h} = \frac{x-1-x-h+1}{(x+h-1)(x-1)h} = \frac{-h}{(x+h-1)(x-1)h}$$

Canceling out the $h$ in the numerator and denominator:
$$\frac{-h}{(x+h-1)(x-1)h} = \frac{-1}{(x+h-1)(x-1)}$$

Now, we can take the limit as $h$ approaches $0$:
$$\lim_{h \to 0} \frac{-1}{(x+h-1)(x-1)}$$

Since the limit does not depend on $h$, we can substitute $h=0$:
$$\frac{-1}{(x+0-1)(x-1)} = \frac{-1}{(x-1)^2}$$

Therefore, $f'(x) = \frac{-1}{(x-1)^2}$.

<hr class="__chatgpt_plugin">

role::user

