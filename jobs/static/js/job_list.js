document.addEventListener('DOMContentLoaded', function() {
    const jobs = document.querySelectorAll('.job');
    jobs.forEach(job => {
        job.addEventListener('click', function() {
            const jobTitle = this.querySelector('h3').textContent;
            alert('You clicked on ' + jobTitle);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    console.log('Job list page loaded');
});
