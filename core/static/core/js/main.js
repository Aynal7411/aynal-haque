function dismissAlert() {
    document.getElementById('site-alert').style.display = 'none';
    // Set cookie for 1 day
    document.cookie = "alert_dismissed=1; max-age=86400; path=/";
}

// Check if cookie exists
function checkAlertCookie() {
    if (document.cookie.split(';').some((item) => item.trim().startsWith('alert_dismissed='))) {
        document.getElementById('site-alert').style.display = 'none';
    }
}

// Run on page load
window.onload = checkAlertCookie;