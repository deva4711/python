// i. Function Declaration
function greet() {
    document.getElementById("outputText").textContent = "Hello from Function Declaration!";
}

// ii. Function Expression
const showMessage = function() {
    document.getElementById("outputText").textContent = "Hello from Function Expression!";
};
document.getElementById("expressionBtn").addEventListener("click", showMessage);

// iii. Arrow Function
const arrowFunc = () => {
    document.getElementById("outputText").textContent = "Hello from Arrow Function!";
};
document.getElementById("arrowBtn").addEventListener("click", arrowFunc);
