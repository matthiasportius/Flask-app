function functionnav() {
    const x = document.getElementById("nav");
    if (x.className === "responsive") {
        x.className = "";
    }
    else {
        x.className="responsive";
    } 
}

const acc = document.getElementsByClassName("accordion");
let i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        const panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}










const register_form = document.getElementsByClassName("register");
const password = document.getElementById("password");
const password_error = document.querySelector("span.register-error");

// window.addEventListener("load", () => {
//     if (password.value.length === 0) {
//         password.className = "empty";
//     }
// });

password.addEventListener("input", (event) => {
    if (password.validity.valid) {
        password_error.textContent = "";
        password_error.className = "register-error";
    } else {
        showError();
    }
});

function showError() {
    if (password.validity.tooShort) {
        password_error.textContent = `Password should be at least ${password.minLength} characters`;
    } else if (password.validity.valueMissing) {
        password_error.textContent="You need to enter a password";
    }
    password_error.className="register-error active";
}

// HTMLInputElement.validationMessage
// checkValidity()
// reportValidity()
// properties like tooShort specify what went wrong
