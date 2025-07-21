function changeContent() {
    // Select element by ID
    const heading = document.getElementById("main-heading");
    heading.textContent = "Welcome to JavaScript DOM!";

    // Select elements by class name
    const infoElements = document.getElementsByClassName("info");
    for (let i = 0; i < infoElements.length; i++) {
        infoElements[i].style.color = "blue";
    }

    // Select elements by tag name
    const paragraphs = document.getElementsByTagName("p");
    paragraphs[1].style.fontWeight = "bold";

    // Select using querySelector
    const firstInfo = document.querySelector(".info");
    firstInfo.style.backgroundColor = "lightyellow";

    // Select using querySelectorAll
    const allInfo = document.querySelectorAll(".info");
    allInfo.forEach(el => el.style.border = "1px solid red");
}
