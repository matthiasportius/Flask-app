// add later for responsive nav on mobile with symbol after
// function functionnav() {
//     var x = document.getElementById("IDnav");
//     if (x.className === "responsive") {
//         x.className = "";
//     }
//     else {
//         x.className="responsive";
//     } 
// }

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}