// Code from I think therefore I blog (easily customized for multiple alerts)
setTimeout(function () {
    let messages = document.querySelectorAll('.alert'); // Alle Elemente mit der Klasse 'alert'
    messages.forEach(function (message) {
        message.classList.remove('show'); // Entferne die 'show'-Klasse, um die Anzeige auszublenden
        setTimeout(function () {
            message.remove(); // Entferne das Element aus dem DOM
        }, 200); // Hier kannst du die Dauer der Ausblendanimation einstellen
    });
}, 2500);
