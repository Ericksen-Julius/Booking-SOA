document.addEventListener('DOMContentLoaded', function () {
    var booking = ""
    var containerBooking = document.getElementById('containerList')
    async function getBookingData() {
        try {
            const response = await fetch('http://localhost:8000/booking/1', {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            // console.log('Success:', result);
            result.forEach(element => {
                booking += `
                    <div class="col-lg-4">
                        <div class="booking-item">
                            <img src="./assets/hotel.jpeg" alt="Provider Image" class="provider-img">
                            <div class="flex-grow-1 d-flex flex-column">
                                <div class="booking-code">Booking Code: ${element.booking_code}</div>
                                <div>Type: ${element.booking_type}</div>
                                <div>Provider Name: ${element.provider_name}</div>
                                <div>Total Price: Rp. ${formatRupiah(element.total_price)}</div>
                                <button class="btn btn-primary btn-detail mt-2 align-self-end">View Details</button>
                            </div>
                        </div>
                    </div>`
            });
            containerBooking.innerHTML = booking
        } catch (error) {
            console.error('Error:', error);
        }
    }
    function formatRupiah(number) {
        return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }
    getBookingData()
})


