
How do i check if a variable is `"leftarm" | "rightarm" | "leftleg" | "rightleg" | "eyes" | "head" | "mouth"` in typescript?

<hr class="__chatgpt_plugin">

role::assistant

In TypeScript, you can use the `typeof` operator along with the `===` operator to check if a variable is one of the specified values. Here's an example:

```typescript
function checkBodyPart(part: string): boolean {
  return part === "leftarm" || part === "rightarm" || part === "leftleg" || part === "rightleg" || part === "eyes" || part === "head" || part === "mouth";
}

// Example usage
const bodyPart = "leftarm";
if (checkBodyPart(bodyPart)) {
  console.log("Valid body part");
} else {
  console.log("Invalid body part");
}
```

In the above code, the `checkBodyPart` function takes a `part` parameter and checks if it matches any of the specified values using multiple `===` comparisons. If the `part` matches any of the values, it returns `true`, indicating that it is a valid body part. Otherwise, it returns `false`.

<hr class="__chatgpt_plugin">

role::user

