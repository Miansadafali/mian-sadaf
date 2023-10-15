const topicBox = document.querySelector('.topic'),
arrowIcons = document.querySelectorAll('.dragging-icon i'),
topicItems = document.querySelectorAll('.topic a');


let isDragging = false;

const handleIcons = () => {
    let scrollVal = Math.round(topicBox.scrollLeft);
    let maxScroll = topicBox.scrollWidth - topicBox.clientWidth;
    arrowIcons[0].parentElement.style.display = scrollVal > 1 ? "flex" : "none";
    arrowIcons[1].parentElement.style.display = maxScroll > scrollVal ? "flex" : "none";
};

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        topicBox.scrollLeft += icon.id === "left" ? -150 : 150;
        setTimeout(() => handleIcons(), 50);
    });
});

topicBox.addEventListener("mousedown", () => {
    isDragging = true;
});

topicBox.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    topicBox.scrollLeft -= e.movementX;
    topicBox.classList.add("grabbing");
});

document.addEventListener("mouseup", () => {
    isDragging = false;
    topicBox.classList.remove("grabbing");
});


// active logic
// const urlParams = new URLSearchParams(window.location.search);
// const topic = urlParams.get('topic');

// document.addEventListener("DOMContentLoaded", () => {
//     if (topic) {
//         topicItems.forEach(item => {
//             if (item.innerText === topic) {
//                 console.log(item);
//                 item.classList.add("active");
//             }
//         });
//     }
// });

topicItems.forEach(item => {
    item.addEventListener("click", (event) => {
        topicItems.forEach(item => item.classList.remove("active"));
        item.classList.add("active");
        
    });
});