document.addEventListener('DOMContentLoaded', function () {
    async function sendBookingData() {
        const data = {
            user_id: 1,
            type: "Hotel",
            total_price: 400000,
            provider_name: "Amaris",
            room_type: 2,
            check_in_date: "2024-07-04",
            check_out_date: "2024-08-04",
            number_of_rooms: 2
        };
        try {
            const response = await fetch('http://localhost:8000/booking', {
                method: 'POST',
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            console.log('Success:', result);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    var buttonPost = document.getElementById('book');
    buttonPost.addEventListener('click', function () {
        sendBookingData();
    })
})


