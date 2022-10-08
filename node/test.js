const hello = "Hello from NODE JS Variable"
console.log(hello)

console.log(`Printing variable hello: ${hello}`);

const path = require("path");
console.log("Using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);

console.log(`Process args: ${process.argv}`)
