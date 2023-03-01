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


const username = document.getElementById("username");
const mail = document.getElementById("mail");
const rpassword = document.getElementById("rpassword");
const password = document.getElementById("password");
const register = [username, mail, password, rpassword]
const password_error = document.querySelector("span.register-error");

window.addEventListener("load", () => {
    for (const x of register) {
        if (x.value.length === 0) {
            x.className = "empty";
        }
    }
});

for (const x of register) {
    x.addEventListener("input", () => {
        x.className = "";
    });
}

password.addEventListener("input", () => {
    password.className = ""
    if (password.validity.valid) {
        password_error.textContent = "";
        password_error.className = "register-error";
    } else {
        showError();
    }
});

function showError() {
    if (password.validity.valueMissing) {
        password_error.textContent="You need to enter a password";
    } else if (password.validity.tooShort) {
        password_error.textContent = `Password should be at least ${password.minLength} characters`;
    } else {
        password_error.textContent = "Allowed: letters, numbers, ?, !, #";
    }
    password_error.className="register-error active";
}
