function validCheck() {
    let fullName = document.myRegisterForm.name.value
    let userName = document.myRegisterForm.username.value
    let eMail = document.myRegisterForm.email.value
    let password1 = document.myRegisterForm.password1.value
    let password2 = document.myRegisterForm.password2.value
    let error = document.getElementById('emsg')

    if (fullName === "" || fullName === null) {
        error.classList.add('err')
        error.textContent = "Full Name cannot be empty"
        document.myRegisterForm.name.focus()
        return false
    }

    if (userName === "" || userName=== null) {
        error.classList.add('err')
        error.textContent = "Username cannot be empty"
        document.myRegisterForm.name.focus()
        return false
    }


    let atPos = eMail.indexOf('@')
    let dotPos = eMail.indexOf('.')
    if (atPos < 1 || dotPos - atPos < 2 || eMail.length - dotPos <= 2) {
        error.classList.add('err')
        error.textContent = "Invalid Email"
        document.myRegisterForm.email.focus()
        return false
    }


    if (password1.length < 8) {
        error.classList.add('err')
        error.textContent = "Invalid Password, Your password length must be at least 8"
        document.myRegisterForm.password1.focus()
        return false
    } else if (password1 !== password2) {
        error.classList.add('err')
        error.textContent = "Passwords Does not match"
        document.registerForm.password1.focus()
        return false
    }

    return true
}