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

// Show the banner if consent hasn't been given
if (getCookie('consent') !== 'true') {
    document.getElementById('cookie-consent-banner').style.display = 'block';
}

// Accept all cookies
document.getElementById('accept-cookies').addEventListener('click', () => {
    setCookie('consent', 'true', 365); // Store consent for 1 year
    document.getElementById('cookie-consent-banner').style.display = 'none';
    // Additional functionality to record consent details can be added here
    location.reload();
});

// Decline all cookies
document.getElementById('decline-cookies').addEventListener('click', () => {
    setCookie('consent', 'false', 365); // Store non-consent for 1 year
    document.getElementById('cookie-consent-banner').style.display = 'none';
    // Additional functionality to handle non-consent can be added here
});

