document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Here you can handle the login logic or validation
    alert('Login attempt for ' + username);
});
