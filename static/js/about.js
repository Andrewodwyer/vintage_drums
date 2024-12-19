document.addEventListener("DOMContentLoaded", function() {
    // Handle Edit Review button click
    const editButtons = document.querySelectorAll('.btn-edit');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const reviewId = this.getAttribute('data-review_id');
            window.location.href = `/edit_review/${reviewId}/`;
        });
    });

    // Handle Delete Review button click
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const reviewId = this.getAttribute('data-review_id');
            const confirmation = confirm("Are you sure you want to delete this review?");
            if (confirmation) {
                // Make a POST request to delete the review
                fetch(`/delete_review/${reviewId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value
                    }
                }).then(response => {
                    if (response.ok) {
                        window.location.reload();
                    } else {
                        alert("There was an issue deleting the review.");
                    }
                });
            }
        });
    });
});
