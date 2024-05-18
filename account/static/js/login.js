
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        alert('Login attempt for ' + username);

        if (username && password) {
            // Allow form submission
            return true;
        } else {
            e.preventDefault();
            alert('Please fill in both fields');
        }
    });
});
