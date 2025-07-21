// Select buttons and paragraph
const greetBtn = document.getElementById("greetBtn");
const colorBtn = document.getElementById("changeColorBtn");
const hideBtn = document.getElementById("hideTextBtn");
const text = document.getElementById("displayText");

// Greet button click
greetBtn.addEventListener("click", () => {
    alert("Hello! Have a great day!");
});

// Change background color
colorBtn.addEventListener("click", () => {
    document.body.style.backgroundColor = "#e0f7fa";
});

// Hide text on click
hideBtn.addEventListener("click", () => {
    text.style.display = "none";
});
