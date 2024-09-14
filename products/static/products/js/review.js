const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_content");
const reviewRating = document.getElementById("id_rating");
const reviewTitle = document.getElementById("id_title");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

console.log("IN STATIC JS")

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    let revTitle = document.getElementById(`title${reviewId}`).innerText;
    let rating = document.getElementById(`rating${reviewId}`).innerText;
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewTitle.value = revTitle;
    reviewRating.value = rating; 
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}