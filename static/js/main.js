// Code from I think therefore I blog (easily customized for multiple alerts)
setTimeout(function () {
    let messages = document.querySelectorAll('.alert'); 
    messages.forEach(function (message) {
        message.classList.remove('show'); 
        setTimeout(function () {
            message.remove(); 
        }, 200); 
    });
}, 5000);
