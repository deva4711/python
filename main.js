// Select the button and paragraph
const button = document.getElementById("changeBtn");
const paragraph = document.getElementById("message");

// Add click event listener
button.addEventListener("click", function () {
    paragraph.textContent = "The message has been updated!";
});

// Add mouseover event listener
paragraph.addEventListener("mouseover", function () {
    paragraph.style.color = "green";
});

// Add mouseout event to reset style
paragraph.addEventListener("mouseout", function () {
    paragraph.style.color = "black";
});
