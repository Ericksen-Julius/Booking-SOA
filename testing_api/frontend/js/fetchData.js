let booking_id = 0;
let booking_type

async function getData() {
    const params = new URLSearchParams(window.location.search);
    const booking_code = params.get('booking_code');
    const provider = document.getElementById('provider_name');
    const total_price = document.getElementById('totalPrice');


    if (!booking_code) {
        document.body.innerHTML = '<h1>Access Denied</h1>';
        return;
    }

    try {
        const response = await fetch(`http://localhost:8000/bookingDetails/${booking_code}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        var result = await response.json();
        result = result['booking details']
        booking_id = result.id;
        booking_type = result.booking_type;
        console.log("result", booking_id);
        var url = '';
        let providerDetails;
        let resultDetails;
        console.log(result.booking_code)

        if (result.booking_code.charAt(0) === "H") {
            try {
                const response = await fetch(`http://3.215.46.161:8011/hotel`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                providerDetails = await response.json();
                console.log("PROVIDER", providerDetails);
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch(`http://3.215.46.161:8011/hotel/room_type/${result.room_type}`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                resultDetails = await response.json();

                console.log("RESULTDETAIL", resultDetails);
            } catch (error) {
                console.error('Error:', error);
            }
        } else if (result.booking_code.charAt(0) == "A") {
            //AIrline
        } else if (result.booking_code.charAt(0) == "R") {
            // Rental
            try {
                // Nanti ganti url api rental
                const response = await fetch(`http://3.215.46.161:8011/hotel`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                console.log(providerDetails);
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch(`${url}/car/room_type/${result.car_id}`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                resultDetails = await response.json();
                console.log(providerDetails);
            } catch (error) {
                console.error('Error:', error);
            }
        } else if (result.booking_code.charAt(0) == "T") {
            // Attraction

        } else {
            return "Error Booking code not valid", 400;
        }

        provider.innerHTML = result.provider_name;
        total_price.innerHTML = formatCurrency(result.total_price);
        let UIType = result.booking_code.charAt(0);

        let details;
        let info = `
            <img src="./assets/hotel.jpeg" alt="" class="w-100 mb-3">
                    <div class="row mb-2">
                        <div class="col-7">
                            ${providerDetails.provider_name}
                        </div>
                        <div class="col-1"></div>
                        <div class="col-4 text-primary fw-bolder text-end">
                            Show Map
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            ${providerDetails.provider_address}
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            ${providerDetails.provider_city}
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            ${providerDetails.provider_country}
                        </div>
                    </div>
                    <hr style="border: none; border-top: 2px solid #0d6efd;">
                    <div class="row mb-2">
                        <div class="fw-bolder col-12">
                            Got a question?
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            +62 123456789
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="text-primary col-12">
                            Email the property
                        </div>
                    </div>
                    <hr style="border: none; border-top: 2px solid #0d6efd;">
                    <div class="row mb-2">
                        <div class="col-12">
                            &#x3F; <span class="fw-bolder">Need Help?</span>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12 text-primary">
                            Contact customer service
                        </div>
                    </div>
                `;

        let book = `
            <div class="row mb-2">
                <div class="col-6 text-center">
                    <p class="fw-bolder mb-2">Booking code</p>
                    <p>${result.booking_code}</p>
                </div>
                <div class="col-6 text-center">
                    <p class="fw-bolder mb-2">Payment method</p>
                    <p>GoPay</p>
                </div>
            </div>`;

        let recipient = `
            <div class="col-sm-4 col-6 text-center">
                <p class="fw-bolder mb-2">Recipient name</p>
                <p>Yan Witanto</p>
            </div>
            <div class="col-sm-4 col-6 text-center">
                <p class="fw-bolder mb-2">Phone number</p>
                <p>08182738263</p>
            </div>
            <div class="col-sm-4 col-12 text-center">
                <p class="fw-bolder mb-2">Email address</p>
                <p>yan@gmail.com</p>
            </div>`;

        if (UIType === 'H') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Room Type</p>
                            <p>${resultDetails.type}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Night(s)</p>
                            <p>${result.number_of_nights}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Quantity</p>
                            <p>${result.number_of_nights}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. ${resultDetails.total_price}</p>
                        </div>

                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Check-in</p>
                            <p>${convertDateToIndonesian(result.check_in_date)}</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Check-out</p>
                            <p>${convertDateToIndonesian(result.check_out_date)}</p>
                        </div>
                    </div>
                </div>`;
        } else if (UIType === 'A') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Flight class</p>
                            <p>Economy</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Flight id</p>
                            <p>${result.flight_id}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Quantity</p>
                            <p>1</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. 15,000,000</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Departure time</p>
                            <p>Sat, June 1 2024 10:00 PM</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Arrival time</p>
                            <p>Sat, June 3 2024 12:00 PM</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">From</p>
                            <p>Surabaya</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">To</p>
                            <p>Jakarta</p>
                        </div>
                    </div>
                </div>`;
        } else if (UIType === 'R') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Car</p>
                            <p>${resultDetails.car_brand} ${resultDetails.car_name}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Day(s)</p>
                            <p>${calculateDays(resultDetails.pickupDate, resultDetails.returnDate)} Days</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Is With Driver</p>
                            <p>${result.is_with_driver == true ? 'Yes' : 'No'}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. ${resultDetails.car_price}/Day</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Pick Up Date</p>
                            <p>${convertDateToIndonesian(result.pickup_date)}</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Return Date</p>
                            <p>${convertDateToIndonesian(result.return_date)}</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Pick Up Location</p>
                            <p>${result.pickup_location}</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Return Location</p>
                            <p>${result.return_location}</p>
                        </div>
                    </div>
                </div>`;
        } else if (UIType === 'T') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="./assets/vip-hotel.jpg" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-4">
                            <p class="fw-bolder mb-2">Type</p>
                            <p>${result.paket_attraction_id}</p>
                        </div>
                        <div class="col-4">
                            <p class="fw-bolder mb-2">Quantity</p>
                            <p>${result.number_of_tickets}</p>
                        </div>
                        <div class="col-4">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. 15,000,000</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">E-ticket number</p>
                            <p>#345</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Visit date</p>
                            <p>${result.visit_date}</p>
                        </div>
                    </div>
                </div>`;
        }
        document.getElementById('detailContainer').innerHTML = details;
        document.getElementById('infoContainer').innerHTML = info;
        document.getElementById('bookContainer').innerHTML = book;
        document.getElementById('recipientContainer').innerHTML = recipient;

    } catch (error) {
        console.error('Error:', error);
    }


}

async function getReview(booking_id, booking_type) {
    try {


        const response = await fetch(`http://localhost:8000/completed_bookings/${booking_type}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const result = await response.json();
        console.log(result)
        if (result.length === 0) {
            reviewButton.innerHTML = "Write a Review";
        } else {
            reviewButton.innerHTML = "Edit Review";
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function postReview(booking_id, rating, comment) {
    try {
        const data = {
            booking_id: booking_id,
            rating: rating,
            comment: comment,
            option_id: []
        };
        const response = await fetch(`http://3.226.141.243:8004/review`, {
            method: 'POST',
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const result = await response.json();
        if (result.message == "Review added successfully") {
            Swal.fire({
                title: "Success",
                text: "Berhasil memberikan review!",
                icon: "success"
            }).then((result) => {
                if (result.isConfirmed) {
                    location.reload();
                }
            });
        }
    } catch (error) {
        console.error('Error:', error);
    }
}



function formatCurrency(amount) {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR' }).format(amount);
}

function convertDateToIndonesian(dateStr) {
    const months = [
        'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
        'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
    ];

    const [year, monthIndex, day] = dateStr.split('-');

    const monthName = months[parseInt(monthIndex, 10) - 1];

    const formattedDate = `${parseInt(day, 10)} ${monthName} ${year}`;

    return formattedDate;
}

document.addEventListener('DOMContentLoaded', (event) => {
    getData();
    const modal = document.getElementById('reviewModal');
    let valueStar = 0
    const comment = document.getElementById('comment');
    const buttonSubmit = document.getElementById('submitComment');
    const stars = modal.querySelectorAll('.rating-stars i');
    stars.forEach(star => {
        star.addEventListener('click', () => {
            const value = parseInt(star.getAttribute('data-value'));
            stars.forEach(s => s.classList.remove('active'));
            for (let i = 0; i < value; i++) {
                stars[i].classList.add('active');
            }
            // document.querySelector('.rating input').value = value;
            valueStar = value;
            console.log(valueStar)
        });
    });
    buttonSubmit.addEventListener('click', () => {
        console.log(booking_id)
        console.log(valueStar)
        console.log(comment.value)
        postReview(booking_id, valueStar, comment.value)
    })

});
