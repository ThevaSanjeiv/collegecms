let loginForm = document.getElementById("LoginForm");
let emailInput = document.querySelector('[name="email"]');
let passwordInput = document.querySelector('[name="password"]');
let [emailValidate, passwordValidate] = [false, false];

loginForm.addEventListener("submit", (e) => {
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    emailInput.value = email;
    passwordInput.value = password;
    if (!email) {
        emailInput.setCustomValidity("Please enter your Mail ID.");
        emailInput.reportValidity();
        e.preventDefault();
        return;
    } else if (!emailValidate) {
        emailInput.setCustomValidity("Please enter a valid Mail ID.");
        emailInput.reportValidity();
        e.preventDefault();
        return;
    } else {
        emailInput.setCustomValidity("");
    }

    if (!password) {
        passwordInput.setCustomValidity("Please enter your password.");
        passwordInput.reportValidity();
        e.preventDefault();
        return;
    } else if (!passwordValidate) {
        passwordInput.setCustomValidity("Password must contain at least 8 characters.");
        passwordInput.reportValidity();
        e.preventDefault();
        return;
    } else {
        passwordInput.setCustomValidity("");
    }
});

emailInput.addEventListener("input", (e) => {
    const email = e.target.value;
    if (email.includes("@") && email.includes(".com")) {
        emailValidate = true;
        emailInput.setCustomValidity("");
    } else {
        emailValidate = false;
        emailInput.setCustomValidity("Please enter a valid Mail ID.");
    }
});

passwordInput.addEventListener("input", (e) => {
    const password = e.target.value;
    if (password.length >= 8) {
        passwordValidate = true;
        passwordInput.setCustomValidity("");
    } else {
        passwordValidate = false;
        passwordInput.setCustomValidity("Password must contain at least 8 characters.");
    }
});
