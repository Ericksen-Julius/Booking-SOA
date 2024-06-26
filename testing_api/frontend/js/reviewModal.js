// Modal functionality
const modal = document.getElementById('reviewModal');

// Function to open the modal
function openReviewModal() {
    modal.style.display = 'block';
}

// Function to close the modal
function closeReviewModal() {
    modal.style.display = 'none';
}

// Close the modal if clicked outside of it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

// Your existing JavaScript for rating and options display
const allStar = document.querySelectorAll('.rating .star');
const ratingValue = document.querySelector('.rating input');

allStar.forEach((item, idx) => {
    item.addEventListener('click', function () {
        let click = 0;
        ratingValue.value = idx + 1;

        allStar.forEach(i => {
            i.classList.replace('bxs-star', 'bx-star');
            i.classList.remove('active');
        });
        for (let i = 0; i < allStar.length; i++) {
            if (i <= idx) {
                allStar[i].classList.replace('bx-star', 'bxs-star');
                allStar[i].classList.add('active');
            } else {
                allStar[i].style.setProperty('--i', click);
                click++;
            }
        }
        
        // Call the function to display options based on the rating
        displayOptions(ratingValue.value);
    });
});

function displayOptions(rating) {
    // Define your options here
    const improvements = ['Option A', 'Option B', 'Option C']; // Things that can be improved
    const issues = ['Issue A', 'Issue B', 'Issue C']; // Things that didn't go well
    const positives = ['Positive A', 'Positive B', 'Positive C']; // Things that went well

    // Clear previous options
    const optionsContainer = document.querySelector('.options-container');
    if (optionsContainer) {
        optionsContainer.innerHTML = '';
    }

    let optionsToDisplay;
    const optionsTitle = document.querySelector('.options-title');

    if (rating < 3) {
        optionsTitle.textContent = 'What went wrong?';
        optionsToDisplay = issues;
    } else if (rating < 5) {
        optionsTitle.textContent = 'What can be improved?';
        optionsToDisplay = improvements;
    } else if (rating == 5) {
        optionsTitle.textContent = 'What went well?';
        optionsToDisplay = positives;
    }

    // Create and append new checkbox inputs
    if (optionsToDisplay) {
        const form = document.createElement('form');
        form.className = 'options-form';
        optionsToDisplay.forEach(option => {
            const inputGroup = document.createElement('div');
            inputGroup.className = 'input-group';

            const input = document.createElement('input');
            input.type = 'checkbox';
            input.id = option;
            input.name = 'options';
            input.value = option;

            const label = document.createElement('label');
            label.htmlFor = option;
            label.textContent = option;

            inputGroup.appendChild(input);
            inputGroup.appendChild(label);
            form.appendChild(inputGroup);
        });

        if (!optionsContainer) {
            const newOptionsContainer = document.createElement('div');
            newOptionsContainer.className = 'options-container';
            document.querySelector('.wrapper').appendChild(newOptionsContainer);
            newOptionsContainer.appendChild(form);
        } else {
            optionsContainer.appendChild(form);
        }
    }
}
