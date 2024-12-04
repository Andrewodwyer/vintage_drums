document.addEventListener('DOMContentLoaded', function () {
    const likeForm = document.getElementById('like-form');
    const likeIcon = document.getElementById('like-icon');
    const likeText = document.getElementById('like-text');
    const likeCount = document.getElementById('like-count');

    document.getElementById('like-container').addEventListener('click', function (e) {
        e.preventDefault(); // Prevent form submission
        console.log('Like container clicked!');
        const formData = new FormData(likeForm);

        fetch(likeForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.user_likes) {
                likeIcon.classList.remove('icon-primary');
                likeIcon.classList.add('icon-success');
                likeText.textContent = "Liked!";
            } else {
                likeIcon.classList.remove('icon-success');
                likeIcon.classList.add('icon-primary');
                likeText.textContent = "Like";
            }
            likeCount.textContent = `${data.like_count} Likes`;
        })
        .catch(error => console.error('Error:', error));
    });
});
