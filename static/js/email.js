/* Variables for email.js */
let formName = document.getElementById('fromName');
let formEmail = document.getElementById('email');
let message = document.getElementById('message');
var errorMsgName = document.getElementById('name-error');
var errorMsgEmail = document.getElementById('email-error');
var errorMsgMsg = document.getElementById('message-error');

/* Validation to make sure that all fields have value to send */
function validateEmailForm() {
    const name = document.querySelector('#fromName').value;
    const email = document.querySelector('#email').value;
    const msg = document.querySelector('#message').value;
    if (name === "") {
        errorMsgName.innerHTML = `Please enter your full name`;
        errorMsgName.style.color = '#FF0000';
    } else if (email === "") {
        errorMsgEmail.innerHTML = `Please enter your full email address`;
        errorMsgEmail.style.color = '#FF0000';
    } else if (msg === "") {
        errorMsgMsg.innerHTML = `Please enter a message`;
        errorMsgMsg.style.color = '#FF0000';
    } else {
        sendEmail();
    }
    return false;
}

/* Function will send the the contactFrom values to the site owner if validation passed. 
/* Code written with the help of the official EmailJS tuttorial https://www.emailjs.com/docs/tutorial/creating-contact-form/ */
function sendEmail() {
    errorMsgName.remove();
    errorMsgEmail.remove();
    errorMsgMsg.remove();
    emailjs.init('user_TRwsZUpJla2MRcQgJKZEc');
    emailjs.send('service_vgdcg0c', 'ms2-email', {
       'from_name': formName.value,
       'from_email': formEmail.value,
       'message': message.value
    }).then(
        function (response) {
            // Email sent - Success message
           alert('Your message was successfully sent!');
       },
        function (error) {
            // Email failed - Error message
           alert('Ooopsie, your message has not been sent. All the required fields are filled in correctly?');
       },

       );
       
       resetForm();
}

/* Resetting from after sending message */
function resetForm() {
    document.getElementById("contactForm").reset();
}