// Check for user consent before proceeding
if (getCookie('consent') === 'true') {
    setupHeartButtons();
}

// Function to set a cookie
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/; Secure";
}

// Function to get a cookie
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Function to setup heart buttons
function setupHeartButtons() {
    document.querySelectorAll('.heart-button').forEach(button => {
        var liked = getCookie(button.getAttribute("id")) === "true";
        button.setAttribute('data-liked', liked);
        button.addEventListener('click', () => {
            liked = !liked;
            button.setAttribute('data-liked', liked);
            setCookie(button.getAttribute("id"), liked, 30);  // Store state in cookies for 30 days
        });
    });
}

