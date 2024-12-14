document.addEventListener('DOMContentLoaded', function() {
    const likeForm = document.getElementById('like-form');
    const likeIcon = document.getElementById('like-icon');
    const likeText = document.getElementById('like-text');
    const likeCount = document.getElementById('like-count');
    
    document.getElementById('like-container').addEventListener('click', function() {
        // Prevent the default form submission
        const formData = new FormData(likeForm);
        
        fetch(likeForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            // Update icon and text based on response
            if (data.user_liked) {
                likeIcon.classList.remove('icon-primary');
                likeIcon.classList.add('icon-success');
                likeText.classList.remove('text-primary');
                likeText.classList.add('text-success');
                likeText.textContent = "Liked!";
            } else {
                likeIcon.classList.remove('icon-success');
                likeIcon.classList.add('icon-primary');
                likeText.classList.remove('text-success');
                likeText.classList.add('text-primary');
                likeText.textContent = 'Like?';
            }
            likeCount.textContent = `${data.like_count} Likes`;
        })
        .catch(error => console.error('Error:', error));
    });
});
