document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        const username = document.getElementById('id_username').value;
        const password1 = document.getElementById('id_password1').value;
        const password2 = document.getElementById('id_password2').value;

        if (password1 !== password2) {
            e.preventDefault();
            alert('Passwords do not match');
        }
    });
});
