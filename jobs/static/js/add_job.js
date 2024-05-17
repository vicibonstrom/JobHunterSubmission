document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        const title = document.getElementById('id_title').value;
        const description = document.getElementById('id_description').value;
        if (!title || !description) {
            e.preventDefault();
            alert('Please fill in all required fields.');
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
    console.log('Add job page loaded');
});
