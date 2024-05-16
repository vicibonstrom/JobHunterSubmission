document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        alert('Login attempt for ' + username);

        if (username && password) {
            this.submit();
        }
    });
});
